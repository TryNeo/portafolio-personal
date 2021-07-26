
/**
 * @const {regex} regex_string  - contiene una exprecion regular que acepta letras y espacios.
 * @const {regex} regex_numbers - contiene una exprecion regular que acepta numeros solamente.
 * @const {regex} regex_username_password - contiene una exprecion regular que acepta letras y numeros y caracteres especiales.
 */
 const regex_string = '^[a-\.-zA-ZáéíóñÁÉÍÓÚÑ ]+$';
 const regex_numbers = '^[0-9]+$';
 const regex_fechas = '^([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})$';
 const regex_username_password = '^[a-zA-Z0-9_-]{4,18}$';
 const regex_email = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$';



/**
 * Funcion mensaje - permite mostrar una alerta con la libreria swealert
 * @param  {string} icon - recibe el tipo de icono /error/success/info/warning
 * @param  {string} title - recibe el tipo de titulo a mostrar en la alertar
 * @param  {string} text - recibe el mensaje de error a mostrar
 */
 function mensaje(icon,title,text){
    Swal.fire({
        icon: icon,
        title: title,
        text: text,
    })
}

/**
 * Funcion mensaje_json - permite mostrar una alerta con la libreria swealert
 * @param  {string} icon - recibe el tipo de icono /error/success/info/warning
 * @param  {string} title - recibe el tipo de titulo a mostrar en la alertar
 * @param  {json} json - recibe el json a recorrer
 */
function mensaje_json(icon,title,json){
    let message = '<ul style="list-style:none;text-align: center;">';
    for (const dataKey in json ) {
        message+='<li>'+json[dataKey]+'</li>';
     }
    message+='</ul>';
    Swal.fire({
        icon: icon,
        title: title,
        html: message,
    })
}



/**
 * Funcion abrir_modal - permite mostrar un modal depediendo del tagName con su respectiva Url
 * @param {string} tagName - recibe un selector de clase o id
 * @param {url} UrlBase - recibe una url en especifico
 */
function abrir_modal(tagName,urlBase){
    $(tagName).load(urlBase,function(){
        $(this).modal({
        backdrop:'static',
        keyboard: false
        })
        $(this).modal('show');
    });
    
}


/**
 * @param {Selector} idForm - 
 * @param {function} validatorServerSide -
 * @param {list} fieldsToValidate - 
 */
function sendingDataServerSide(idForm,validatorServerSide,fieldsToValidate){
    let url = $(idForm).attr("action");
    $(document).on('submit',idForm,function (e) {
        e.preventDefault();
        let formData = $(this).serializeArray();
        $.ajax({
            url: url,
            type: 'POST',
            data: formData,
            dataType: 'json'
        }).done(function (data) {
            $('#popup').modal('hide');
            mensaje('success','Exitoso',data['message']);
        }).fail(function (error) {
            fieldsToValidate.forEach((value,index) => {
                if (error.responseJSON['message'].hasOwnProperty(fieldsToValidate[index])){
                    validatorServerSide.errorTrigger($('[name='+fieldsToValidate[index]+']'), error.responseJSON['message'][''+fieldsToValidate[index]+'']);
                }
            });
        })
    })
}


function validString(value){

}