# ქვემოთ ჩამოთვლილი ბრძანებების გაშვებით დააინსტალირეთ flask  და Flask-SQLAlchemy მოდულები.
# დაინსტალირების შემდეგ დააკომენტარეთ აღნიშნული ბრძანებები, ხოლო დანარჩენი ბრძანებები გააქტიურეთ
import os

#os.system("pip install flask")
#os.system("pip install Flask-SQLAlchemy")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorials.sqlite'
db = SQLAlchemy(app)


# add your code here
# =========
class Oscar(db.Model):
    __tablename__ = "Oscar"
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    age = db.Column(db.Integer)
    name = db.Column(db.String)
    gender = db.Column(db.CHAR)
    movie = db.Column(db.String)

    def __init__(self, year, age, name, gender, movie):
        self.year = year
        self.age = age
        self.name = name
        self.gender = gender
        self.movie = movie

    def __str__(self):
        return f"({self.id}) Weli: {self.year} | Asaki: {self.age} | Name: {self.name} | Sqesi: {self.gender} | Filmi: {self.movie}"


# ==========

@app.route('/')
def hello_world():
    with app.app_context():
        oscar_f = Oscar.query.first()
        print(oscar_f.movie)
    return 'Hello World!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        oscar = Oscar(year=2023, age=19, name="Data Tchanukvadze", gender='M', movie="Intersellar")
        db.session.add(oscar)
        db.session.commit()
    app.run()
