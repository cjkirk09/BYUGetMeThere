
class Directions:
	def __init__(self, google, building):
		self.googleJson = google
		self.buildingInfo = building

	def loadAll(self, google, info):
		self.googleJson = google
		self.buildingInfo = info
