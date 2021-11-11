"""
    Database class

"""


class Database:

    def __init__(self):
        self.db = ''
        self.question_set = {}
        self.random_id = 0

    # getter method db
    def get_db(self):
        return self.db

    # setter method db
    def set_db(self, db):
        self.db = db

    # getter method question set
    def get_question_set(self):
        return self.question_set

    # setter method question set
    def set_question_set(self, question_set):
        self.question_set = question_set

    # getter method random id
    def get_random_id(self):
        return self.random_id

    # setter method random id
    def set_random_id(self, random_id):
        self.random_id = random_id
