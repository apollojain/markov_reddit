import config, itertools

user_agent = ("PyEng Bot 0.1")
r = config.r
def actual_post(string):
	print(string)
	return_string = string.split('::')[1]
	return return_string 

def consume_by_subreddit(subreddit, n=50):
	submissions = r.get_subreddit(subreddit).get_hot(limit=n)
	submissions_array = [actual_post(str(x)) for x in submissions]
	return submissions_array

def consume_by_subreddits(subreddits, n=50):
	return_array = [consume_by_subreddit(subreddit, n) for subreddit in subreddits]
	return_array = list(itertools.chain.from_terable(return_array))
	return return_array


