from pymongo import MongoClient
from datetime import datetime
import psutil
import os

class SystemMonitor:

    CONNECTION_STRING = None
    client = None
    collection = None
    initialized = False

    @classmethod
    def init(self):
        self.CONNECTION_STRING = "mongodb://localhost:27017/"
        self.client = MongoClient(self.CONNECTION_STRING)
        self.collection = self.client['partyyy']['systemMonitor']
        self.initialized = True
