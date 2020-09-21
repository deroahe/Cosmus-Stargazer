from flask import Flask, render_template, request, redirect
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default="N/A")
    date_posted = db.Column(db.String(100), nullable=False, default=datetime.datetime.now().strftime("%c"))

    def __repr__(self):
        return 'Blog post ' + str(self.id)