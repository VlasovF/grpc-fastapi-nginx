from datetime import datetime
import random
import uuid
import string


def rfloat():
    return float(format(random.random(), ".2f"))


def rlocation():
    loc = {
        "lat": 90 - random.random() * 180,
        "lon": 180 - random.random()  *  360
    }
    return loc


def rstr(size: int = 10):
    chars = string.ascii_uppercase
    return ''.join([random.choice(chars) for i in range(size)])


def get_document(n: int = 10):
    data = {
        "article_id": random.randint(0, 10000000),
        "text": rstr(500),
        "title": rstr(),
        "date": datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"),
        "lang": "ru",
        "locations": [rlocation() for i in range(0, random.randint(1, 4))],
        "semantic_vector": [rfloat() for i in range(0, n)],
        "keywords": [f"keyword{i}" for i in range(0, 512)],
        "entities": [rstr() for i in range(0, random.randint(1, 10))],
        "themes": [str(uuid.uuid4()) for i in range(0, n)],
        "class": [str(uuid.uuid4()) for i in range(0, n)]
    }
    return data
