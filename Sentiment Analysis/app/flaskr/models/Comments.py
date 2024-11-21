# from sqlalchemy import Column, Integer, Date, String, Boolean
# from sqlalchemy.schema import UniqueConstraint
# from app.flaskr.config.database import Base
#
#
# class Comment(Base):
#     __tablename__ = 'comments'
#
#     id = Column(Integer, primary_key=True)
#     comment = Column(String(240), unique=False)
#     sentiment = Column(Boolean, unique=False)
#     created_at = Column(Date, unique=False)
#
#     __table_args__ = (UniqueConstraint("comment"),)
#
#     def __init__(self, comment, sentiment, created_at):
#         self.comment = comment
#         self.sentiment = sentiment
#         self.created_at = created_at
#
#     def to_dict(self):
#         return {
#             "comment": self.comment,
#             "sentiment": self.sentiment,
#             "created_at": self.created_at
#         }