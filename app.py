from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'

all_posts = [
    {
        'title': 'Post 1',
        'content': 'Content of post 1',
        'author': 'cosmus'
    },
    {
        'title': 'Post 2',
        'content': 'Content of post 2'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home')
def hello():
    return "Hello world!"

@app.route('/onlyget', methods=['GET'])
def get_req():
    return "You can only GET this this webpage."

if __name__ == "__main__":
    app.run(debug=True)