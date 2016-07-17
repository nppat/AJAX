**Well, this works great without the AJAX, but with it on, it will not delete the newest note that has been created, but WILL delete the older ones, not sure why this is.  Certainly irritating, but I have ran out of time for this assignment and need to move onto the next.**



- Form for updating the note information (title, description) for the 'Django' note - note that there is no 'button' to submit this form, but that's okay. We'll initially have this 'Update' button in our app and update our information using this 'button' and once we get Ajax working just hide this 'Update' button. Now ask yourself what information would you need to include in this form? Title, Description, and maybe the ID of the note that was created???

- Form for deleting the note information for the 'Django' note - now ask yourself what information would you need to include in this form? 		Maybe the id of the note that was created???

- Form for updating the note information (title, description) for the Python note.

-Form for deleting the note information for the 'Python' note.

-Form for creating a new note - now what information should you have in this form?


Once you identify what forms you need, building the app becomes much easier.

Instructions

- You should have a database table called 'notes' with 'id', 'title', 'description', 'created_at', and 'updated_at' and adding notes adds a new record to the database.
- Make sure you that make all of this work without ajax first (when you submit the form, it should add/delete/update the note in the database and also output a valid jSON data, or a partial).