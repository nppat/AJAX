$(document).ready(function(){
	$('form').submit(function(){ // on form submit
		var city = $('#city').val();
		var url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=imperial&appid=e2effeb6fa653cd523b960990a1d7f3f";
		// adding &units=imperial converts the temp to F.  Found this in the API docs.
		$.get(url, function(res){
			var data = ''; // set data var
			data += "<h1>"+ res.main.temp + "&deg; F</h1>"; // Get temperature, style in degrees F
			data += "<p>in</p>";
			data += "<h2>" + res.name + "</h2>"; // Get City name
			$("#weather_data").html(data); // Send to div and build the html
		}, "json");
		return false; // False so the page does not refresh
	});
});