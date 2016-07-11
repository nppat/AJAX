$(document).ready(function(){
	var pokemon = '';
	for(var i = 1;i < 152; i++)	{
		pokemon += "<img src='http://pokeapi.co/media/img/"+ i +".png'>";
	}
	$('#holder').html(pokemon);
})