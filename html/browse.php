<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Game Answers</title>
	<link rel="stylesheet" href="css/questionSummary.css">
	<?php include 'commonHead.php' ?>

	<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css">
	
	<link rel="stylesheet" href="css/browse.css">

	<script type="text/javascript" src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
	<script type="text/javascript" src="js/browse.js"></script>
	<script type="text/javascript" src="js/index/loadBrowse.js"></script>
</head>
<body>
	<?php include 'header.php'; ?>

	<div id="content960">

		<?php include 'aside.php'; ?>
		<section>
			<h2 class="headingDark">Browse Questions</h2>
			<div id="tabs">
				<ul class ="tabbs">
					<!--Most Viewed  => Featured
						Most Answers => What's Hot
						No answers   => Unanswered
						Least Viewed => Least Viewed -->
					<li id="loadtab1"><a href="#tabs-1">Most Viewed</a></li>
					<li id="loadtab2"><a href="#tabs-2">What's Hot</a></li>
					<li id="loadtab3"><a href="#tabs-3">Unanswered</a></li>
					<li id="loadtab4"><a href="#tabs-4">Least Viewed</a></li>
				</ul>
				<div id="tabs-1">
				</div>
				<div id="tabs-2">
				</div>
				<div id="tabs-3">
				</div>
				<div id="tabs-4">
				</div>
			</div>
		</section>
	

	</div>

</body>
</html>