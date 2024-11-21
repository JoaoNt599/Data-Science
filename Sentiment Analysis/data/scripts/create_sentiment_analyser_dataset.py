import random
import json
import re
import string

from pyspark import SparkContext
from nltk.corpus import stopwords
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples


def postive_tokens():
    return twitter_samples.tokenized('positive_tweets.json')


def negative_tokens():
    return twitter_samples.tokenized('negative_tweets.json')


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


def get_tokens(token_list: list):
    return dict([token, True] for token in token_list)


def build_dataset(token_list: list, sentiment: str):
    return token_list, sentiment


def get_spark_session() -> SparkSession:
    spark_conf: SparkConf = SparkConf()
    spark_conf.setAll([
        ('spark.master', 'spark://spark-master:7077'),
        ('spark.app.name', 'spark-engsoft37'),
    ])

    return SparkSession.builder.config(conf=spark_conf).getOrCreate()


def save_dataset(dataset: str):
    path = "/opt/workspace/output/dataset.json"
    with open(path, "w") as json_file:
        json_file.write(dataset)


def create_dataset():
    spark = get_spark_session()
    spark_context: SparkContext = spark.sparkContext
    stop_words = stopwords.words('english')

    positive_token = spark_context.parallelize(postive_tokens())
    negative_token = spark_context.parallelize(negative_tokens())

    cleaned_positive_token = positive_token.map(lambda r: remove_noise(r, stop_words))
    cleaned_negative_token = negative_token.map(lambda r: remove_noise(r, stop_words))

    positive_tokens_model = cleaned_positive_token.map(get_tokens)
    negative_tokens_model = cleaned_negative_token.map(get_tokens)

    positive_dataset = positive_tokens_model.map(lambda r: build_dataset(r, "Positive"))
    negative_dataset = negative_tokens_model.map(lambda r: build_dataset(r, "Negative"))

    dataset_merged = positive_dataset.union(negative_dataset)
    dataset = dataset_merged.take(10000)

    random.shuffle(dataset)

    train = dataset[:7000]

    spark.stop()

    save_dataset(json.dumps(train))


if __name__ == "__main__":
    create_dataset()
