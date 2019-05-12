$(document).ready(function() {
	$('form#askQuestion').submit(submitThread);
	window.flag = false;

});

//=============================================================================
/// SubmitThread
/// Submits the question on "ask.php" to the database, does some pre-checks.
//=============================================================================
function submitThread (e) {
	if (window.flag == true)
		return;
	
	$('form#askQuestion .submit').hide();

	e.preventDefault();

	// check user has logged in
	if (!sessionStorage.gaAccountName)
	{
		alert("Please login to continue");
		return;
	}

	// get database data from DOM
	var argTitle = $('input[name="questionTitle"]').val();
	var argBody = $('textarea[name="questionBody"]').val();
	var gameOptions = $('select')[0].options;
	var argGame = gameOptions[gameOptions.selectedIndex].text;

	// ensure the user has filled in required information
	if (argTitle.length == 0)
		alert("You need a title!");
	else if (argBody.length == 0)
		alert("You need a question!");
	else if (argGame.length == 0)
		alert("You need a game!");
	else
		window.flag = true;

	// if not enough info, then submit button will reappear
	if (window.flag == false) {
		$('form#askQuestion .submit').show();
		return;
	}
	window.flag = false;

	// serialize data into a JSON friendly format
	var dataKnown = {
		'username' : sessionStorage.gaAccountName,
		'game' : argGame,
		'title' : argTitle,
		'body' : argBody
	};

	// submit data to database
	$.ajax({
		url: './server/createThread.cgi',
		type: 'GET',
		data: dataKnown,

		success: function(data) {
			console.log("submitThread: 'success' callback");

			if (data.indexOf("success") != -1) {
				window.location = "./index.php";
				window.flag = true;
			}
			else {
				alert("Server error.");
				$('form#askQuestion .submit').show();
			}
		},

		error: function() {
			console.log("submitThread: 'error' callback");
			$('form#askQuestion .submit').show();
		},

		complete: function() {
			console.log("submitThread: 'complete' callback");
		}
	});
}