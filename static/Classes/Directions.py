
class Directions:
	def __init__(self):
		self.googleJson = ""
		self.buildingInfo = ""

	def loadAll(self, google, info):
		self.googleJson = google
		self.buildingInfo = info
