<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Game Answers - Login/Register</title>

	<?php include 'commonHead.php' ?>
	
	<link rel="stylesheet" type="text/css" href="css/forLogin.css">
	<script type="text/javascript" src="js/accountRegister.js"></script>
</head>
<body>
	<?php include 'header.php' ?>

	<div id="content960">
		<section>
			<div class="registerForm">
				<h2 class="headingDark">Register</h1>
				<form id="register" method="GET">

					<div id="leftside">
						<label for="username" class="headingDark">Username</label>	
						<label for="passwd" class="headingDark">Password</label>
						<label for="passwdCheck" class="headingDark">Verify Password</label>
						<label for="email" class="headingDark">Email</label>
					</div>

					<div id="rightside">
						<input type="text" name="username" id="usernameReg" />
						<input type="password" name="passwd" id="passdReg" />
						<input type="password" name="passwdCheck" id="passCheck" />
						<input type="email" name="email" id="email" size="40"/>
			
						<label class='error' id='errorReg' style='display: none; font-size: 12px; padding: 5px 0px;'></label>
					
						<button class="submit" type="submit" name="submitReg">Sign Up</button>
					</div>
				</form>
			</div>

		</section>
	</div>


</body>
</html>