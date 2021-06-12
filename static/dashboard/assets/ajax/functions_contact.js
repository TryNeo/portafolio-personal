document.addEventListener('DOMContentLoaded', function () {
        $('.tarjetContact').on('click', function () {
            $('input[name="action"]').val('add');
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
                        mensaje('success','Exitoso',data['message']);
                    } else {
                        mensaje_json('error', 'Oops..', data['message']);
                    }
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                })
            })
        }

    },
    false);