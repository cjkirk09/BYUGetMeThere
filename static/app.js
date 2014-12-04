(function(app)
{
	app.controller('menuController', [
		'$scope',
		
		function($scope)
		{
			angular.extend($scope, {
				state: {
					menuOpen: false
				},
				toggleMenu: function()
				{
					$scope.state.menuOpen = !$scope.state.menuOpen;	
				}
			});
		}
	]);

})(angular.module('ByuGetMeThereApp', []));