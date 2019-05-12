$(document).ready( function() {
	$.ajax({
		url: 'reply.php',
		type: 'GET',

		success: function(data) {
			window.replyData = data;
		},

		error: function() {
			console.log("Thread: Error");
		},

		complete: function() {
			console.log("Thread: Complete");
		}
	});
})

var dataPass = {
	"id_pk" : getURLParameter("id")
};

$.ajax({
	url: './server/getThread.cgi',
	type: 'GET',
	data: dataPass,

	success: function(data) {

		var dataParsed = $.parseJSON(data);

		$('#threadTitle').html(dataParsed[0]['title']);
		$('#question #body p').html(dataParsed[0]['body']);
		$('#question #score p').html(dataParsed[0]['score']);
		$('#question img').attr("src", dataParsed[0]['avatar']);

		var x = new Date(dataParsed[0]['timestamp']);



		var userInfoStr = "Posted on " + 
				x.toDateString() + 
				" at " +
				x.toTimeString().substring(0, 8) +
				" by '" +
				dataParsed[0]['username_fk'] + "'";

		
		$('#question #info p').text(userInfoStr);

		console.log("getThread: Success");
	},

	error: function() {
		console.log("getThread: Error");
	},

	complete: function() {
		console.log("getThread: Complete");
	}
});

$.ajax({
	url: './server/getReply.cgi',
	type: 'GET',
	data: dataPass,

	success: function(data) {
		console.log($.parseJSON(data));
		window.allReplies = $.parseJSON(data);

		var section = $("#replies");

		for (window.increment = 0; window.increment < window.allReplies.length; ++window.increment) {

		    section.append(window.replyData);
			$('#body p').last().html(window.allReplies[window.increment]['body']);
			$('#username p').last().html(window.allReplies[window.increment]['username_fk']);
			$('#replies img').last().attr("src", window.allReplies[window.increment]['avatar']);

			
			var date = new Date(window.allReplies[window.increment]['timestamp']);
			var dateNow = new Date();

			var diff = (dateNow.getTime() - date.getTime()) / 1000;

			if (diff < 61) {
				$('#time p').last().html( parseInt( diff ) + " s");
			} else if (diff < 7200) {
				$('#time p').last().html( parseInt( diff / 60 ) + " mins");
			} else if (diff < 172800) {
				$('#time p').last().html( parseInt( diff / 3600) + " hrs");
			} else {
				$('#time p').last().html( parseInt( diff / 86400) + " days");
			}
		}

		console.log("getReply: Success");
	},

	error: function() {
		console.log("getReply: Error");
	},

	complete: function() {
		console.log("getReply: Complete");
	}
});