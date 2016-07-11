$(document).ready(function(){
	// show the Pokemon in the div
	var pokemon = '';
	for(var i = 1;i < 152; i++)	{ // Loop through the Pokemon and add each image to the Pokemon variable
		pokemon += "<img id='"+ i +"'src='http://pokeapi.co/media/img/"+ i +".png'>";
	}
	document.getElementById("holder").innerHTML = pokemon; // Display the Pokemon in the #holder div
	
	// On click, display Pokemon info in the card.  Name, image, types, height, & weight
	$('img').click(function(){
		var img_id = $(this).attr('id');
		$.get("http://pokeapi.co/api/v1/pokemon/" + img_id, function(res){
			var info = "";
			info += "<h2>" + res.name + "</h2>"; // Get name
			info += "<img id='" + img_id + "' src='http://pokeapi.co/media/img/"+ img_id +".png'>"; // Get image
			info += "<h3>Types</h3>"; // Get types
			info += "<ul>"; // create unordered list
			for(var i = 0; i < res.types.length; i++){ //  loop through types and add them to info
				info += "<li>" + res.types[i].name + "</li>";
			}
			info += "</ul>";
			info +="<h3> Height </h3>"
			info +="<h4>" + res.height + "</h4>"; // get height
			info +="<h3> Weight </h3>"
			info +="<h4>" + res.weight + "</h4>"; // get weight
			$("#pokedex").html(info); // build html in #pokedex passing in the info variable
		}, "json"); // type of info we expect to get back is json
	});
});