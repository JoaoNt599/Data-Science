from app.flaskr.config import db
from flask import (
    Blueprint, request, current_app, jsonify
)

bp = Blueprint('comments', __name__, url_prefix='/comments')


@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        database = db.get_db()

        sentiment_analysis_list = database.execute('SELECT * FROM comments ORDER BY id DESC LIMIT 50 OFFSET 0')\
            .fetchall()

        comments = map(lambda sa: {'comment': sa['comment'], 'sentiment': sa['sentiment'], 'created_at': sa['created_at']},
            sentiment_analysis_list)

        # current_app.logger.info(f"Comments: {list(comments)}")

        return jsonify(list(comments)), 200, {'ContentType': 'application/json'}

    elif request.method == 'POST':
        sentiment_analysis_list = request.json

        # current_app.logger.info(f"Comments: {sentiment_analysis_list}")

        database = db.get_db()

        for sentiment_analysis in sentiment_analysis_list:
            try:
                database.execute('INSERT INTO comments (comment, sentiment, created_at) VALUES (?,?,?)',
                                 (sentiment_analysis['comment'], sentiment_analysis['sentiment'], sentiment_analysis['createdAt']))

                database.commit()
            except database.IntegrityError as e:
                current_app.logger.error(f"Erro ao inserir o comentário: {e}")

        return {}, 201, {'ContentType':'application/json'}


@bp.route("/chart-data", methods=['GET'])
def chart_data():
    if request.method == 'GET':
        database = db.get_db()
        query = '''
            SELECT 
                count(CASE sentiment WHEN 1 THEN 1 END) as total_positive,
                count(CASE sentiment WHEN 0 THEN 0 END) as total_negative,
                STRFTIME('%H:00', created_at) as hour from comments
            where STRFTIME('%Y-%m-%d', created_at) = STRFTIME('%Y-%m-%d', 'now')
            group by STRFTIME('%H', created_at)
        '''

        result = database.execute(query).fetchall()

        data = map(
            lambda r: {'totalPositive': r['total_positive'], 'totalNegative': r['total_negative'], 'hour': r['hour']},
            result
        )

        # current_app.logger.info(list(data))

        return jsonify(list(data)), 200, {'ContentType':'application/json'}
    else:
        raise Exception(f'Método {request.method} não permitido.')