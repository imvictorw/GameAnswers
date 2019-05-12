var profile;
$(document).ready(function () {
    profilepic();
    usernamebar();
});

function profilepic() {
    profile = $('<img>').attr({
        'src': 'img/defaultAvatar.png',

    });
    $('#profilepic').append(profile);
}

function usernamebar() {
    var x = Math.round($(window).width());
    $('#username').css({

        'width': x + 'px',
    });
}