$(function(){
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
    sendingDataServerSide('#fntServiceCreate',validatorServerSide,fieldsToValidate,true,table_service);
    sendingDataServerSide('#fntServiceUpdate',validatorServerSide,fieldsToValidate,true,table_service);
    deleteDataofServerSide('#fntServiceDelete',true,table_service);
});