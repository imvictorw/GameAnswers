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

	var filter = "NONE";
	if (getURLParameter("id") != null)
		filter = getURLParameter("id");

	if (filter == "NONE")
		loadMostRecent();
	else
		filterMostRecent(filter);
})

function loadMostRecent() {
	$.ajax({
		url: './server/getThread_MostRecent.cgi',
		type: 'GET',

		success: function(data) {

			window.mostRecentData = $.parseJSON(data);

			var section = $("section");

			for (window.increment = 0; window.increment < window.mostRecentData.length; ++window.increment) {
			
			    section.append(window.questionData);
				$('.text p').last().html(window.mostRecentData[window.increment]['title']);
				$('.userName a').last().html(window.mostRecentData[window.increment]['username_fk']);
				$('.fadebg').last().html(window.mostRecentData[window.increment]['game_fk']);
				$('.views .top').last().html(window.mostRecentData[window.increment]['score']);
				$('.answers .top').last().html(window.mostRecentData[window.increment]['answercount']);

				var date = new Date(window.mostRecentData[window.increment]['timestamp']);
				var dateNow = new Date();

				var diff = (dateNow.getTime() - date.getTime()) / 1000;

				if (diff < 61) {
					$('.time').last().html( parseInt( diff ) + " s");
				} else if (diff < 7200) {
					$('.time').last().html( parseInt( diff / 60 ) + " mins");
				} else if (diff < 172800) {
					$('.time').last().html( parseInt( diff / 3600) + " hrs");
				} else {
					$('.time').last().html( parseInt( diff / 86400) + " days");
				}
			}

			$('.questionSummary').click(function() {
				window.location = "./thread.php?id=" + window.mostRecentData[$(this).index() - 1]['id_pk'];
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

function filterMostRecent(filter) {

	var dataPass = {
		'filter': filter
	}
	
	$.ajax({
		url: './server/getThread_FilterMostRecent.cgi',
		type: 'GET',
		data: dataPass,

		success: function(data) {
			window.filterRecentData = $.parseJSON(data);

			var section = $("section");

			for (window.increment = 0; window.increment < window.filterRecentData.length; ++window.increment) {
			
			    section.append(window.questionData);
				$('.text p').last().html(window.filterRecentData[window.increment]['title']);
				$('.userName a').last().html(window.filterRecentData[window.increment]['username_fk']);
				$('.fadebg').last().html(window.filterRecentData[window.increment]['game_fk']);
				$('.views .top').last().html(window.filterRecentData[window.increment]['score']);
				$('.answers .top').last().html(window.filterRecentData[window.increment]['answercount']);

				var date = new Date(window.filterRecentData[window.increment]['timestamp']);
				var dateNow = new Date();

				var diff = (dateNow.getTime() - date.getTime()) / 1000;

				if (diff < 61) {
					$('.time').last().html( parseInt( diff ) + " s");
				} else if (diff < 7200) {
					$('.time').last().html( parseInt( diff / 60 ) + " mins");
				} else if (diff < 172800) {
					$('.time').last().html( parseInt( diff / 3600) + " hrs");
				} else {
					$('.time').last().html( parseInt( diff / 86400) + " days");
				}
			}

			$('.questionSummary').click(function() {
				window.location = "./thread.php?id=" + window.filterRecentData[$(this).index() - 1]['id_pk'];
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