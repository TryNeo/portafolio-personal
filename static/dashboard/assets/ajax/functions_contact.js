$(function() {

    const fieldsToValidate = ['icon','title','description']

 
    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });

    validatorServerSide.validator.custom = function(el, event){
   
        if($(el).is('[name=icon]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El nombre de icono '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El nombre del icono '+value+' contiene caracteres especiales o numeros';
            }
        }

        if($(el).is('[name=title]')){
            let value = $(el).val()

            if (!validateStringLength(value,5)){
                return 'El nombre del titulo '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El nombre del titulo '+value+' contiene o numeros';
            }
        }

        if($(el).is('[name=description')){
            let value = $(el).val()

            if (!validateStringLength(value,5)){
                return 'La descripcion '+value+' debe ser mas largo';
            }
        }
    }

    sendingDataServerSide('#fntContactCreate',validatorServerSide,fieldsToValidate)
    sendingDataServerSide('#fntContactUpdate',validatorServerSide,fieldsToValidate)
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