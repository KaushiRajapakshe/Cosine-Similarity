"""
    Semantic Similarity

    Setup
    * Package requirements
        - !pip install numpy==1.19.2
        - !pip install pandas==1.1.3
        - !pip install tensorflow==2.6.0
        - !pip install transformers==2.11.0

"""

# Press the green button in the gutter to run the script.
from controller.main_controller import MainController
from logic.cosine import similarity
from model.Database import Database
from flask import Flask, request
from logic.firebase_database import DatabaseFirebase
app = Flask(__name__)
main_class = ''


@app.route('/similarity', methods=['POST', 'GET'])
def s_similarity():
    if request.method == 'POST':
        request_data = request.get_json()
        for question in request_data.items():
            sentence1 = question[1]['answer']
            sentence2 = question[1]['submitted_answer']
            score = similarity(sentence1, sentence2)
            question[1]['score'] = str(round((score * 10), 2))
        return request_data
    else:
        return "Hello World! get"


@app.route('/shot_question', methods=['POST', 'GET'])
def shot_question():
    if request.method == 'GET':
        return MainController.main_call(main_class)
    else:
        return "Hello World! post"


class Main:
    def __init__(self):
        self.database = Database()
        DatabaseFirebase.init_firebase(self.database)


if __name__ == '__main__':
    print('Welcome!')

    main_class = Main()
    app.run(debug=True, port=5001)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
