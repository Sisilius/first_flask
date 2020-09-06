from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<string:name>/<int:id>') #Передаём кастоымные значения через адрессную строку
def user(name, id):
    return f'Страница пользователя {name} с id {id}'


if __name__ == '__main__':
    app.run(debug = True)