from flask import *
from flask import Flask
from flask import request
from flask import send_from_directory

import json

import sys
sys.path.insert(0, '/var/www/BYUGetMeThereTest/BYUGetMeThere/static/Classes/')

from parser import Parser

app = Flask(__name__)

@app.route("/")
def index():
	return send_from_directory("/var/www/BYUGetMeThereTest/BYUGetMeThere/static","index.html")
@app.route("/static/<path:thePath>")
def getFiles(thePath):
	return send_from_directory('/static/',thePath)
@app.route("/getPath", methods=['GET','POST'])
def getPath():
	myParser = Parser()
	#return request
	return myParser.getPathJSON(request.get_json())

@app.route("/getCustomPath")
def getCustomPath():
	myParser = Parser()
	return myParser.getCustomPathJSON(request.get_json())

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
@app.route("/getBuildingInfo/<input>")
def getBuildingInfo(input):
	myParser = Parser()
	return myParser.getBuildingInfo(input)
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
	myParser = Parser()
	return myParser.loginJSON(request.get_json())
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
	#return "This is your user name: " + str(input)
	mydb = DB()
	return mydb.getBuildings()	
	
if __name__ == "__main__":
	app.run()
