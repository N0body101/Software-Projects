"use strict";
$(document).ready( () => {

    // move focus to first text box
    $("#arrival_date").focus();
    
    // the handler for the click event of the submit button
    $("#reservation_form").submit( event => {
        let isValid = true;

		  //validate arrival date
		  const datePattern = /^\d{2}\/\d{2}\/\d{4}$/;
		  const datePattern1 = /^\d{1}\/\d{2}\/\d{4}$/;
		  const datePattern2 = /^\d{1}\/\d{1}\/\d{4}$/;
		  const datePattern3 = /^\d{2}\/\d{1}\/\d{4}$/;
        const date = $("#arrival_date").val().trim();
        if (date == "") { 
            $("#arrival_date").next().text("This field is required.");
            isValid = false; 
        } else if (!datePattern.test(date) && !datePattern1.test(date) && !datePattern2.test(date) && !datePattern3.test(date)) {
            $("#arrival_date").next().text("Use mm/dd/yyyy format.");
            isValid = false;
        } else {
            $("#arrival_date").next().text("");
        }
        $("#arrival_date").val(date);


		  // validate nights
		  const nights = $("#nights").val().trim();
        if (nights == "") {
            $("#nights").next().text("This field is required.");
            isValid = false;
        } else if (isNaN(nights) == true) {
				$("#nights").next().text("Must be numeric.");
				isValid = false;
		  } else {
            $("#nights").next().text("");
        }
        $("#nights").val(nights);

		  // validate the name entry
        const name = $("#name").val().trim();
        if (name == "") {
            $("#name").next().text("This field is required.");
            isValid = false;
        } else {
            $("#name").next().text("");
        }
        $("#name").val(name);
        
        // validate the email entry with a regular expression
        const emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
        const email = $("#email").val().trim();
        if (email == "") { 
            $("#email").next().text("This field is required.");
            isValid = false;
        } else if ( !emailPattern.test(email) ) {
            $("#email").next().text("Must be a valid email address.");
            isValid = false;
        } else {
            $("#email").next().text("");
        }
        $("#email").val(email);

		  // validate the phone number
		  const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
        const phone = $("#phone").val().trim();
        if (phone == "") { 
            $("#phone").next().text("This field is required.");
            isValid = false; 
        } else if ( !phonePattern.test(phone) ) {
            $("#phone").next().text("Use 999-999-9999 format.");
            isValid = false;
        } else {
            $("#phone").next().text("");
        }
        $("#phone").val(phone);
                    
        // prevent the submission of the form if any entries are invalid 
        if (isValid == false) {
            event.preventDefault();                
        }
    });

});