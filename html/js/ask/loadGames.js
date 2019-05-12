$(document).ready( function() {

	$.ajax({
		url: './server/getTagList.cgi',
		type: 'GET',

		success: function(data) {
			window.tagData = $.parseJSON(data);

			if ($('#game').html() != null) {
				for (window.increment = 0; window.increment < window.tagData.length; ++window.increment) {			
					$("#gameOptions").append('<option value="' + (window.increment + 1) + '">' + window.tagData[window.increment]['name'] + '</option>');
				}
			}
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});

})