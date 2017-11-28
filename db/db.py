from pymongo import MongoClient


def get_Spider_DB():
    url = "192.168.1.99"
    # url = "localhost"
    port = 27017
    db_name = 'weibo_spider'
    client = MongoClient(url, port)
    client[db_name].authenticate('xmtj', '0-=p[]P{}', 'admin')
    db = client[db_name]
    return db


mongodb = get_Spider_DB()


def saveToMongo(username, content, picUrls, time):
    global mongodb
