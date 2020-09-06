from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask (__name__)
# Вся байда с БД
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# Поехали таблицы
class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    intro = db.Column(db.String(200), nullable = False)
    text = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default = datetime.utcnow)
# типа возвращает объект и его id
    def __repr__(self):
        return '<Article %r>' %self.id


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create_article', methods = ['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:
            return "Ошибка при добавлении"
    else:
        return render_template('create_article.html')


@app.route('/user/<string:name>/<int:id>') #Передаём кастоымные значения через адрессную строку
def user(name, id):
    return f'Страница пользователя {name} с id {id}'


if __name__ == '__main__':
    app.run(debug = True)