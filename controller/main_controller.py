"""
    Semantic Similarity

    Setup
    * Package requirements
        - !pip install numpy==1.19.2
        - !pip install pandas==1.1.3
        - !pip install tensorflow==2.6.0
        - !pip install transformers==2.11.0

    Main Controller
"""

# Importing all required libraries to work with the main controller
from controller.database_controller import DatabaseController


class MainController:

    def __init__(self):
        self.database = None

    def main_call(self):
        # initialize firebase
        # Database.init_firebase(self.database)

        return DatabaseController.get_short_question(self.database)
