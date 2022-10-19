"use strict"

$(document).ready ( () => {
   //click on the image changes the enlarge image to that image
   $("#image_list a").click( evt => {
      evt.preventDefault();
      const target = evt.currentTarget.href;
      $("#image").attr("src", target);

      //This is animate where it fade out to the left
      $("#image").animate(
         {opacity: 0, marginLeft: "-=250"}, 1000,
         () => {
            //This is a callback function where the animate the fadeIn to the right
            $("#image").animate(
               {opacity: 1, marginLeft: "+=250"} , 1000);
         }
      );
   });

   const slider = $("#image_list");      // slider = ul element

    // the click event handler for the right button
    $("#right_button").click( () => { 

        // get value of current left property
        const leftProperty = parseInt(slider.css("left"));
        
        // determine new value of left property
        let newLeftProperty = 0;
        if (leftProperty - 100 > -900) {
            newLeftProperty = leftProperty - 100;
        }
        
        // use the animate function to change the left property
        slider.animate({left: newLeftProperty}, 1000);    
    }); 
    
    // the click event handler for the left button
    $("#left_button").click( () => {
    
        // get value of current left property
        const leftProperty = parseInt(slider.css("left"));
        
        // determine new value of left property
        let newLeftProperty = 0;
        if (leftProperty < 0) {
            newLeftProperty = leftProperty + 100;
        }
        else {
            newLeftProperty = -800;
        }
        
        // use the animate function to change the left property
        slider.animate({left: newLeftProperty}, 1000);
    });

});