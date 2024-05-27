from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class People(db.Model):
    __tablename__ = 'people'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)
    
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

@app.route("/")
def hello_world():
    try:
        new_person = People(first_name='Batman', last_name='Robin')
        db.session.add(new_person)
        db.session.commit()
        people = People.query.all()
        return render_template('index.html', users=people)
        #return jsonify(hello='User Added')
    except Exception as e:
        return jsonify(error=str(e))

@app.route("/people/")
def get_all():
    try:
        persons={}
        people = People.query.all()
        for person in people:
            persons[person.id]={'first_name': person.first_name, 'last_name': person.last_name}
        return jsonify(hello=persons)
    except Exception as e:
        return jsonify(hello=str(e))