from flask import Flask
from flask import request
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
	return send_from_directory("/var/www/BYUGetMeThereTest/AppFolder/static","index.html")
@app.route("/static/<path:thePath>")
def getFiles(thePath):
	return send_from_directory('/static/',thePath)
@app.route("/getPath", methods=['GET','POST'])
def getPath():
	#JSON gets startPlace: "string", endPlace: "string"
	#returns 
	#  startCoord: [ lattitude, longitude ],
	#  endCoord: [ lattitude, longitude ],
	#  floorPlan: "url",
	#  buildingInfo:
	if request.method == 'GET':
		return "getPath"
	if request.method == 'POST':
		myJson = request.get_json()
		return str(myJson['myusername'])
	else:
		return 'error'
@app.route("/getCustomPath")
def getCustomPath():
	#JSON startCood: [lat,long], endplace: "string"
	#returns 
	#  startCoord: [ lattitude, longitude ],
	#  endCoord: [ lattitude, longitude ],
	#  floorPlan: "url",
	#  buildingInfo:
	return "CustomPath"
@app.route("/getSavedPaths")
def getSavedPaths():
	#  username:"username",
	#  password:"password"
	#Assuming we need to return the paths? JSON set up?
	return "SavedPaths"
@app.route("/loadPath")
def loadPath():
	#  username:"username",
	#  password:"password",
	#  pathid: "path" //or path points/ locations
	#  returns
	#  startCoord: [ lattitude, longitude ],
	#  endCoord: [ lattitude, longitude ],
	#  floorPlan: "url",
	#  buildingInfo:
	return "loadPath"
@app.route("/loadTour")
def loadTour():
	#  tourname: "name"
	# returns
	#  path: [ [lat,long], [lat,long],,, ],
	#  places: [ place:{ coord:[lat,long], name:"string", info:"string", image:"url"(optional) }, , ]
	return "load tour"
@app.route("/savePath")
def savePath():
	#  username: "username", //some way to know which user it is
	#  coordinates: [,,]
	# returns t/f on if successful or not
	return "savePath"
@app.route("/getBuildingInfo")
def getBuildingInfo():
	# ??? up in the air if this is even needed
	return "building info"
@app.route("/initialize")
def initialize():
	# same as "/" route. initial page seen by user
	return "init"
@app.route("/regester")
def regester():
	# username: "username"
	# password: "password"
	# checks to see if user name already taken
	# then logs in
	# returns successful or not 
	return "regester"
@app.route("/login")
def login():
	# username: "username"
	# password: "password"
	# returns successful or not
	return "login"
@app.route("/getMapKey")
def getMapKey():
	#returns mapKey: "key"
	return "map key"
@app.route("/saveSchedule")
def saveSchedule():
	# username: "username"
	# password: "password"
	# classes: [,,] json of class goes inbetween ','
	# returns successful or not
	return "save my schedule"
@app.route("/mapSchedule")
def mapSchedule():
	# username: "username"
	# password: "password"
	# what day to show MWFTTh ect.
	# returns
	#  no saved schedule/other failure message
	#  path of schedule (similar to load path)
	return "map my schedule"
@app.route("/user/<input>")
def user(input):
	return "This is your user name: " + str(input)

if __name__ == "__main__":
	app.run()
