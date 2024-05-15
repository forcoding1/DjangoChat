// scripts.js

$(document).ready(function() {
    setInterval(function() {
        $.ajax({
            type: 'GET',
            url: "/getMessages/" + roomName + "/",
            success: function(response) {
                console.log(response);
                $("#display").empty();
                response.messages.forEach(function(message) {
                    var temp = "<div class='container darker'><b>" + message.user + "</b><p>" + message.value + "</p><span class='time-left'>" + message.date + "</span></div>";
                    $("#display").append(temp);
                });
            },
            error: function(response) {
                alert('An error occurred');
            }
        });
    }, 1000);
});

$(document).on('submit', '#post-form', function(e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '/send',
        data: {
            username: $('#username').val(),
            room_id: $('#room_id').val(),
            message: $('#message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(data) {
            // Optionally alert data or perform any success action
        }
    });
    $('#message').val('');
});
