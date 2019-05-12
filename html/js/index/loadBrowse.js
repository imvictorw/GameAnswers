$(document).ready( function() {

	$.ajax({
		url: 'question.php',
		type: 'GET',

		success: function(data) {
			window.questionData = data;
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});

	var tab2 = false;
	var tab3 = false;
	var tab4 = false;
	loadFeaturedTab();

	$("#loadtab2").click(function(){
		if (!tab2)
			loadHotTab();
		tab2 = true;
	});

	$("#loadtab3").click(function(){
		if (!tab3)
			loadUnanswered();
		tab3 = true;
	});

	$("#loadtab4").click(function(){
		if (!tab4)
			loadLeastViewed();
		tab4 = true;
	});
});

function loadFeaturedTab() {

	$.ajax({
		url: './server/getThread_loadFeatured.cgi',
		type: 'GET',

		success: function(data) {

			window.featuredData = $.parseJSON(data);

			var section = $("#tabs-1");

			for (window.increment = 0; window.increment < window.featuredData.length; ++window.increment) {
			
				section.append(window.questionData);
				$('#tabs-1 .text p').last().html(window.featuredData[window.increment]['title']);
				$('#tabs-1 .userName a').last().html(window.featuredData[window.increment]['username_fk']);
				$('#tabs-1 .fadebg').last().html(window.featuredData[window.increment]['game_fk']);
				$('#tabs-1 .views .top').last().html(window.featuredData[window.increment]['score']);
				$('#tabs-1 .answers .top').last().html(window.featuredData[window.increment]['answercount']);

				var date = new Date(window.featuredData[window.increment]['timestamp']);
				var dateNow = new Date();

				var diff = (dateNow.getTime() - date.getTime()) / 1000;

				if (diff < 61) {
					$('#tabs-1 .time').last().html( parseInt( diff ) + " s");
				} else if (diff < 7200) {
					$('#tabs-1 .time').last().html( parseInt( diff / 60 ) + " mins");
				} else if (diff < 172800) {
					$('#tabs-1 .time').last().html( parseInt( diff / 3600) + " hrs");
				} else {
					$('#tabs-1 .time').last().html( parseInt( diff / 86400) + " days");
				}
			}

			$('.questionSummary').click(function() {
				window.location = "./thread.php?id=" + window.featuredData[$(this).index()]['id_pk'];
			});

			console.log("Thread: Success");
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});
}

function loadHotTab() {

	$.ajax({
		url: './server/getThread_loadHot.cgi',
		type: 'GET',

		success: function(data) {

			window.hotData = $.parseJSON(data);

			var section = $("#tabs-2");

			for (window.increment = 0; window.increment < window.hotData.length; ++window.increment) {
			
				section.append(window.questionData);
				$('#tabs-2 .text p').last().html(window.hotData[window.increment]['title']);
				$('#tabs-2 .userName a').last().html(window.hotData[window.increment]['username_fk']);
				$('#tabs-2 .fadebg').last().html(window.hotData[window.increment]['game_fk']);
				$('#tabs-2 .views .top').last().html(window.hotData[window.increment]['score']);
				$('#tabs-2 .answers .top').last().html(window.hotData[window.increment]['answercount']);

				var date = new Date(window.hotData[window.increment]['timestamp']);
				var dateNow = new Date();

				var diff = (dateNow.getTime() - date.getTime()) / 1000;

				if (diff < 61) {
					$('#tabs-2 .time').last().html( parseInt( diff ) + " s");
				} else if (diff < 7200) {
					$('#tabs-2 .time').last().html( parseInt( diff / 60 ) + " mins");
				} else if (diff < 172800) {
					$('#tabs-2 .time').last().html( parseInt( diff / 3600) + " hrs");
				} else {
					$('#tabs-2 .time').last().html( parseInt( diff / 86400) + " days");
				}
			}

			$('.questionSummary').click(function() {
				window.location = "./thread.php?id=" + window.hotData[$(this).index()]['id_pk'];
			});

			console.log("Thread: Success");
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});
}

function loadUnanswered() {
	
	$.ajax({
		url: './server/getThread_loadUnanswered.cgi',
		type: 'GET',

		success: function(data) {

			window.unansweredData = $.parseJSON(data);

			var section = $("#tabs-3");

			for (window.increment = 0; window.increment < window.unansweredData.length; ++window.increment) {
			
				section.append(window.questionData);
				$('#tabs-3 .text p').last().html(window.unansweredData[window.increment]['title']);
				$('#tabs-3 .userName a').last().html(window.unansweredData[window.increment]['username_fk']);
				$('#tabs-3 .fadebg').last().html(window.unansweredData[window.increment]['game_fk']);
				$('#tabs-3 .views .top').last().html(window.unansweredData[window.increment]['score']);
				$('#tabs-3 .answers .top').last().html(window.unansweredData[window.increment]['answercount']);

				var date = new Date(window.unansweredData[window.increment]['timestamp']);
				var dateNow = new Date();

				var diff = (dateNow.getTime() - date.getTime()) / 1000;

				if (diff < 61) {
					$('#tabs-3 .time').last().html( parseInt( diff ) + " s");
				} else if (diff < 7200) {
					$('#tabs-3 .time').last().html( parseInt( diff / 60 ) + " mins");
				} else if (diff < 172800) {
					$('#tabs-3 .time').last().html( parseInt( diff / 3600) + " hrs");
				} else {
					$('#tabs-3 .time').last().html( parseInt( diff / 86400) + " days");
				}
			}

			$('.questionSummary').click(function() {
				window.location = "./thread.php?id=" + window.unansweredData[$(this).index()]['id_pk'];
			});

			console.log("Thread: Success");
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});
}

function loadLeastViewed() {

	$.ajax({
		url: './server/getThread_loadLeastViewed.cgi',
		type: 'GET',

		success: function(data) {

			window.LeastViewedData = $.parseJSON(data);

			var section = $("#tabs-4");

			for (window.increment = 0; window.increment < window.LeastViewedData.length; ++window.increment) {
			
				section.append(window.questionData);
				$('#tabs-4 .text p').last().html(window.LeastViewedData[window.increment]['title']);
				$('#tabs-4 .userName a').last().html(window.LeastViewedData[window.increment]['username_fk']);
				$('#tabs-4 .fadebg').last().html(window.LeastViewedData[window.increment]['game_fk']);
				$('#tabs-4 .views .top').last().html(window.LeastViewedData[window.increment]['score']);
				$('#tabs-4 .answers .top').last().html(window.LeastViewedData[window.increment]['answercount']);

				var date = new Date(window.LeastViewedData[window.increment]['timestamp']);
				var dateNow = new Date();

				var diff = (dateNow.getTime() - date.getTime()) / 1000;

				if (diff < 61) {
					$('#tabs-4 .time').last().html( parseInt( diff ) + " s");
				} else if (diff < 7200) {
					$('#tabs-4 .time').last().html( parseInt( diff / 60 ) + " mins");
				} else if (diff < 172800) {
					$('#tabs-4 .time').last().html( parseInt( diff / 3600) + " hrs");
				} else {
					$('#tabs-4 .time').last().html( parseInt( diff / 86400) + " days");
				}
			}

			$('.questionSummary').click(function() {
				window.location = "./thread.php?id=" + window.LeastViewedData[$(this).index()]['id_pk'];
			});

			console.log("Thread: Success");
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});
}