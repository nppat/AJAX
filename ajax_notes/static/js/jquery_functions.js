$(document).ready(function(){
   $('#add_form').submit(function(){
   		alert("Ok add new note");
		$.post('/notes/create', $(this).serialize(), function(res) {
			console.log(res);
			$('#notes').html(res);

		});
		$('#add_form')[0].reset();
		return false;
	});
   $('#delete_form').submit(function(){
   		alert("Ok delete");
   		$.post("/notes/delete/{{ notes['id'] }}", $(this).serialize(), function(res) {
   			console.log(res);
   			$('#notes').html(res);
   		});
   		return false;
	});
   $('#update_form').submit(function(){
   		alert("Ok update");
   		$.post("/notes/update/{{ notes['id'] }}", $(this).serialize(), function(res) {
   			console.log(res);
   			$('#notes').html(res);
   		});
   		return false;
	});
});