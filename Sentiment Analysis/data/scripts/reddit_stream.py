import praw
import re
import string
import ast
import json
import requests

from datetime import datetime

from nltk import tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk import NaiveBayesClassifier

from pyspark import SparkContext, RDD
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.streaming import StreamingContext

COMMENTS_API_URL = "http://web-app:3000/comments/"
REDDIT_CLIENT_ID = "6TgyXf-Ie3G0TGHVvGf7Lg"
REDDIT_CLIENT_SECRET = "XLFAALr7j-NHWop-QQNBWLc6Tpus-A"
INTERVAL = 20


def get_spark_session() -> SparkSession:
    spark_conf: SparkConf = SparkConf()
    spark_conf.setAll([
        ('spark.master', 'spark://spark-master:7077'),
        ('spark.app.name', 'spark-engsoft37'),
    ])

    return SparkSession.builder.config(conf=spark_conf).getOrCreate()


def tokenize_string(text):
    return tokenize.word_tokenize(text)


def remove_noise(tokens: list, stop_words: tuple = ()) -> list:
    cleaned_tokens = []

    for token, tag in pos_tag(tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|' \
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)

        token = re.sub("(@[A-Za-z0-9_]+)", "", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def train_model(dataset) -> NaiveBayesClassifier:
    return NaiveBayesClassifier.train(dataset)


def classify_comment(comment, classifier: NaiveBayesClassifier):
    token = dict([token, True] for token in comment)
    sentiment = classifier.classify(token)
    return comment, sentiment


def reddit_comments():
    reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET, user_agent="Marcus Maciel")

    for comment in reddit.subreddit("COVID19").comments(limit=100):
        created_at = datetime.fromtimestamp(int(comment.created_utc)).strftime("%Y-%m-%d %H:%M:%S")
        contents = (comment.body, created_at)
        yield str(contents)


def rfunc(time, rdd):
    return rdd.flatMap(lambda r: reddit_comments())


def apply_sentiment_analysis(rdd, classifier: NaiveBayesClassifier, logger):
    # logger.info(f"RDD_L: {rdd}")

    sentiment_list = []

    for line in rdd:
        # logger.debug(f"Line-RDD: {line}")
        comment = line[0]
        created_at = line[1]
        comment_tokens = remove_noise(tokenize_string(comment))
        apply_sentiment = classify_comment(comment_tokens, classifier)
        sentiment = True if apply_sentiment[1] == "Positive" else False
        content = {
            "comment": comment,
            "sentiment": sentiment,
            "createdAt": created_at
        }

        sentiment_list.append(content)

    try:
        requests.post(COMMENTS_API_URL, data=json.dumps(sentiment_list), headers={"Content-Type": "application/json"})
        # logger.info(f"SENTIMENT_LIST: {sentiment_list}")
    except Exception as e:
        logger.error(f"Erro ao salvar a lista de comentários: {e}")


def output_rdd(time, rdd: RDD, classifier: NaiveBayesClassifier, logger):
    # logger.info(f"TimeD: {time} | RDD-D: {rdd}")
    comment_list = rdd.collect()
    apply_sentiment_analysis(comment_list, classifier, logger)


def stream_data():
    dataset_json = open('/opt/workspace/output/dataset.json', 'r')
    dataset = json.loads(dataset_json.read())
    classifier = train_model(dataset)

    spark = get_spark_session()
    spark_context: SparkContext = spark.sparkContext
    spark_context.setLogLevel("INFO")

    log_4j = spark_context._jvm.org.apache.log4j
    logger = log_4j.LogManager.getLogger(__name__)

    stream_context = StreamingContext(spark_context, INTERVAL)
    stream_rdd = stream_context.sparkContext.parallelize([0])

    stream = stream_context.queueStream([], default=stream_rdd)
    stream_transformed = stream.transform(rfunc)

    coord_stream = stream_transformed.map(lambda line: ast.literal_eval(line))
    coord_stream.foreachRDD(lambda time, rdd: output_rdd(time, rdd, classifier, logger))

    stream_context.start()

    stream_context.awaitTermination()


if __name__ == "__main__":
    stream_data()
