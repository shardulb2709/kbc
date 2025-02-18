from flask import Flask, render_template, request, session, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # change this to a secure secret key

# Define our quiz questions
questions = [
    {
        "question": "What is the capital of Italy?",
        "options": ["Milan", "Pisa", "Torino", "Rome"],
        "answer": "Rome",
        "prize": 100
    },
    {
        "question": "Which country has highest GDP?",
        "options": ["USA", "Germany", "China", "India"],
        "answer": "USA",
        "prize": 200
    },
    {
        "question": "Who is the captain of Indian cricket team in 2024?",
        "options": ["Rohit", "Dhoni", "Kohli", "Bumrah"],
        "answer": "Rohit",
        "prize": 500
    },
    {
        "question": "Who is the PM of India?",
        "options": ["Modi", "Rahul", "Kejriwal", "Amit"],
        "answer": "Modi",
        "prize": 1000
    }
]

@app.route('/')
def index():
    # Initialize session variables
    session['current'] = 0
    session['total'] = 0
    return render_template('quiz.html', question=questions[0])

@app.route('/quiz', methods=['POST'])
def quiz():
    current = session.get('current', 0)
    total = session.get('total', 0)
    user_answer = request.form.get('answer')

    # Check the answer for the current question
    if user_answer == questions[current]['answer']:
        flash(f"Correct! You won ${questions[current]['prize']}.", "success")
        total += questions[current]['prize']
    else:
        flash("Sorry! That's the wrong answer.", "danger")
        return render_template('result.html', total=total)

    # Move to the next question
    current += 1
    session['current'] = current
    session['total'] = total

    if current < len(questions):
        return render_template('quiz.html', question=questions[current])
    else:
        flash("Congratulations! You have completed the quiz.", "info")
        return render_template('result.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
