function (app) {
	app.controller('menuController', [
		'$scope',
		'infoService',
		function ($scope, infoService) {
			angular.extend($scope, {
				state: {
					menuOpen: false,
					loginOpen: false,
					routeBoxOpen: false,
					courseDialogOpen: false,
                    minusClicked: false
				},
				userInfo: {
					username: "",
					password: "",
					errorMessage: "",
                    currentUser: false,
                    currentUsername: "",
                    schedules: []
				},
				routeInfo: {
                    boxOpen: false,
					startPoint: "Start",
					endPoint: "End",
					lastStartPoint: "",
					lastEndPoint: "",
					path: [],
					errorMessage: ""
				},

                buildingInfo: {
                    echo_search: "",
                    selected:'Select Building',
                    name: "BUILDING NAME",
                    phone: "801-555-1234",
                    hours: "12:00am-12:00pm"
                },

				buildings: {
					allInfo: [],
					buildingList: []
				},
                
                floorplans: {
	                list: [],
	                currentFloor: 0
	            },

	            // this is where the data is stored from the schedule popup
	            newcourse: {
	            	name: "",
	            	hour: "Hour",
	            	minute: "Minute",
	            	ampm: "AM/PM",
	            	//     Su 		M 	   Tu     W      Th     F      Sa
	            	days: [false, false, false, false, false, false, false],
	            	building_id: "Building",
	            	room: ""
	            },

				time: {
					hoursList: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
					minutesList: [00, 05, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
					ampm: ['am', 'pm'],
                	daysOfWeek: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                	daysAbbrev: ["Su", "M", "Tu", "W", "Th", "F", "Sa"],
					currentDayOfWeek: function(){ return $scope.getDayOfWeek(); }
				},
 
				toggleMenu: function()
				{
					$scope.state.menuOpen = !$scope.state.menuOpen;	
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = false;
					$scope.state.courseDialogOpen = false;
				},
				toggleLogin: function()
				{
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = !$scope.state.loginOpen;
					$scope.state.routeBoxOpen = false;
					$scope.state.courseDialogOpen = false;
				},
				toggleRouteBox: function(obj)
				{
					//window.alert("in toggle");
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = !$scope.state.routeBoxOpen;
					$scope.state.courseDialogOpen = false;
				},
                toggleOkDialog: function()
                {
                    $scope.state.menuOpen = false;
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = false;
					$scope.state.minusClicked = !$scope.state.minusClicked;
                },
				toggleCourseDialog: function()
				{
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = false;
					$scope.state.courseDialogOpen = !$scope.state.courseDialogOpen;
				},

				register: function()
				{
                    if ($scope.userInfo.currentUser) {
                        $scope.userInfo.errorMessage = "Please log out first.";
                        return;
                    }
					// make sure input is valid
                    if ($scope.userInfo.username === "") {
                        $scope.userInfo.errorMessage = "Please enter a valid username";
                    }
                    else if ($scope.userInfo.password === "") {
                        $scope.userInfo.errorMessage = "Please enter a valid password";
                    }
                    else {
                        $scope.userInfo.errorMessage = "";
                        var userString = { username: $scope.userInfo.username, password: $scope.userInfo.password };
                        infoService.createUser(userString).then(function(success) {
                            //$scope.userInfo.errorMessage = success;
                            if (success == "True") {
                                $scope.userInfo.errorMessage = "Welcome " + $scope.userInfo.username;
                                $scope.userInfo.currentUsername = $scope.userInfo.username;
                                $scope.userInfo.currentUser = true;
                                $scope.userInfo.password = "";
                            }
                            else {
                                $scope.userInfo.errorMessage = "Sorry, that username is taken";
                            }
                        });
                        // let the user close the login screen so they can see success/failure
                        // $scope.toggleLogin();
                    }
				},
				login: function()
				{
                    if ($scope.userInfo.currentUser) {
                        $scope.userInfo.errorMessage = "Please log out first.";
                        return;
                    }
                    // username: toor
                    // password: mypassword
					// make sure input is valid
                    if ($scope.userInfo.username === "") {
                        $scope.userInfo.errorMessage = "Please enter a valid username";
                    }
                    else if ($scope.userInfo.password === "") {
                        $scope.userInfo.errorMessage = "Please enter a valid password";
                    }
                    else {
                        $scope.userInfo.errorMessage = "";
                        var userString = { username: $scope.userInfo.username, password: $scope.userInfo.password };
//                        $scope.userInfo.errorMessage = userString;
                        infoService.verifyUser(userString).then(function(success) {
                            $scope.userInfo.errorMessage = success;
                            if (success == "true") {
                                $scope.userInfo.errorMessage = "Welcome " + $scope.userInfo.username;
                                $scope.userInfo.currentUser = true;
                                $scope.userInfo.currentUsername = $scope.userInfo.username;
                                $scope.userInfo.password = "";
                                $scope.userInfo.schedules = $scope.getSavedSchedules();
                            }
                        });	
                        // let the user close the login screen so they can see success/failure
                        // $scope.toggleLogin();
                    }
				},
                logout: function()
                {
                    $scope.userInfo.currentUser = false;
                },
				validRoute: function(){
					var startGood = false;
					var endGood = false;
					for( building in $scope.buildings.buildingList){
						if($scope.buildings.buildingList[building].id == $scope.routeInfo.startPoint){
							startGood = true;
						}
					}
					for( building in $scope.buildings.buildingList){
						if($scope.buildings.buildingList[building].id == $scope.routeInfo.endPoint){
							endGood = true;
						}
					}
					if( $scope.routeInfo.startPoint == "currentLocation" ){
						startGood = true;
					}
					if( !startGood){
						$scope.routeInfo.errorMessage = "Please enter a valid starting point";
					}
					else if ( !endGood ){
						$scope.routeInfo.errorMessage = "Please enter an valid ending point";	
					}
					else{
						$scope.routeInfo.errorMessage ="";
					}
					return startGood && endGood;
				}, 
				getRoute: function()
				{
					//verify that startpoint and endpoint are not empty
					if( $scope.routeInfo.startPoint == ""){
						$scope.routeInfo.errorMessage = "Please enter a starting point";
					}
					else if ( $scope.routeInfo.endPoint =="" ){
						$scope.routeInfo.errorMessage = "Please enter an ending point";	
					}
					else{
						//convert the entered info to the building abbreviations and check that they are valid
						if($scope.validRoute()){
							if($scope.routeInfo.lastStartPoint !=$scope.routeInfo.startPoint || 
								$scope.routeInfo.endPoint != $scope.routeInfo.lastEndPoint){
							
	
							    if( $scope.routeInfo.startPoint == "currentLocation" ){
								    infoService.getCustomPath({endPlace: $scope.routeInfo.endPoint}).then( function(pathInfo){
									  if( pathInfo.error){
									    $scope.routeInfo.errorMessage= pathInfo.error;							
								      }
							          else{
									    $scope.routeInfo.errorMessage= "";

									    $scope.routeInfo.path = [];
									    $scope.routeInfo.path[0] = "currentLocation";
									    $scope.routeInfo.path[1] = {latitude:pathInfo.endCoord.latitude,
                                                                longitude: pathInfo.endCoord.longitude};
                                        $scope.floorplans.list = pathInfo.floorPlans;
                                        $scope.getBuildingInfo();
							          }	
									});
							    }
							    else{
                                  var stringPath = { startPlace: $scope.routeInfo.startPoint, endPlace: $scope.routeInfo.endPoint };
							      infoService.getPath(stringPath).then(function(pathInfo){
								    if( pathInfo.error){
									    $scope.routeInfo.errorMessage= pathInfo.error;							
								    }
							        else{
									    $scope.routeInfo.errorMessage= "";

									    $scope.routeInfo.path = [];
									    $scope.routeInfo.path[0] = {latitude:pathInfo.startCoord.latitude,
                                                                longitude:pathInfo.startCoord.longitude};
									    $scope.routeInfo.path[1] = {latitude:pathInfo.endCoord.latitude,
                                                                longitude: pathInfo.endCoord.longitude};
                                        $scope.floorplans.list = pathInfo.floorPlans;
                                        $scope.getBuildingInfo($scope.routeInfo.endPoint);
							       }
							       });
							    
							   }
							    $scope.routeInfo.lastStartPoint = $scope.routeInfo.startPoint;
							    $scope.routeInfo.lastEndPoint = $scope.routeInfo.endPoint;
						   }
						}
						else{
							$scope.routeInfo.errorMessage = "Please enter valid points";	
						}

					}
					return $scope.routeInfo.errorMessage;
					//$scope.routeInfo.path[0] = {latitude:40.248852, longitude:-111.647374};
					//$scope.routeInfo.path[1] = {latitude:40.245879, longitude:-111.651644};
					//$scope.routeInfo.path[2] = {latitude:40.249329, longitude:-111.650665};
					//$scope.routeInfo.path[3] = {latitude:40.249092, longitude:-111.653519};
					//$scope.routeInfo.errorMessage = "";		
					// $scope.routeInfo.errorMessage = "I couldn't get the route yet";
				},
                getBuildingInfo: function(selected) 
                {
                    $scope.buildingInfo.selected = selected;
                    $scope.buildingInfo.echo_search = selected;
                    // get building info from server 
                    infoService.getBuilding(selected).then(function(building){
                        $scope.buildingInfo.name = building.name;
                        $scope.buildingInfo.phone = building.phone_number;
                        $scope.buildingInfo.hours = building.hours; 
                        if ($scope.buildingInfo.hours == "") {
                            $scope.buildingInfo.hours = "Sorry. Hours for this building are unavailable."
                        }  
                    });
                    
                },
                nextFloor: function () //advance floor plan pic to the next floor
                {
                    $scope.floorplans.currentFloor = ($scope.floorplans.currentFloor+1) % $scope.floorplans.list.length;
                },
                previousFloor: function() // floor plan pic to the previous floor
                {
                    $scope.floorplans.currentFloor = (($scope.floorplans.currentFloor-1) + $scope.floorplans.list.length)
                    % $scope.floorplans.list.length;
                },
                newSchedule: function () // same thing as hitting every minus button
                {
                	$scope.userInfo.schedules = initializeSchedules();
                },
                initializeSchedules: function () // set up the days of the week schedules
                {
                	// empty out the user's schedules array
                	// create 7 new schedules, one for each day of the week
                	// they should be named appropriately and have an empty courses array
                	var schedules = [];
                	for (var i = 0; i < 7; i++)
                	{
                		var newSchedule = {
                			name: $scope.time.daysOfWeek[i],
                			courses: []
                		};
                		schedules.push(newSchedule);
                	}
                	return schedules;
                },
                getSavedSchedules: function () // get user's schedule from server
                {
                	var data = {username: $scope.userInfo.currentUsername};
                	infoService.getSavedSchedules(data).then(function(success) {
                		// save the user's schedule
                		// if the user doesn't have a schedule for a day of the week, add a blank schedule as placeholder
                		if (success.error === "'NoneType' object has no attribute '__getitem__'")
                		{
                			return $scope.initializeSchedules();
                		}
                		else
                		{
                			console.log(success);
                			return success;
                		}
                	});
                },
                addCourse: function () // add a course to the user's schedule(s)
                {
            		// ensure the user filled in all the boxes - 
            		// if even one field is missing OR if they haven't selected any days, 
            		// give an error and don't add the course
            		var allboxesfilled = true;
            		allboxesfilled = allboxesfilled && ($scope.newcourse.name != "");
            		allboxesfilled = allboxesfilled && ($scope.newcourse.hour != "Hour");
            		allboxesfilled = allboxesfilled && ($scope.newcourse.minute != "Minute");
            		allboxesfilled = allboxesfilled && ($scope.newcourse.ampm != "AM/PM");
            		var dayselected = false;
            		for (i in $scope.newcourse.days) dayselected = dayselected || ($scope.newcourse.days[i]==true);
            		allboxesfilled = allboxesfilled && dayselected;
            		allboxesfilled = allboxesfilled && ($scope.newcourse.building_id != "Building");
            		allboxesfilled = allboxesfilled && ($scope.newcourse.room != "");
            		if (!allboxesfilled)
            		{
            			// error - all fields are required!
            			$scope.newcourse.errorMessage = "All fields are required.";
            			console.log("All fields are required to add a course.");
            			return;
            		}

					$scope.newcourse.errorMessage = "";

					// parse the days of the week into a string
					var dayString = "";
					for (i in $scope.newcourse.days) 
						if ($scope.newcourse.days[i] == true) 
							dayString += $scope.time.daysAbbrev[i];

                	// parse the add course popup
                	for (day in $scope.newcourse.days)
                	{
                		// if the user indicated the course is on this day, add it to that day's schedule
                		if ($scope.newcourse.days[day] == true)
                		{
                			var s;
                			// find the schedule for that day
                			for (schedule in $scope.userInfo.schedules)
                			{
                				if ($scope.userInfo.schedules[schedule].name === $scope.time.daysOfWeek[day])
                				{
	                				// add the course to the schedule
	                				$scope.userInfo.schedules[schedule].courses.push({
	                					name: $scope.newcourse.name,
	                					hour: $scope.newcourse.hour,
	                					minute: $scope.newcourse.minute,
	                					ampm: $scope.newcourse.ampm,
	                					days: dayString,
	                					building_id: $scope.newcourse.building_id,
	                					room: $scope.newcourse.room
	                				});
                				}
                			}
                		}
                	}
                },
                saveSchedule: function () // send user-created schedule to server
                {
                	var userName = $scope.userInfo.currentUsername;
                	var courses = [];
                	// get schedule, convert it into data
                	for (day in $scope.time.daysOfWeek)
                	{
	                	data = {
	                		username:userName, 
	                		schedule_name: $scope.time.daysOfWeek[day],
	                		courses: []
	                	};
	                	// send to server
	                	infoService.saveSchedule(data).then(function(success) {
	                		// check for errors
	                	})
                	}
                },
                clearTentativeCourse: function () // clear button in new course
                {
                	$scope.newcourse.name = "";
                	$scope.newcourse.hour = "Hour";
                	$scope.newcourse.minute = "Minute";
                	$scope.newcourse.ampm = "AM/PM";
                	$scope.newcourse.days = [false, false, false, false, false, false, false];
                	$scope.newcourse.building_id = "Building";
                	$scope.newcourse.room = "";
                },
                removeCourse: function () // called when the user pushes the - button
                {
                	$scope.toggleOkDialog(); // close the warning message	
                },
                getDayOfWeek: function() // used for scheduling
                {
                	var day = $scope.time.daysOfWeek[new Date().getDay()];
                	console.log(day);
                	return day;
                }
			});
			infoService.getAllBuildings().then(function(buildingData){
						for ( building in buildingData ){
							var b = { id: buildingData[building].id, name: buildingData[building].name };
							$scope.buildings.allInfo[$scope.buildings.allInfo.length] = buildingData[building];
							$scope.buildings.buildingList[$scope.buildings.buildingList.length] = b;
						}
					});
			$scope.userInfo.schedules = $scope.initializeSchedules();
		}
	]);

	app.factory('infoService',['$http', function($http)
	{
		return {
			getPath: function(stringPath)
			{
				return $http.post('http://104.236.182.126/getPath',stringPath)
					.then(function(response) {
						return response.data;
					});
			},
			getCustomPath: function(endPoint)
			{
				return $http.post('http://104.236.182.126/getCustomPath',endPoint)
					.then(function(response) {
						return response.data;
					});
			},
            getBuilding: function(searchedBuilding)
            {
                return $http.get('http://104.236.182.126/getBuildingInfo/'+searchedBuilding)
                    .then(function(response) {
                        return response.data;    
                    });
            },

            verifyUser: function(userString)
            {
                return $http.post('http://104.236.182.126/login',userString)
                    .then(function(response) {
                        return response.data;
                    });
            },
            createUser: function(userString)
            {
                return $http.post('http://104.236.182.126/register',userString)
                    .then(function(response) {
                        return response.data;
                    });
            },

			getAllBuildings: function()
			{
				return $http.get('http://104.236.182.126/getAllBuildings')
					.then(function(response) {
						return response.data;
					});
			},

			saveSchedule: function(userString)
			{
				return $http.get('http://104.236.182.126/saveSchedule',userString)
					.then(function(response) {
						return response.data;
					});
			},

			getSavedSchedules: function(userString)
			{
				return $http.get('http://104.236.182.126/getSavedSchedules',userString)
					.then(function(response) {
						return response.data;
					});
			}
			
		};
	}]);

})(angular.module('ByuGetMeThereApp', []));

