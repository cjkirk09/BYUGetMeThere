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
					loginOpen: false
				},
				userInfo: {
					username: null,
					password: null,
					errorMessage: null
				},
				toggleMenu: function()
				{
					$scope.state.menuOpen = !$scope.state.menuOpen;	
					$scope.state.loginOpen = false;
				},
				toggleLogin: function()
				{
					$scope.state.menuOpen = false;
					$scope.state.loginOpen = !$scope.state.loginOpen;
				},
				register: function()
				{
					$scope.userInfo.errorMessage = "clicked Register";
				},
				login: function()
				{
					$scope.userInfo.errorMessage = "clicked Login";					
				}

			});
		}
	]);

	app.factory('infoService',['$http', function($http)
	{
		return {
			getPosts: function()
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
