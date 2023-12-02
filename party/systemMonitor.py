from pymongo import MongoClient
from datetime import datetime
import psutil

class SystemMonitor:

    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    collection = client['partyyy']['systemMonitor']
    initialized = True

    @classmethod
    def init(self, cls):
        if not cls.initialized:
            self.cls.client = MongoClient(self.cls.CONNECTION_STRING)
            self.cls.collection = cls.client['partyyy']['systemMonitor']
            self.cls.initialized = True

    @classmethod
    def record_system_info(self, cls):
        if not self.cls.initialized:
            self.cls.init()

        self.cpu_percent = psutil.cpu_percent(interval=1)
        self.memory_percent = psutil.virtual_memory().percent
        self.uptime = int(round(psutil.boot_time()))

        data = {
            'timestamp': datetime.now(),
            'cpu_percent': self.cpu_percent,
            'memory_percent': self.memory_percent,
            'uptime': self.uptime
        }

        self.cls.collection.insert_one(data)

    @classmethod
    def getStatus(self) -> list[bool]:
        return list(self.record_system_info()['status'])
