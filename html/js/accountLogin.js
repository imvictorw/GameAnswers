//=============================================================================
$(document).ready(function() {
	$('form#login').submit(submitLogin);
});

//=============================================================================
/// submitLogin
/// Attempts to login with the data in the form. Creates session if successful
//=============================================================================
function submitLogin(e)
{
	e.preventDefault();

	var dataPass = $("form#login").serialize(); 
	console.log("submitLogin() - data: " + dataPass);

	// query database with login data
	$.ajax({
		url: './server/login.cgi',
		type: 'GET',
		data: dataPass,

		// success callback
		success: function(data) {
			console.log("login.cgi: 'success' callback");

			// checks for actual success
			if (data.indexOf("success") != -1) {
				 console.log("login.cgi: success");

				$('#errorLogin').css({
					'color' : '#0c0',
					'display' : 'block'});

				$('#errorLogin').html("You've successfully logged in.");

				// create local login session
				sessionStorage.gaAccountName = $("#usernameLogin").val();
				setTimeout(function() {window.location = "./index.php";}, 500);
			}
			else {
				console.log("login.cgi: incorrect details");
				
				$('#errorLogin').css({'color':'red','display':'block'}).html("Invalid username and/or password.");
			}
		},

		// error callback
		error: function() {
			console.log("login.cgi: 'error' callback");

			$('#errorLogin').css({
				'color' : 'red',
				'display' : 'block'});

			$('#errorLogin').html('Server error. Try again.');
		},

		// complete callback
		complete: function() {
			console.log("login.cgi: 'complete' callback");
		}
	});
}
