def processFileList(fileList):
	for file in fileList:
		removeDuplicates("data/" + file)
		sortFile("data/" + file)


def sortFile(fileName):
	print("Sorting " + fileName)
	try:
		lines = []
		with open(fileName, "r") as file:
			fullLine = ""
			for line in file:
				fullLine += line
				if "|-|" in line[-8:]:  # if end of comment
					lines.append(fullLine)
					fullLine = ""

		lines.sort()

		with open(fileName, "w") as file:
			for line in lines:
				file.write(line)
	except FileNotFoundError:
		pass


def removeDuplicates(fileName):
	try:
		lines = []
		with open(fileName, "r") as file:
			fullLine = ""
			for line in file:
				fullLine += line
				if "|-|" in line[-8:]:  # if end of comment
					lines.append(fullLine)
					fullLine = ""

		lines = list(set(lines))

		with open(fileName, "w") as file:
			for line in lines:
				file.write(line)

	except FileNotFoundError:
		pass
