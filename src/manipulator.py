class Manipulator:
	"""Class for data transformations/manipulations
		"""

	@staticmethod
	def fileSorter(fileName):
		lines = []
		with open(fileName, "r") as file:
			for line in file:
				lines.append(line)

		lines.sort()

		with open(fileName, "w") as file:
			for line in lines:
				file.write(line)
