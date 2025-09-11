from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, nullable=False, unique=True)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


@app.route('/')
def index_view():
    opinion = Opinion.query.order_by(func.random()).first()
    if opinion is None:
        return 'В базе данных мнений о фильмах нет.'
    return opinion.text


if __name__ == '__main__':
    app.run(debug=True)
