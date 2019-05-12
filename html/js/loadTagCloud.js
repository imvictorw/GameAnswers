$(document).ready( function() {

	$.ajax({
		url: './server/getTagCloud.cgi',
		type: 'GET',

		success: function(data) {
			window.tagData = $.parseJSON(data);

			for (window.increment = 0; window.increment < 25; ++window.increment) {			
				$(".tagCloud").append('<a href="index.php?id=' + 
					window.tagData[window.increment]['id_pk'] + 
					'"><li class="tag">' + 
					window.tagData[window.increment]['name'] + 
					'</li></a>');
			}
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});

	$("body").append("<footer></footer>")
	$("footer").load("footer.php");

})