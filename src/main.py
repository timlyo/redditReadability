from redditParser import RedditParser
from manipulator import Manipulator

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
	print("Analysing the top ", len(mostSubscribed), " subreddits")
	print("Analysing ", len(defaults), " defaults")
	print("Analysing ", len(others), " others")
	print("Analysing ", len(mostSubscribed) + len(defaults) + len(others), " total")

	#redditParser = RedditParser(mostSubscribed + defaults + others)

	Manipulator.fileSorter("data/funny")

# for subReddit in :  # print(redditParser.getComments(subReddit))


if __name__ == "__main__":
	main()
