import logging
import os
import time
from time import gmtime, strftime
from pymongo import MongoClient


class CustomFormatter(logging.StreamHandler):
    def emit(self, record):
        return super().emit(record)


class DatabaseLoggingHandler(logging.Handler):

    def __init__(self, database='logs', collection="logs"):
        logging.Handler.__init__(self)
        self.client = MongoClient("localhost",username='root', password='example',)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def emit(self, record):
        """save log record in file or database"""
        formatted_message = self.format(record)

        database_record = {
            "level": record.levelname,
            "module": record.module,
            "line": record.lineno,
            "asctime": record.asctime if getattr(record, "asctime", None) else strftime("%Y-%m-%d %H:%M", gmtime()),
            "message": record.message # use `formatted_message` for store formatted log
        }

        try:
            self.collection.insert_one(database_record)
        except Exception as e:
            print(e)
