from flask import *
from flask import Flask
from flask import request
from flask import send_from_directory

import json

import sys
sys.path.insert(0, '/var/www/BYUGetMeThereExperimental/BYUGetMeThere/static/Classes/')

from parser import Parser

app = Flask(__name__)


@app.route("/getCount")
def getCount():
	f = open('/var/www/BYUGetMeThereExperimental/BYUGetMeThere/static/count.txt','r')
	return str(f.read())

@app.route("/favicon.ico")
def favIcon():
	return send_from_directory("/var/www/BYUGetMeThereExperimental/BYUGetMeThere/static","favicon.ico")

@app.route("/")
def index():
	g = open('/var/www/BYUGetMeThereExperimental/BYUGetMeThere/static/count.txt','r')
	count = g.read()
	count1 = int(count)
	g.close()
	g = open('/var/www/BYUGetMeThereExperimental/BYUGetMeThere/static/count.txt','w')
	g.write(str(count1+1))
	g.close()
	return send_from_directory("/var/www/BYUGetMeThereExperimental/BYUGetMeThere/static","index.html")
@app.route("/static/<path:thePath>")
def getFiles(thePath):
	return send_from_directory('/static/',thePath)
@app.route("/getPath", methods=['GET','POST'])
def getPath():
	myParser = Parser()
	#return request
	return myParser.getPathJSON(request.get_json())

@app.route("/getCustomPath", methods=['GET','POST'])
def getCustomPath():
	myParser = Parser()
	return myParser.getCustomPathJSON(request.get_json())

@app.route("/getSavedSchedules",  methods=['GET','POST'])
def getSavedSchedules():
	myParser = Parser()
	return myParser.getSavedSchedulesJSON(request.get_json())
@app.route("/getBuildingInfo/<input>")
def getBuildingInfo(input):
	myParser = Parser()
	return myParser.getBuildingInfo(input)
@app.route("/initialize")
def initialize():
	# same as "/" route. initial page seen by user
	return "init"
@app.route("/register",methods=['GET','POST'])
def register():
	myParser = Parser()
	return myParser.createUser(request.get_json())
@app.route("/login",methods=['GET','POST'])
def login():
	# username: "username"
	# password: "password"
	# returns successful or not
	myParser = Parser()
	return myParser.verifyUser(request.get_json())
@app.route("/getMapKey")
def getMapKey():
	#returns mapKey: "key"
	return "map key"
@app.route("/saveSchedule",  methods=['GET','POST'])
def saveSchedule():
	myParser = Parser()
	return myParser.saveSchedule(request.get_json())
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
@app.route("/getAllBuildings")
def getAllBuildings():
	myParser = Parser()
	return myParser.getAllBuildings()
@app.route("/getDirections", methods=['GET','POST'])
def getDirections():
	myParser = Parser()
	return myParser.getDirections(request.get_json(), app.config["API_KEY"])

@app.route("/test")
def getTest():
	return 	"test"

	
if __name__ == "__main__":
	app.run()
