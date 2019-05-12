$(document).ready(function () {
   //initializing the accordion
  $('#navigationMenu').accordion({
        heightStyle: "content",
   	 	  autoHeight: false,
        active: false,
        alwaysOpen: false,
        fillspace: false,
        collapsible: true,
        navigation: true,
        clearStyle: true
    });

  $('#navigationMenu').accordion({ 
        active: 0
     });

  $('headings').unbind('click');
  
});