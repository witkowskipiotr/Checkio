

$(document).ready(function () {
function searchOpen() {
    var search = $('#id_username').val();
    $.ajax({
        url: '/ajax/person_new/name/',
        dataType: 'json',
        type: 'GET',
        data: {
            name: search
        },

        success: function (data) {
            $( "#id_username" ).autocomplete ({
                source: data.source
            });
        },
        error: function () {
            console.log('error');
        }

    });
}




  $("#id_username").on('keyup', function () {
    searchOpen();
  });
});
