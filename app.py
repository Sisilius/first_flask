from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return 'Привет, мир!'

@app.route('/about')
def about():
    return 'Страница "О нас"'

if __name__ == '__main__':
    app.run(debug = True)