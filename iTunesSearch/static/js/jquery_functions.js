$(document).ready(function() {
	$('img').hide(); // the Gif has to be hidden first
    $('form').submit(function() {
        $('img').show(); // Gif used for waiting on the load up
        $.post($(this).attr('action'), $(this).serialize(), function(res) {
            console.log('the response object:');
            console.log(res); // shows the input into res
            var html_string = ""; // start to build the html string to go into the result div
            if(res.results.length !== 0) {
                html_string = "<video controls src='" + res.results[0].previewUrl + "'></video>"; // insert the data we pulled from the json, using the first index in the results
            } else {
                html_string = "Not Found"; // error message
            }
            console.log('the html string:');
            console.log(html_string); // shows the html_string loaded up
            $('img').hide();  //  hide the waiting gif
            $('#result').html(html_string) // insert html_string into the div to show the video, if there is one to show
        }, 'json');
        return false;
    });
});
