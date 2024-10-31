from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask import session
import requests
import random
from html import unescape

app = Flask(__name__)
app.config.from_object(Config)

from models import db, User

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize questions
TOTAL_QUESTIONS = 4

''' Fetch questions from API'''
def fetch_question():   
    try:
        response = requests.get('https://opentdb.com/api.php?amount=4&category=17&difficulty=medium&type=multiple')
        response.raise_for_status()
        data = response.json()
        question_info = data['results'][0]
        question = unescape(question_info['question'])
        correct_answer = unescape(question_info['correct_answer'])
        incorrect_answers = [unescape(ans) for ans in question_info['incorrect_answers']]
        all_answers = incorrect_answers + [correct_answer]
        random.shuffle(all_answers)
        return question, correct_answer, all_answers
    except requests.RequestException as e:
        print(f"Error fetching question: {e}")
        return None, None, None

from routes import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
