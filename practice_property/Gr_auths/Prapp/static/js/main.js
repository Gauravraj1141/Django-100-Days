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