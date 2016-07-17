$(document).ready(function(){
	$('img').hide(); // Waiting gif
	$('form').submit(function(){ // on form submit
		$('img').show(); // Show loading gif
		//Use this action attribute and serialize
		$.post($(this).attr('action'), $(this).serialize(), function(res) {
			console.log(res);
			var html_string = ""; // create var to build html
			// Show user what they typed in, using what was returned from google api
			html_string += "<h3 class='text-center'>Directions from "+res.routes[0].legs[0].start_address+" to "+res.routes[0].legs[0].end_address+".</h3>";
			html_string += "<ul class='list-group'>"; // start building a list
			for (var  i= 0; i < res.routes[0].legs[0].steps.length; i++){ // loop through each step that there is in the route
				// Each step has html_instruction which indicates "right,left, street etc", so list each step with instructions
				 html_string += "<li class='list-group-item'>" + res.routes[0].legs[0].steps[i].html_instructions + "</li>";
			}
			console.log(html_string);
			html_string += "</ul>"; // close out the list
			$('img').hide(); // hide loading gif
			$('#result').html(html_string); // display html_string in #result div
		}, 'json');
		return false; // do not refresh page
	});
});