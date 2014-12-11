
        var byu = new google.maps.LatLng(40.248770, -111.649273);
       var map;
       var positionmarker;
       var startmarker;
       var endmarker;
       var directionsDisplay;
       var directionsService = new google.maps.DirectionsService();

       function initialize(){
          directionsDisplay = new google.maps.DirectionsRenderer();
          //directionsDisplay.setSuppressMarkers(true);
          var mapProp = {
             center:byu,
             zoom:15,
             mapTypeId: google.maps.MapTypeId.ROADMAP,
             zoomControlOptions:{
                style: google.maps.ZoomControlStyle.DEFAULT,
                position: google.maps.ControlPosition.LEFT_CENTER
             }
          };
  
          map=new google.maps.Map(document.getElementById('map'),mapProp);
          directionsDisplay.setMap(map);
       }

       // Try HTML5 geolocation
       function findMyLocation(){
       // window.alert("in findMyLocation");
       if(positionmarker != null){
          positionmarker.setMap(null);
       }
       if(navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
             var pos = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
             //console.log("I found the user's position: " + pos);

             positionmarker = new MarkerWithLabel({
                 map:map,
                 draggable:false,
                 animation: google.maps.Animation.DROP,
                 position: pos,
                 title: "Your Location",

                 labelContent: "You are here",
                 labelAnchor: new google.maps.Point(22, 0),
                 labelClass: "maplabels", // the CSS class for the label
                 labelStyle: {opacity: 0.75}
             });
  
             map.setCenter(pos);
             // when the map is at 17 it's close enough to see individual BYU buildings.
             // map.setZoom(12);
             
              map.setZoom(17);
             

           }, function() {handleNoGeolocation(true);});
       } //closes if
       else {
         // Browser doesn't support Geolocation
         handleNoGeolocation(false);
       }
     }//closes findMyLocation
  
     function handleNoGeolocation(errorFlag) {
       if (errorFlag) {
         var content = 'Error: The Geolocation service failed.';
       } else {
         var content = 'Error: Your browser doesn\'t support geolocation.';
       }
       
       var options = {
         map: map,
         position: byu,
         content: content
       };
     
       var infowindow = new google.maps.InfoWindow(options);
       map.setCenter(options.position);
       map.setZoom(16);
     }

     function clearRoute(){
         if(positionmarker != null){
              positionmarker.setMap(null);
         }
         directionsDisplay.set('directions',null);
         if(startmarker != null ){
			 startmarker.close();
		 }
		 if(endmarker != null ){
			 endmarker.close();
		 }
     }

     function getRoute(scope){
         // set selected buildings
         var message = scope.getRoute();
	     scope.$apply();
	     if( scope.routeInfo.errorMessage == "" ){
            toggleRouteBox();
            scope.$apply();
            var path = scope.routeInfo.path;
            var start = null;
            if( path[0] == "currentLocation" ){
				if(navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(function(position) {
                      start = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
		           }, function() {handleNoGeolocation(true);});
			   }
			   else{
				   handleNoGeolocation(false);
				   clearRoute();
				   return;
			   }
			   //findMyLocation();
			   //return;
			}        
            else{
                start = new google.maps.LatLng(path[0].latitude, path[0].longitude);
            }
			
			var end = new google.maps.LatLng(path[path.length-1].latitude, path[path.length-1].longitude);
            var waypts = [];
            if( path.length >2 ){
                for( var i=1; i < path.length-1; i++ ){
                    waypts.push( { location: new google.maps.LatLng(path[i].latitude, path[i].longitude), stopover:true});
                }
            }
            var request = {
                origin: start,
                destination: end,
                waypoints: waypts,
                optimizeWaypoints: false,
                travelMode: google.maps.TravelMode.WALKING
            };
            directionsService.route(request, function(response, status) {
                if (status == google.maps.DirectionsStatus.OK) {
					if(startmarker != null ){
			           startmarker.close();
		            }
		            if(endmarker != null ){
			           endmarker.close();
		            }
                    directionsDisplay.setDirections(response);
                    startmarker = new google.maps.InfoWindow({
                        map:map,
                        position: start,
                        content: "Start: "+scope.routeInfo.startPoint,
                    });
                    endmarker = new google.maps.InfoWindow({
                        map:map,
                        position: end,
                        content: "End: "+scope.routeInfo.endPoint,
                    });

                }
            });
        }
     }
     
     google.maps.event.addDomListener(window, 'load', initialize);
   
		function display(){
            window.alert("in display");
        }
         function goTo(id){
            window.scroll(0,findPos(document.getElementById(id)));
        }
        
        function findPos(obj) {
            var curtop = 0;
            if (obj.offsetParent) {
            do {
                curtop += obj.offsetTop;
            } while (obj = obj.offsetParent);
            return [curtop];
            }
        }
        
        function toggleRouteBox() {
            document.getElementById("routebox").style.visibility = "visible";
            if(document.getElementById("routebox").style.display == "none" ) {
                document.getElementById("routebox").style.display = "";
            }
            else {
                document.getElementById("routebox").style.display = "none";
            }
        }
        
        function closeRouteBox() {
            document.getElementById("routebox").style.visibility = "hidden";
        }
