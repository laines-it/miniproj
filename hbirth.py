# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'gothic_secret_666'

# Правильный код доступа
CORRECT_CODE = "513"

# Данные для теста
TEST_QUESTIONS = [
    {
        "id": 1,
        "question": "Лия это",
        "image": "",
        "options": [
            {"text": "Leah", "correct": True},
            {"text": "Lia", "correct": False}
        ],
        "commentTrue": "Свага",
        "commentFalse": "Мало сваги"
    },
    {
        "id": 2,
        "question": "Что сделать?",
        "image": "child.svg",
        "options": [
            {"text": "Погладить", "correct": False},
            {"text": "Уебать со всей силы", "correct": True}
        ],
        "commentTrue": "Правильно!",
        "commentFalse": "Только если ногой"
    },
    {
        "id": 3,
        "question": "venom",
        "image": "",
        "options": [
            {"text": "venom", "correct": True}
        ],
        "commentTrue": "venom"
    },
    {
        "id": 4,
        "question": "Лучший репер России",
        "image": "",
        "options": [
            {"text": "Оксимирон", "correct": True},
            {"text": "Очередной хуесос", "correct": True}
        ],
        "commentTrue": "если что, оба ответа правильные"
    },
    {
        "id": 5,
        "question": "Как купить лсд?",
        "image": "",
        "options": [
            {"text": "Отсосать", "correct": True},
            {"text": "За деньги", "correct": False}
        ],
        "commentTrue": "Конечно, это же бесплатно",
        "commentFalse": "Слыш, это противозаконно! А главное, затратно!"
    },
    {
        "id": 6,
        "question": "Это круто?",
        "image": "mcr.jpg",
        "options": [
            {"text": "Да", "correct": True},
            {"text": "Нет", "correct": False}
        ],
        "commentTrue": "ДАДАДАДДА!",
        "commentFalse": "Охуел?"
    },
    {
        "id": 7,
        "question": "[Смешная шутка]",
        "image": "",
        "options": [
            {"text": "АЭАХАХАЭАЭАЭ", "correct": True},
            {"text": "ААХАХАХХАХХА", "correct": False}
        ],
        "commentTrue": "база",
        "commentFalse": "слабо"
    },
    {
        "id": 8,
        "question": "Лучший монстр",
        "image": "",
        "options": [
            {"text": "Белый", "correct": True},
            {"text": "Черный", "correct": False}
        ],
        "commentTrue": "Очевидно, черный хуже",
        "commentFalse": "Очевидно, белый лучше"
    },
    {
        "id": 9,
        "question": "Лучший Monster Energy",
        "image": "",
        "options": [
            {"text": "Monster Ultra White", "correct": True},
            {"text": "Monster Original", "correct": False}
        ],
        "commentTrue": "Очевидно, черный хуже",
        "commentFalse": "Очевидно, белый лучше"
    },
    {
        "id": 10,
        "question": "Сколько стоит пакет в Ашане?",
        "image": "",
        "options": [
            {"text": "10 рублей", "correct": False},
            {"text": "Дорого", "correct": True}
        ],
        "commentTrue": "Я честно, хуй его знает",
        "commentFalse": "Я честно, хуй его знает"
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    
    if request.method == 'POST':
        entered_code = request.form.get('code')
        
        if entered_code == CORRECT_CODE:
            session['authenticated'] = True
            return redirect(url_for('sanctuary'))
        else:
            error = "Проебалась!"
    
    return render_template('index.html', error=error)

@app.route('/sanctuary')
def sanctuary():
    if not session.get('authenticated'):
        return redirect(url_for('index'))
    return render_template('sanctuary.html')

@app.route('/test')
def test():
    if not session.get('authenticated'):
        return redirect(url_for('index'))
    return render_template('test.html', questions=TEST_QUESTIONS)

@app.route('/leave')
def leave():
    session.pop('authenticated', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)