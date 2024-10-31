from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from models import User, QuizResult
import requests
import random
from html import unescape
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember_me') == 'on'
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user, remember=remember)
            return redirect(url_for('quiz'))  # Redirect to quiz after login
        flash('Invalid username or password')
    return render_template('login.html', title='Sign In')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register')

@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    # Initialize questions if not already in session or if the current question index is out of range
    if 'questions' not in session or session['current_question_index'] >= len(session['questions']):
        session['questions'] = fetch_questions()  # Fetch questions at the start
        session['current_question_index'] = 0
        session['correct_count'] = 0

    questions = session['questions']
    current_question_index = session['current_question_index']

    if request.method == 'POST':
        selected_answer = request.form.get('answers')
        correct_answer = questions[current_question_index]['correct_answer']

        if selected_answer == correct_answer:
            session['correct_count'] += 1

        session['current_question_index'] += 1

        # Check if we have reached the end of the questions
        if session['current_question_index'] >= len(questions):
            return redirect(url_for('quiz_completed'))

        return redirect(url_for('quiz'))  # Redirect to the same quiz route to show the next question

    # Check if there are questions to display
    if current_question_index < len(questions):
        question = questions[current_question_index]
        return render_template('quiz.html', question=question['text'], answers=question['options'])
    else:
        # If no questions are available, redirect to completion
        return redirect(url_for('quiz_completed'))

@app.route('/quiz_completed')
@login_required
def quiz_completed():
    correct_count = session.get('correct_count', 0)
    total_questions = len(session.get('questions', []))
    return render_template('quiz_completed.html', title='Quiz Completed', correct_count=correct_count, total_questions=total_questions)

@app.route('/results')
@login_required
def results():
    correct_count = session.get('correct_count', 0)
    total_questions = len(session.get('questions', []))
    return render_template('results.html', results=session.get('results', []), correct_count=correct_count, total_questions=total_questions)

@app.route('/submit_quiz', methods=['POST'])
@login_required
def submit_quiz():
    score = calculate_score()  
    timestamp = datetime.now()  
    result = {
        'score': score,
        'timestamp': timestamp
    }
    if 'results' not in session:
        session['results'] = []
    session['results'].append(result)

    return redirect(url_for('results'))

@app.route('/users')
@login_required
def users():
    users = User.query.all()  # Fetch all registered users from the database
    return render_template('users.html', users=users)

def fetch_questions():
    try:
        response = requests.get('https://opentdb.com/api.php?amount=4&category=17&difficulty=medium&type=multiple')
        response.raise_for_status()
        data = response.json()
        questions = []
        for question_info in data['results']:
            question = unescape(question_info['question'])
            correct_answer = unescape(question_info['correct_answer'])
            incorrect_answers = [unescape(ans) for ans in question_info['incorrect_answers']]
            all_answers = incorrect_answers + [correct_answer]
            random.shuffle(all_answers)
            questions.append({
                'text': question,
                'correct_answer': correct_answer,
                'options': all_answers
            })
        return questions
    except requests.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []  # Return an empty list if there's an error


