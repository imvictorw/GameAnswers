<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Game Answers</title>

	<?php include 'commonHead.php' ?>
	
	<script type="text/javascript" src="js/ask/submitQuestion.js"></script>
	<script type="text/javascript" src="js/ask/loadGames.js"></script>

</head>
<body>
	<?php include 'header.php'; ?>

	<div id="content960">
		<?php include 'aside.php'; ?>
		<section>
			<h2 class="headingDark">Ask a Question</h2>

			<!-- Question Form -->
			<form id="askQuestion" method="GET">
				<div id="title">
					<h4 class="headingDark">Title</h4>
					<input type="text" name="questionTitle" id="questionTitle" size="50">
				</div>

				<div id="question">
					<h4 class="headingDark">Question</h4>
					<textarea name="questionBody" id="questionBody"></textarea>
				</div>
				
				<div id="game">
					<h4 class="headingDark">Game Tag</h4>
					<select name="gameOptions" id="gameOptions">
						<option value="" selected></option>
					</select>
				</div>

				<button type="submit" name="submitThread" class="submit">Submit</button>
			</form>

		</section>

	</div>


</body>
</html>