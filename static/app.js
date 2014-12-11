(function (app) {
	app.controller('menuController', [
		'$scope',
		'infoService',
		function ($scope, infoService) {
			angular.extend($scope, {
				state: {
					menuOpen: false,
					loginOpen: false,
					routeBoxOpen: false,
					newScheduleItemOpen: false
				},
				userInfo: {
					username: "",
					password: "",
					errorMessage: "",
                    currentUser: false,
                    currentUsername: ""
				},
				routeInfo: {
                    boxOpen: false,
					startPoint: "",
					endPoint: "",
					lastStartPoint: "",
					lastEndPoint: "",
					path: [],
					errorMessage: ""
				},

                buildingInfo: {
                    echo_search: "",
                    selected: "",
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

	            scheduleItem: {
	            	name: "",
	            	hour: "",
	            	minute: "",
	            	ampm: "",
	            	days: [false, false, false, false, false, false, false],
	            	building_id: "",
	            	room: ""
	            },

                 schedule: {
                 	list: [],
                 	hoursList: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
                 	minutesList: ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55'],
                 	ampm: ['am', 'pm']
                 },
 
				toggleMenu: function()
				{
					$scope.state.menuOpen = !$scope.state.menuOpen;	
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = false;
					$scope.state.newScheduleItemOpen = false;
				},
				toggleLogin: function()
				{
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = !$scope.state.loginOpen;
					$scope.state.routeBoxOpen = false;
					$scope.state.newScheduleItemOpen = false;
				},
				toggleRouteBox: function(obj)
				{
					//window.alert("in toggle");
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = !$scope.state.routeBoxOpen;
					$scope.state.newScheduleItemOpen = false;
				},
				toggleNewScheduleItem: function()
				{
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = false;
					$scope.state.newScheduleItemOpen = !$scope.state.newScheduleItemOpen;
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
                        // set selected building so the building info button will work right
                        $scope.buildingInfo.selected = $scope.routeInfo.endPoint;

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
                                        $scope.getBuildingInfo();
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
                getBuildingInfo: function() 
                {
                    var searchedBuilding = $scope.buildingInfo.selected;
                    $scope.buildingInfo.echo_search = searchedBuilding;
                    // get building info from server 
                    infoService.getBuilding(searchedBuilding).then(function(building){
                        $scope.buildingInfo.name = building.name;
                        $scope.buildingInfo.phone = building.phone_number;
                        $scope.buildingInfo.hours = building.hours;   
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
                	// get all divs of id='scheduleItem'
                	// remove them from DOM
                },
                getSavedSchedules: function () // get user's schedule from server
                {
                	var username = $scope.userInfo.currentUsername;
                	infoService.loadSchedule(username).then(function(success) {
                		// save the user's schedule
                	});
                },
                saveSchedule: function () // send user-created schedule to server
                {
                	var userName = $scope.userInfo.currentUsername;
                	var daysOfWeek = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"};
                	// get schedule, convert it into data
                	for (day in daysOfWeek)
                	{
	                	data = {
	                		username:userName, 
	                		schedule_name:daysOfWeek[day],
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
                	$scope.scheduleItem.name = "";
                	$scope.scheduleItem.hour = "";
                	$scope.scheduleItem.minute = "";
                	$scope.scheduleItem.ampm = "";
                	$scope.scheduleItem.days = [false, false, false, false, false, false, false];
                	$scope.scheduleItem.building_id = "";
                	$scope.scheduleItem.room = "";
                },
                removeScheduleItem: function () // called when the user pushes the - button
                {
                	
                }
            
					
				

			});
			infoService.getAllBuildings().then(function(buildingData){
						for ( building in buildingData ){
							var b = { id: buildingData[building].id, name: buildingData[building].name };
							$scope.buildings.allInfo[$scope.buildings.allInfo.length] = buildingData[building];
							$scope.buildings.buildingList[$scope.buildings.buildingList.length] = b;
						}
					});
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
