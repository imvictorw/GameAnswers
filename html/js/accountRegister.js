//=============================================================================
$(document).ready(function() {
		
		$('form#register').submit(submitRegister); 
});

//=============================================================================
function submitRegister(e)
{
	var pwLength = document.getElementById('passCheck').value.length
	var verifyPW = document.getElementById('passCheck').value
	var inputPW = document.getElementById('passdReg').value
	e.preventDefault();
	var dataPass = $("form#register").serialize();
	console.log("submitRegister: dataPass = " + dataPass);
	
	console.log(verifyPW);
	console.log(inputPW);
	if(pwLength < 6){
		$('#errorReg').css({
				'color' : 'red',
				'display' : 'block'});

			$('#errorReg').html("Your password contains less that 6 letters.");
			return;
	}
	if(verifyPW != inputPW){
		$('#errorReg').css({
				'color' : 'red',
				'display' : 'block'});

			$('#errorReg').html("The entered passwords do not match.");
			return;
	}
	// attempt to 'register' with the database
	$.ajax({
		url: './server/register.cgi',
		type: 'GET',
		data: dataPass,

		// success callback
		success: function() {
			console.log("register.cgi: 'success' callback");

			$('#errorReg').css({
				'color' : '#0c0',
				'display' : 'block'});

			$('#errorReg').html("You have successfully registered.");

			setTimeout(function() {window.location = "./index.php";}, 500);
		},

		// error callback
		error: function() {
			console.log("register.cgi: 'error' callback");
			
			$('#errorReg').css({
				'color' : 'red',
				'display' : 'block'});

			$('#errorReg').html('Server error. Try again.');
		},

		// complete callback
		complete: function() {
			console.log("register.cgi: 'complete' callback");
		}
	});
}
