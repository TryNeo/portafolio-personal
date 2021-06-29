$(function() {
    
    let formContact = document.querySelector('#fntContactCreate');
    let inputFormat = document.querySelectorAll('#fntContactCreate input')
    
    campsList = {
        'resultado':false,
    }
    
    const validateData = (e) => {
        switch (e.target.name) {
            case 'icon':
                campsList['resultado'] = validateEmptyField(e.target.value,'#id_icon','#icon');
            break;
            case 'title':
                campsList['resultado'] = validateEmptyField(e.target.value,'#id_title','#title');
            break;
        }
    }

    validateForm(inputFormat,validateData);

    if (formContact != null) {
        let url = $(formContact).attr("action");
        $(formContact).on('submit', function (e) {
            e.preventDefault();
            if (campsList['resultado']){
                let form_data = $(this).serializeArray();
                $.ajax({
                    url: url,
                    type: 'POST',
                    data: form_data,
                    dataType: 'json'
                }).done(function (data) {
                    alert("hello")
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                })
            }else{
                mensaje("error","Campos invalidos",'Los campos no son validos')
            }
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