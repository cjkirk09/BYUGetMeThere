(function (app) {
	app.controller('menuController', [
		'$scope',
		'infoService',
		function ($scope, infoService) {
			angular.extend($scope, {
				state: {
					menuOpen: false,
					loginOpen: false,
					routeBoxOpen: false
				},
				userInfo: {
					username: "",
					password: "",
					errorMessage: "invalid username/password",
                    currentUser: false
				},
				routeInfo: {
					startPoint: "",
					endPoint: "",
					lastStartPoint: "",
					lastEndPoint: "",
					path: [],
					errorMessage: "ERROR MESSAGE WILL GO HERE"
				},
                buildingInfo: {
                    echo_search: "",
                    current: "",
                    name: "BUILDING NAME",
                    phone: "801-555-1234",
                    hours: "12:00am-12:00pm"
                },
				toggleMenu: function()
				{
					$scope.state.menuOpen = !$scope.state.menuOpen;	
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = false;
				},
				toggleLogin: function()
				{
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = !$scope.state.loginOpen;
					$scope.state.routeBoxOpen = false;
				},
				toggleRouteBox: function()
				{
					//window.alert("in toggle");
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = false;
					$scope.state.routeBoxOpen = !$scope.state.routeBoxOpen;
				},
				register: function()
				{
					// make sure input is valid
                    if ($scope.userInfo.username === "") {
                        $scope.userInfo.errorMessage = "Please enter a valid username";
                    }
                    else if ($scope.userInfo.password === "") {
                        $scope.userInfo.errorMessage = "Please enter a valid password";
                    }
                    else {
                        $scope.userInfo.errorMessage = "";
                        // needs to make call to server
                    }
				},
				login: function()
				{
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
//                            if (success) {
//                                $scope.userInfo.currentUser = true;
//                                // reset username and password (no reason to hang onto them)
//                                $scope.userInfo.username = "";
//                                $scope.userInfo.password = "";
//                            }
                        });	
                    }
				},
				validRoute: function(){
					if( $scope.routeInfo.startPoint == ""){
						$scope.routeInfo.errorMessage = "Please enter a starting point";
					}
					else if ( $scope.routeInfo.endPoint =="" ){
						$scope.routeInfo.errorMessage = "Please enter an ending point";	
					}
					else{
						$scope.routeInfo.errorMessage ="";
					}
					return $scope.routeInfo.errorMessage;
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
						if($scope.routeInfo.startPoint == "ASB" && $scope.routeInfo.endPoint == "JSB"){
							if($scope.routeInfo.lastStartPoint !=$scope.routeInfo.startPoint || 
								$scope.routeInfo.endPoint != $scope.routeInfo.lastEndPoint){
							var stringPath = { startPlace: $scope.routeInfo.startPoint, endPlace: $scope.routeInfo.endPoint };
	
							infoService.getPath(stringPath).then(function(pathInfo){
								if( pathInfo.error){
									$scope.routeInfo.errorMessage= pathInfo.error;							
								}
							   else{
									$scope.routeInfo.errorMessage= "";
									path = [];
									$scope.routeInfo.path[0] = {latitude:pathInfo.startCoord.latitude,
                                                                longitude:pathInfo.startCoord.longitude};
									$scope.routeInfo.path[1] = {latitude:pathInfo.endCoord.latitude,
                                                                longitude: pathInfo.endCoord.longitude};
							   }
							});
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
                    var searchedBuilding = $scope.buildingInfo.current;
                    $scope.buildingInfo.echo_search = searchedBuilding;
                    // get building info from server 
                    infoService.getBuilding(searchedBuilding).then(function(building){
                        $scope.buildingInfo.name = building.name;
                        $scope.buildingInfo.phone = building.phone_number;
                        $scope.buildingInfo.hours = building.hours;   
                    });
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
                        return response.data
                    });
            }
			
		};
	}]);

})(angular.module('ByuGetMeThereApp', []));
