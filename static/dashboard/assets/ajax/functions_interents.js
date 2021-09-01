$(function(){
    const fieldsToValidate = ['name','icon']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=name]')){
            let value= $(el).val()
            if (!validateStringLength(value,5)){
                return 'El nombre del titulo '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El nombre del titulo '+value+' contiene caracteres especiales o numeros';
            }
        }
        if($(el).is('[name=icon]')){
            let value= $(el).val()
            if (!validateStringLength(value,5)){
                return 'El nombre del icono '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El nombre del icono '+value+' contiene caracteres especiales o numeros';
            }
        }
    }
    sendingDataServerSide('#fntInterentCreate',validatorServerSide,fieldsToValidate,true,table_interents);
    sendingDataServerSide('#fntInterentUpdate',validatorServerSide,fieldsToValidate,true,table_interents);
    deleteDataofServerSide('#fntInterentDelete',true,table_interents);

});