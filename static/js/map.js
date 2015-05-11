
       var byu = new google.maps.LatLng(40.248770, -111.649273);
       var myLocation;
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
             zoom:16,
             minZoom:14,
             maxZoom:20,
             mapTypeId: google.maps.MapTypeId.ROADMAP,
             zoomControlOptions:{
                style: google.maps.ZoomControlStyle.DEFAULT,
                position: google.maps.ControlPosition.LEFT_CENTER
             }
          };
  
          map=new google.maps.Map(document.getElementById('map'),mapProp);
          directionsDisplay.setMap(map);
          getMyCoords(null, true);
          
           // bounds of the desired area
          var allowedBounds = new google.maps.LatLngBounds(
             new google.maps.LatLng(40.242973, -111.663233),
             new google.maps.LatLng(40.266010, -111.638085)
          );
          var boundLimits = {
              maxLat : allowedBounds.getNorthEast().lat(),
              maxLng : allowedBounds.getNorthEast().lng(),
              minLat : allowedBounds.getSouthWest().lat(),
              minLng : allowedBounds.getSouthWest().lng()
          };

          var lastValidCenter = map.getCenter();
          var newLat, newLng;
          google.maps.event.addListener(map, 'center_changed', function() {
              center = map.getCenter();
              if (allowedBounds.contains(center)) {
                  // still within valid bounds, so save the last valid position
                  lastValidCenter = map.getCenter();
                  return;
              }
              newLat = lastValidCenter.lat();
              newLng = lastValidCenter.lng();
              if(center.lng() > boundLimits.minLng && center.lng() < boundLimits.maxLng){
                  newLng = center.lng();
              }
              if(center.lat() > boundLimits.minLat && center.lat() < boundLimits.maxLat){
                  newLat = center.lat();
              }
              map.panTo(new google.maps.LatLng(newLat, newLng));
          });
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
             myLocation = pos;
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
     
     function getMyCoords(scope,initial){
		 var isCurrentLocation;
		 if(scope == null){
			 isCurrentLocation = false;
		 }
		 else{
			 isCurrentLocation = scope.routeInfo.startPoint == "currentLocation";
		 }
		 if(isCurrentLocation || initial){ //initial is a bool to tell where this is the initial finding of my location
			if(navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(position) {
                   myLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
		        });
			}        
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
				start = myLocation;
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
        function zoomIn()
        {
            var img = document.getElementById('floorplan-img');
            img.height = img.height * 1.5;
            img.width = auto
        }
        function zoomOut()
        {
            var img = document.getElementById('floorplan-img');
            img.height = img.height / 1.5;
            img.width = auto
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
