$(document).ready(function(){

	// highlights the nav bar link that we are on
	$('nav a').attr('href', function() {
		var x = window.location.pathname.substring(location.pathname.lastIndexOf("/") + 1);

		if (x.length == 0)
		{
			console.log("changed");
			window.location.pathname = window.location.pathname + "index.php";
			return;
		}

		// 
		if ($(this).attr('href').indexOf(x) != -1) {
			$(this).css({
				"color" : "#FF6000"
			});
		}
	});
});