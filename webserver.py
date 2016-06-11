# example_webserver.py #
########################

import markov
from flask import Flask, request, render_template

import praw

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/submission', methods = ['POST'])
def authorized():
    subreddits = request.form['subreddits']
    subreddit_list = subreddits.split(",")
    title, post = markov.markov_chain(subreddit_list, 10, 50)
    return render_template('submission.html', title=title, post=post)
    # return variables_text + '</br></br>' + text + '</br></br>' + back_link

if __name__ == '__main__':
    
    app.run(debug=True, port=65010)

    