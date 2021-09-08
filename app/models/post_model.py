import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['kenzie']

class Post:
    
    def __init__(self, title: str, author: str, tags: list, content: str) -> None:
        self.title: str = title
        self.author: str = author
        self.tags: list = tags
        self.content: str = content
        self.create_at = datetime.datetime.utcnow()
        self.updated_at = ''
        self.id = 0
    
    def create_id(self):
        list_items = list(db.posts.find())
        id = 0
        for item in list_items:
            if item['id'] > id:
                id = item['id']
        self.id = id + 1

    def create_post(self):
        return db.posts.insert_one(self.__dict__)

    @staticmethod
    def delete_post(id):
        db.posts.delete_one({'id': id})
    
    @staticmethod
    def get_all():
        posts_list = list(db.posts.find())
        for post in posts_list:
            del post['_id']
        return posts_list
    
    @staticmethod
    def get_by_id(id):
        post = db.posts.find_one({'id': id})
        del post['_id']
        return post

    @staticmethod
    def update_post(update_data, id):
        post = db.posts.find_one_and_update({'id': id}, {'$set': update_data})
        del post['_id']
