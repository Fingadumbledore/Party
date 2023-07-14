from pymongo import MongoClient
from enum import Enum
import random


def generate_kiste(count: int) -> list[bool]:
    return [random.choice([True, False]) for _ in range(count)]


class MateKiste():
    def __init__(self):
        pass
