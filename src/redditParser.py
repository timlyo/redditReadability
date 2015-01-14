import praw
import sys

from reference import Reference


class RedditParser:
	def __init__(self, subredditNames):
		self.redditAPI = praw.Reddit(Reference.userAgent)
		self.subRedditNames = subredditNames
		self.comments = []

		self.parse()
		for item in self.comments:
			print(item)

	def parse(self):
		for name in self.subRedditNames:
			with open("data/" + name, 'a') as file:
				print(name)
				""":type : praw.objects.Subreddit"""
				subreddit = self.redditAPI.get_subreddit(name)

				submissions = subreddit.get_top_from_day()
				commentNum = 0
				for submission in submissions:
					assert isinstance(submission, praw.objects.Submission)
					sys.stdout.write("replacing moreComment items\r")
					submission.replace_more_comments(limit=16, threshold=10)
					for comment in submission.comments:
						assert isinstance(comment, praw.objects.Comment), type(comment)
						if abs(comment.score) < 3:
							continue
						commentNum += 1
						sys.stdout.write(" " + str(commentNum) + "\r")
						file.write("{0} || {1} || {2} \n".format(comment.id, comment.score, comment.body))

			print()


		# comments = self.redditAPI.get_comments("all")
		# for comment in comments:
		# 	assert isinstance(comment, praw.objects.Comment)
		# 	print(comment.id + " " + str(comment.score) + " " + comment.body)
		# 	# print("submission:", comment.submission)
