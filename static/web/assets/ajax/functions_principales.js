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
 * Funciona que obtiene los eventos cada vez que un input es aplastado
 * @param {String} tagName - recibe un selector de clase o id
 * @param {function} funciontValidate - recibe una funcion la cual actuara como intermediario para la validacion
 * 
 */

function validateForm(inputSelector,functionValidate){
    inputSelector.forEach((input) => {
        input.addEventListener('keyup',functionValidate);
        input.addEventListener('blur',functionValidate);
    });
}


function showColorsInput(tagSelector,tagId,name_one,name_two){
    $(tagSelector).removeClass(name_one);
    $(tagId).removeClass(name_one);
    $(tagSelector).addClass(name_two);
    $(tagId).addClass(name_two);
}



function validateEmptyField(value, tagSelector,tagId){
    valid = false;
    if (value === ''){
        showColorsInput(tagSelector,tagId,'success','error');
        valid = false;
    }else{
        showColorsInput(tagSelector,tagId,'error','success');
        valid = true;
    }
    return valid;
}



// IGNORAR ESTAS LINEAS DE CODIGOS - EN PROCESO DE CONSTRUCION O NO.

/*
*    campsList = {
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
*/

