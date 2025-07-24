# app.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_987!'

# Правильный код доступа
CORRECT_CODE = "0726"

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    
    if request.method == 'POST':
        entered_code = request.form.get('code')
        
        if entered_code == CORRECT_CODE:
            session['authenticated'] = True
            return redirect(url_for('welcome'))
        else:
            error = "Неверный код. Попробуйте ещё раз."
    
    return render_template('index.html', error=error)

@app.route('/welcome')
def welcome():
    if not session.get('authenticated'):
        return redirect(url_for('index'))
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.pop('authenticated', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)