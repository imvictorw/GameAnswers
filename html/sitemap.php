<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Game Answers - Sitemap</title>

	<?php include 'commonHead.php' ?>
	<link rel="stylesheet" type="text/css" href="css/sitemap.css">
</head>
<body>
	<?php include 'header.php' ?>
	
	<div id="content960">
	<?php include 'aside.php' ?>
	<section>
		<h2 class="headingDark">Site Map</h2>

		<ul id='sitemap'>
			<li><a href="index.php"> - Index/Home</a></li>
			<ul id='sitemapChild'>
				<li><a href ="sitemap.php"> - Site Map</a></li>
			</ul>
			<li><a href="ask.php">- Ask</a></li>
			<li><a href="browse.php"> - Browse</a></li>
			<ul id='sitemapChild'>
				<li><a href="thread.php?id=1"> - Question Thread</a></li>
			</ul>
			<li><a href="support.php"> - Support</a></li>
			<li><a href="register.php"> - Register</a></li>
	</ul>
	</section>

	</div>


</body>
</html>