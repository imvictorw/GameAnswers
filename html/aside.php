<aside>
	<h2 class="headingDark">Account</h2>
	<div class="container" id="profileBox">

		<div class="loginForm">
			<form id="login" method="GET">
				<label for="username">Username</label><br />
				<input type="text" size="30" placeholder="username" name="username" id="usernameLogin" /><br />
			
				<label for="passd">Password</label><br />
				<input type="password" size="30" placeholder="password" name="passd" id="passdLogin" /><br />

				<label class='error' id='errorLogin' style='display: none; font-size: 12px; padding: 5px 0px;'></label>
			
				<button type="submit" name="login" class="submit">Login</button>
				<button onclick="signup(); return false;" id="signupButton">Signup</button>
			</form>
		</div>

		<div style="display:none;" class="loggedIn">
			<img id="profilepicture" width="64" height="64" src="">
			<div id="content">
				<p><span id="usernameText"></span></p>
				<p><span id="questionCount"></span> questions</p>
				<p><span id="answerCount"></span> answers</p>
				<p></p>
			</div>
			
			<button  type="submit" name="logout" class="logout" onclick="logout()">Logout</button>
		</div>
	</div>

	<h2 class="headingDark">Tag Cloud</h3>
	<div class="container" id="recentTags">
		<ul class="tagCloud">
		</ul>
	</div>
</aside>