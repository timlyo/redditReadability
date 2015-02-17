from redditParser import RedditParser

from datetime import datetime as DateTime
from manipulator import *
from ranking import *
from src.ranking import analyseFile, compileToFile

mostSubscribed = [
	"funny", "pics", "askreddit", "todayilearned", "worldnews", "science", "iama", "blog", "videos", "gaming"]

defaults = [
	"announcements", "art", "askreddit", "askscience", "aww", "blog", "books", "creepy", "dataisbeautiful", "diy",
	"documentaries", "earthporn", "explainlikeimfive", "fitness", "food", "funny", "futurology", "gadgets", "gaming",
	"getmotivated", "gifs", "history", "iama", "internetisbeautiful", "jokes", "lifeprotips", "listentothis",
	"mildlyinteresting", "movies", "music", "news", "nosleep", "nottheonion", "oldschoolcool", "personalfinance",
	"philosophy", "photoshopbattles", "pics", "science", "showerthoughts", "space", "sports", "television", "tifu",
	"todayilearned", "twoxchromosomes", "upliftingnews", "videos", "worldnews", "writingprompts"]

others = [
	"writinghub", "writing"]


def main():
	startTime = DateTime.now()
	subredditList = list(set(mostSubscribed + defaults + others))  # remove dupes

	print()
	print("started at " + str(startTime))
	print("Analysing the top ", len(mostSubscribed), " subreddits")
	print("Analysing ", len(defaults), " defaults")
	print("Analysing ", len(others), " others")
	print("Analysing ", len(subredditList), " total")
	print()

	# redditParser = RedditParser(subredditList)
	#
	# processFileList(subredditList)

	for subreddit in subredditList:
		analyseFile("data/" + subreddit)

	for subreddit in subredditList:
		compileToFile(subredditList)

	print("Finished, took " + str(DateTime.now() - startTime))

if __name__ == "__main__":
	main()
