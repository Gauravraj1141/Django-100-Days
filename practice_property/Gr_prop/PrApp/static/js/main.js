function getCities() {
    var state_id = $('#id_State_name').val();
    $.ajax({
        url: '/get-cities/',
        data: {
            'state_id': state_id
        },
        success: function (data) {
            $('#id_City_name').empty();
            $.each(data, function (key, city) {
                console.log(data)
                for (const i in city) {
                    console.log(city[i])
                    $('#id_City_name').append(`<option value="${city[i].ct_id}">${city[i].ctname}</option>`);
                }
            });
        }
    });
}


// Get the alert element
var alert = document.getElementById("alert");

// Set a timeout to remove the alert after 3 seconds

if (alert) {
    setTimeout(function () {
        alert.style.display = "none";
    }, 2000);
}