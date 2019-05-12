$(document).ready( function() {
	$('#createreply button').click(function() {
		window.flag = false;
		submitReply();
	});
});

function submitReply() {
	if (window.flag == true)
		return;

	$('#createreply button').hide();

	// check user has logged in
	if (!sessionStorage.gaAccountName) {
		alert("Please login to continue");
		return;
	}

	var dataPass = {
		"questionid" : getURLParameter("id"),
		"username" : sessionStorage.gaAccountName,
		"body" : $("#newreply textarea").val()
	};

	if (dataPass["body"].length == 0)
		alert("You need some text!");
	else
		window.flag = true;

	// if not enough info, then submit button will reappear
	if (window.flag == false) {
		$('#createreply button').show();
		return;
	}
	window.flag = false;

	$.ajax({
		url: './server/createReply.cgi',
		type: 'GET',
		data: dataPass,

		success: function(returnedData) {

			var dataParsed = returnedData;

			if (returnedData.indexOf("success") != -1) {
				window.location = "";
			}
			else {
				alert("Server error.");
				$('#createreply button').show();
			}

			console.log("Thread: Success");
		},

		error: function() {
			console.log("Thread: Error");
			$('form#askQuestion .submit').show();
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});
}