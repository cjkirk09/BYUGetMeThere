(function(app)
{
	app.controller('menuController', [
		'$scope',
		'infoService',
		function($scope)
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
					//infoService.getPath()
					$scope.routeInfo.errorMessage = "I couldn't get the route yet";
				}

			});
		}
	]);

	app.factory('infoService',['$http', function($http)
	{
		return {
			getPath: function()
			{
				return $http.get('http://localhost:3000/posts')
					.then(function(response) {
						return response.data;
					});
			},
			savePost: function(post)
			{
				return $http.put('http://localhost:3000/posts/' + post.id, post);
			},
			deletePost: function(post)
			{
				return $http.delete('http://localhost:3000/posts/' + post.id);
			}
		};
	}]);

})(angular.module('ByuGetMeThereApp', []));
