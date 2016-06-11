import re, random, consume

def markov_dictionary(str_array):
	dictionary = {}
	for string in str_array: 
		print string
		string = " .".join(string.split("."))
		word_array = re.split("\s+", string)
		for i in range(1, len(word_array)):
			key = word_array[i - 1]
			value =  word_array[i]
			if key not in dictionary: 
				dictionary[key] = []
			dictionary[key].append(value)
	return dictionary 


def construct_chain(dictionary, length):
	def start_char():
		if '.' in dictionary: 
			return '.'
		else: 
			return random.choice(dictionary.keys())
	cur = start_char()
	text = ''
	for i in range(length):

		cur = random.choice(dictionary[cur])
		text += cur + ' '
		if cur not in dictionary: 
			cur = start_char()

	if '.' in dictionary: 
		while cur != '.': 
			cur = random.choice(dictionary[cur])
			text += cur + ' '
			if cur not in dictionary: 
				cur = start_char()

	text = re.sub('^[a-zA-Z0-9,.!? ]*$', '', text)
	text = text.replace(" .", ".")
	return text 

def markov_chain(r, subreddits, title_length, submission_length):
	titles, submissions = consume.consume_by_subreddits(r, subreddits)
	title_dictionary = markov_dictionary(titles)
	submission_dictionary = markov_dictionary(submissions)
	title_text = construct_chain(title_dictionary, title_length)
	submission_text = construct_chain(submission_dictionary, submission_length)
	return_pair = [title_text, submission_text]
	return return_pair

if __name__ == '__main__':
	print markov_chain(["The_Donald"], 10, 50)
