**Instructions**
- make sure that you build this form without Ajax first. In other words, make sure the form is posted to say '/posts/create' and make sure '/posts/create' adds a new record to the database and return in json format or you can return a partial (up to you) the results.

- make sure that you're storing the information on the database (create a table called 'posts' with 'id', 'description', 'created_at', and 'updated_at'). I didn't follow directions and created a schema with a table called notes with id, notes, created_at and updated_at. [x]

- once '/notes/create' is all working perfectly (adding new records to the database and outputting the right json data, or the right partial), then turn Ajax on and make sure it's working now with Ajax.

**Helpful things to remember**
- Remember that .post sends a new HTTP request and can use information received back from that request to update part of the page.  The .post method again does not send that information directly to your controller or model.  It simply initiates a new HTTP request. 

- It's your back-end code's job to provide relevant HTTP response (HTML or json) back for your JavaScript to use.  When your backend codes echo or prints something, all of these are sent back as the HTTP response (in other words, if your codes store information to the proper database but do not print or echo anything, your HTTP response would basically be blank and your javascript code may not know what to do).


--  For some reason, my input validation will not work correctly.  It works perfect without the AJAX on, but when switched on, it will not flash the error or success message, unless the page is refreshed.  Not sure why.