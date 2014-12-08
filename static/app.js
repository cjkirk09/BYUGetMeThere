(function(app)
{
	app.controller('menuController', [
		'$scope',
		'infoService',
		function($scope, infoService)
		{
			angular.extend($scope, {
				state: {
					menuOpen: false,
					loginOpen: false,
					routeBoxOpen: false
				},
				userInfo: {
					username: "",
					password: "", 
					errorMessage: "invalid username/password"
				},
				routeInfo: {
					startPoint: "",
					endPoint: "",
					path: [], 
					errorMessage: "ERROR MESSAGE WILL GO HERE"
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
					$scope.userInfo.errorMessage = "clicked Register";
				},
				login: function()
				{
					$scope.userInfo.errorMessage = "clicked Login";					
				},
				getRoute: function()
				{
					//verify that startpoint and endpoint are not empty
					if( $scope.routeInfo.startPoint == ""){
						$scope.routeInfo.errorMessage = "Please enter a starting point";
					}
					else if ( $scope.routeInfo.endPoint =="" ){
						$scope.routeInfo.errorMessage = "Please enter a ending point";	
					}
					else{
						//convert the entered info to the building abbreviations
						var stringPath = { startPlace: $scope.routeInfo.startPoint, endPlace: $scope.routeInfo.endPoint };
						infoService.getPath(stringPath).then(function(pathInfo){
							$scope.routeInfo.errorMessage= " " + pathInfo.error;
							path = [];
							path[0] = pathInfo.startCoord;
							path[1] = pathInfo.endCoord;
						});
					}
					
					//$scope.routeInfo.path[0] = {latitude:40.248852, longitude:-111.647374};
					//$scope.routeInfo.path[1] = {latitude:40.245879, longitude:-111.651644};
					//$scope.routeInfo.path[2] = {latitude:40.249329, longitude:-111.650665};
					//$scope.routeInfo.path[3] = {latitude:40.249092, longitude:-111.653519};
					//$scope.routeInfo.errorMessage = "";		
					// $scope.routeInfo.errorMessage = "I couldn't get the route yet";
				}

			});
		}
	]);

	app.factory('infoService',['$http', function($http)
	{
		return {
			getPath: function(stringPath)
			{
				return $http.get('http://104.236.182.126/getPath', stringPath)
					.then(function(response) {
						return response.data;
					});
			}
			
		};
	}]);

})(angular.module('ByuGetMeThereApp', []));
