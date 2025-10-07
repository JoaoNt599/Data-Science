from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class MongoDBConnection:

    _instance = None

    def __new__(cls, uri: str, db_name: str):
        if cls._instance is None:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            cls._instance._initialize(uri, db_name)
        return cls._instance
    

    def _initialize(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.sb = None
        self.connect()
    

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print(f"Connected to MongoDB database: {self.db_name}")
        except ConnectionFailure as err:
            print(f"Could not connect to MongoDB: {err}") 
    

    def get_database(self):
        return self.db


# Example usage:
# mongo_conn = MongoDBConnection("mongodb://localhost:27017/", "mydatabase")
# db = mongo_conn.get_database()