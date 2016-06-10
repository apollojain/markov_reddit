import config, itertools

def actual_post(string):
	print(string)
	return_string = string.split('::')[1]
	return return_string 

def combine_arrays(twod_array, i):
	return reduce(lambda x, y: x + [y[i]], twod_array)

def consume_by_subreddit(r, subreddit, n=50):
	submissions = r.get_subreddit(subreddit).get_hot(limit=n)
	titles = [submission.title.encode("utf-8") for submission in submissions]
	submissions = r.get_subreddit(subreddit).get_hot(limit=n)
	posts = [str(submission.selftext.encode("utf-8")) for submission in submissions]
	return [titles, posts]

def consume_by_subreddits(r, subreddits, n=50):
	if len(subreddits) == 1:
		return consume_by_subreddit(r, subreddits[0], n)
	initial_submissions = [consume_by_subreddit(subreddit, n) for subreddit in subreddits]
	titles = combine_arrays(initial_submissions, 0)
	submissions = combine_arrays(initial_submissions, 1)
	return_array = [titles, submissions]
	return return_array

if __name__ == '__main__':
	print consume_by_subreddits(['The_Donald'])