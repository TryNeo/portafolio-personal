$(function() {
    
    let formContact = document.querySelector('#fntContactCreate');
    let formContactDelete = document.querySelector('#fntContactDelete');
    // Bootstrap 4 Validation
    $(".needs-validation").submit(function() {
        var form = $(this);
        if (form[0].checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
        }
        form.addClass('was-validated');
    });

    if (formContact != null) {
        let url = $(formContact).attr("action");
        $(formContact).on('submit', function (e) {
            e.preventDefault();
            let form_data = $(this).serializeArray();
            $.ajax({
                url: url,
                type: 'POST',
                data: form_data,
                dataType: 'json'
            }).done(function (data) {
                $('#popup').modal('hide');
                mensaje('success','Exitoso',data['message']);
            }).fail(function (error) {
                mensaje_json('error','Campos no validos',error.responseJSON['message']);
            })
        })
    }

    if (formContactDelete != null) {
        let url = $(formContactDelete).attr("action");
        $(formContactDelete).on('submit', function (e) {
            e.preventDefault();
            let form_data = $(this).serializeArray();
            $.ajax({
                url: url,
                type: 'POST',
                data: form_data,
                dataType: 'json'
            }).done(function (data) {
                $('#popup').modal('hide');
                mensaje('success','Exitoso',data['message']);
            }).fail(function (error) {
                $('#popup').modal('hide');
                mensaje('error','Hubo problemas al eliminar',error);
            })
        })
    }

});

function loadingCardsContact() {
    $.ajax({
        url: 'http://127.0.0.1:8000/dashboard/contact/',
        type: 'POST',
        data: {'action': 'contact_info'},
    }).done(function (data) {
        let card_contact = ''
        for (const dataKey in data) {
            card_contact += '<div class="col-sm-12"><div class="grid-col"><div class="card card-bordered"><div class="card-body">' +
                '<div class="col-md-12"><button type="button" class="close" aria-label="Close"><span aria-hidden="true"><i class="fa fa-trash"></i></span></button>' +
                '<button type="button" class="close" aria-label="Close"><span aria-hidden="true"><i class="fa fa-edit"></i></span></button>' +
                '<div class="row">' +
                '<h3><i class=""></i>' + data[dataKey]["title"] + '</h3>' +
                '</div><p>' + data[dataKey]["description"] + '</p>' +
                '</div></div></div></div></div>';
        }
        document.getElementById('insert-card').innerHTML = card_contact;
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(textStatus, errorThrown);
    })
}