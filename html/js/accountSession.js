//=============================================================================
function pollLoginSession() {

	console.log("pollLoginSession: gaAccountName = " + sessionStorage.gaAccountName);

	if (sessionStorage.gaAccountName) {
		$('#loginLink').html('<a href="./profile.php">' + sessionStorage.gaAccountName + "</a>");
		return;
	}

	$('#loginLink').html('<a href="./register.php">Register</a>');
}

//=============================================================================
function logout() {
	console.log("logout: Clearing session");

	sessionStorage.clear();
	setTimeout(function() {window.location = "./index.php";}, 250);
}

//=============================================================================
function signup() {
	console.log("signup: Redirecting to signup page");

	setTimeout(function() {window.location = "./register.php";}, 250);
}

//=============================================================================
function getUserInfo() {

	var dataPass = {
		'username' : sessionStorage.gaAccountName
	}

	console.log(dataPass);

	// query database with login data
	$.ajax({
		url: './server/getUserData.cgi',
		type: 'GET',
		data: dataPass,

		// success callback
		success: function(data) {
			console.log("getUserInfo.cgi: 'success' callback");

			var converted = $.parseJSON(data);

			console.log(converted[0]['questionCount']);

			if (converted[0]['avatar'] != null) {
				$("#profilepicture").attr("src", converted[0]['avatar']);
				$("#profileBox #questionCount").text(converted[0]['questionCount']);
				$("#profileBox #answerCount").text(converted[0]['answerCount']);
			}
		},

		// error callback
		error: function() {
			console.log("getUserInfo.cgi: 'error' callback");
		},

		// complete callback
		complete: function() {
			console.log("getUserInfo.cgi: 'complete' callback");
		}
	});
}


//=============================================================================
$(document).ready(function() {
	pollLoginSession();

	if (!sessionStorage.gaAccountName)
	{
		$("aside>h2:first-of-type").html("Login");
	}
	else
	{
		$("#profileBox .loginForm").css({"display" : "none"});
		$("#profileBox .loggedIn").css({"display" : "inline"});
		//$("#profileBox h3").css({"display" : "none"})

		//$("#profileBox .logout").before('<h3>' + sessionStorage.gaAccountName + '</h3><img id="profilepicture" width="64" height="64" src=""><br />');
		
		//$("#profileBox img").after('<p>Username: ' + sessionStorage.gaAccountName + '</p>');

		$("#profileBox .loggedIn #usernameText").text(sessionStorage.gaAccountName);
		getUserInfo();
		/*
		 * TODO Add styling to account name, image and other details
		 * TODO Add user info to aside.php
		 * TODO Fix AJAX for getUserInfo()
		 */

		//getUserInfo();
	}

	changepf();
});

//===========================================================================
//Changing profile picture
function changepf(){
	$("#profilepicture").click(function(){

		var pchange = prompt("Enter an url to change your profile picture");
		var dataPass = {
			'avatar' : pchange,
			'username' : sessionStorage.gaAccountName
		}
		console.log(dataPass);
		if(pchange != null){
			if(pchange.length == 0 || pchange.indexOf(".jpg") == -1){
				window.alert("Please enter a valid jpg url for your image.");
				return;
			}
		}

		$.ajax({
			url: './server/addProfilePicture.cgi',
			type: 'GET',
			data: dataPass,

			// success callback
			success: function() {
				console.log("addProfilePicture.cgi: 'success' callback");
				setTimeout(function() {window.location = "./index.php";}, 250); 
			},

			// error callback
			error: function() {
				console.log("addProfilePicture.cgi: 'error' callback");
			},

			// complete callback
			complete: function() {
				console.log("addProfilePicture.cgi: 'complete' callback");
			}
		});
	})
}