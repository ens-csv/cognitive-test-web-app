from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        answers = {
            'q1': 'C',
            'q2': 'A',
            'q3': 'B',
            'q4': 'C'
        }

        score = 0
        for question, correct_answer in answers.items():
            if request.form.get(question) == correct_answer:
                score += 1

        return render_template('result.html', score=score, total=len(answers))

    return render_template('test.html')
