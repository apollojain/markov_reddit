# example_webserver.py #
########################

import markov
from flask import Flask, request, render_template

import praw

app = Flask(__name__)

CLIENT_ID = 'ff8BUH8JGCcN0Q'
CLIENT_SECRET = 'QmNmgGIDR4De5mqcNn0UMROGobA'
REDIRECT_URI = 'http://127.0.0.1:65010/authorize_callback'

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/submission', methods = ['POST'])
def authorized():
    subreddits = request.form['subreddits']
    subreddit_list = subreddits.split(",")
    title, post = markov.markov_chain(r, subreddit_list, 10, 50)
    return render_template('submission.html', title=title, post=post)
    # return variables_text + '</br></br>' + text + '</br></br>' + back_link

if __name__ == '__main__':
    r = praw.Reddit('OAuth Webserver example by u/_Daimon_ ver 0.1. See '
                    'https://praw.readthedocs.org/en/latest/'
                    'pages/oauth.html for more info.')
    r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
    app.run(debug=True, port=65010)

    