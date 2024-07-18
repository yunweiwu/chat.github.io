$(document).ready(function() {
    $('#loginForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/login',
            method: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                if (response.success) {
                    $('#loginForm').hide();
                    $('#chatArea').show();
                    $('#loggedInUser').text(response.username);
                } else {
                    alert('Invalid username or password');
                }
            }
        });
    });

    $('#sendMessageForm').on('submit', function(e) {
        e.preventDefault();
        var message = $('#messageInput').val();
        $.ajax({
            url: '/send_message',
            method: 'POST',
            data: {username: $('#loggedInUser').text(), message: message},
            success: function(response) {
                if (response.success) {
                    $('#messageInput').val('');
                    loadMessages();
                } else {
                    alert('Error sending message');
                }
            }
        });
    });

    function loadMessages() {
        $.ajax({
            url: '/get_messages',
            method: 'GET',
            success: function(response) {
                var messages = response.messages;
                var html = '';
                for (var i = 0; i < messages.length; i++) {
                    html += '<p><strong>' + messages[i].username + ':</strong> ' + messages[i].message + '</p>';
                }
                $('#messages').html(html);
            }
        });
    }

    $('#loadMoreMessages').on('click', function() {
        // Implement logic to load more messages when this button is clicked
    });
});
