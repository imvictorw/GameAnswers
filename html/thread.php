<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Game Answers</title>

	<?php include 'commonHead.php' ?>
	
	<link rel="stylesheet" type="text/css" href="css/questionSummary.css">
	<link rel="stylesheet" type="text/css" href="css/forThread.css">

	<script type="text/javascript" src="js/thread/getThread.js"></script>
	<script type="text/javascript" src="js/thread/createReply.js"></script>

</head>
<body>
	<?php include 'header.php'; ?>

	<div id="content960">
		<?php include 'aside.php'; ?>
		<section>
			<h2 class="headingDark" id="threadTitle"></h2>

			<div id="question">
				<img width="64px" height="64px" src="">

				<div id="score">
					<p></p>
				</div>
				
				<div id="body">
					<p></p>
				</div>

				<div id="info">
					<p></p>
				</div>
			</div>
			
			<div id="replies">
			</div>

			<div id="newreply">
				<h3>Reply</h3>
				<form id="createreply" method="GET">
					<textarea name="" id="" cols="30" rows="10"></textarea>

					<button onclick="return false;">Submit</button>
				</form>
			</div>

		</section>

	</div>

</body>
</html>