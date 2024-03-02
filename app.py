from flask import Flask, render_template, request, url_for, redirect

from question.questions import comment_bp
from user.user import user_bp

app = Flask(__name__)
# Подключаем Blueprint
app.register_blueprint(user_bp)
app.register_blueprint(comment_bp)

app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 't8r7se98gdgsd7gd7sg8sfsg78'

# Простейшая база данных для хранения вопросов и ответов
questions = [
    {'id': 1, 'title': 'Как использовать Flask', 'content': 'Я не знаю как использовать Flask(('},
    {'id': 2, 'title': 'Как использовать Django', 'content': 'Я не знаю как использовать Django(('}
]

answers = [
    {'id': 1, 'question_id': 1, 'answer': 'Просто скачайте Flask через команду'},
    {'id': 2, 'question_id': 2, 'answer': 'Просто скачайте Django через команду'}
]


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html', questions=questions)


# Страница с деталями вопросов и ответов
@app.route('/question/<int:question_id>')
def question(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        question_answers = [a for a in answers if a['question_id'] == question_id]
        return render_template('question.html', question=question, question_answers=question_answers)
    else:
        return 'Вопрос не найден'


# Страница для добавления нового вопроса
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_content = {
            'id': len(questions) + 1,
            'title': title,
            'content': content
        }
        questions.append(new_content)
        return redirect(url_for('hello_world'))
    else:
        return render_template('ask.html')


app.run(debug=True)
