import countsyl


def analyseFile(fileName):
	lines = []
	readabilityMaxima = [0, 0]
	scoreMaxima = [0, 0]

	with open(fileName, "r") as file:
		fullLine = ""
		for line in file:
			fullLine += line
			if "|-|" in line[-8:]:  # if end of comment
				lines.append(fullLine)
				fullLine = ""

	with open(fileName + "-readability", "w") as file:
		file.write('["Score", "Readability"],\n')
		for line in lines:
			score = int(line.replace("|-|", "").split("||")[1])
			comment = line.replace("|-|", "").split("||")[2]
			readability = getReadability(comment)
			if readability < -10:
				continue
			file.write("[" + str(score) + "," + "%0.2f" % readability + "],\n")


def getReadability(comment):
	# Flesch kincaid http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
	totalWords = len(comment.split(" "))
	totalSentences = len(comment.split("."))

	totalsyllables = 0
	for word in comment.split(" "):
		totalsyllables += countsyl.count_syllables(word)[1]  # TODO test whether to use max or min syllables

	return 206.835 - 1.015*(totalWords/totalSentences) - 84.6*(totalsyllables/totalWords)
