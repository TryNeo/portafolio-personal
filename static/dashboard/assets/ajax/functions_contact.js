document.addEventListener('DOMContentLoaded', function () {
        $('.tarjetContact').on('click', function () {
            $('input[name="action"]').val('add');
            $('.modal-title').find('span').html('Creacion de Tarjeta Contacto')
            document.getElementById('formContact').reset();
            $('#ContactModal').modal('show');
        })
        let formContacto = document.querySelector('#formContact');
        if (formContacto != null) {
            $(formContacto).on('submit', function (e) {
                e.preventDefault();
                let form_data = $(this).serializeArray();
                $.ajax({
                    url: 'http://127.0.0.1:8000/dashboard/contact/',
                    type: 'POST',
                    data: form_data,
                    dataType: 'json'
                }).done(function (data) {
                    if (data['status']) {
                        $('#ContactModal').modal('hide');
                        document.getElementById('formContact').reset();
                        mensaje('success', 'Exitoso', data['message']);
                    } else {
                        mensaje_json('error', 'Oops..', data['message']);
                    }
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                })
            })
        }

        $('.btnEdit').on('click', function (e) {
            e.preventDefault();
            let id_contact = $(this).attr('rel')
            let data = {'action': 'load_data', 'id_contact': id_contact};
            $.ajax({
                url: 'http://127.0.0.1:8000/dashboard/contact/',
                type: 'POST',
                data: data,
            }).done(function (data) {
                if (data['status']) {
                    $('.modal-title').find('span').html('Edicion de Tarjeta Contacto')
                    $('input[name="action"]').val('edit');
                    $('input[name="id_contact"]').val(data['message']['id_contact']);
                    $('input[name="icon"]').val(data['message']['icon']);
                    $('input[name="title"]').val(data['message']['title']);
                    $('textarea[name="description"]').val(data['message']['description']);
                    $('#ContactModal').modal('show');
                } else {
                    mensaje_json('error', 'Oops.. lo siento', data['message']);
                }
            }).fail(function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            })
        })

     $('.btnDelete').on('click', function (e) {
            e.preventDefault();
            let id_contact = $(this).attr('rel')
            let data = {'action': 'delete', 'id_contact': id_contact};
            $.ajax({
                url: 'http://127.0.0.1:8000/dashboard/contact/',
                type: 'POST',
                data: data,
            }).done(function (data) {
                if(data['status']){
                    mensaje('success','Exitoso',data['message'])
                    setTimeout(function(){
                        location.reload()
                    },2000)
                }
            }).fail(function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            })
        })

    },
    false);


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