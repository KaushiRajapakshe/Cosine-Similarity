"""
    Database Controller
"""


# Importing all required libraries to database controller
class DatabaseController:

    def get_short_question(self):
        short_answer_ref = self.db.collection(u'shortQuestion')
        query = (short_answer_ref.order_by(u'id').start_after({u'id': self.random_id}).limit(10))
        self.random_id += 10
        docs = query.get()
        doc_id = 1
        for doc in docs:
            self.question_set[doc_id] = doc.to_dict()
            doc_id += 1
        return self.question_set
