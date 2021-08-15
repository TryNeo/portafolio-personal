$(function(){
    const fieldsToValidate = ['name','last_name','work','photo','business']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=name]')){
            let value= $(el).val()

            if (!validateStringLength(value,2)){
                return 'El nombre '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El nombre '+value+' contiene caracteres especiales o numeros';
            }
        }
       
        if($(el).is('[name=last_name]')){
            let value= $(el).val()

            if (!validateStringLength(value,2)){
                return 'El apellido '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El apellido '+value+' contiene caracteres especiales o numeros';
            }
        }

        if($(el).is('[name=work]')){
            let value= $(el).val()

            if (!validateStringLength(value,2)){
                return 'El trabajo '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El trabajo '+value+' contiene caracteres especiales o numeros';
            }
        }
       
        if($(el).is('[name=business]')){
            let value= $(el).val()

            if (!validateStringLength(value,2)){
                return 'La empresa'+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'La empresa '+value+' contiene caracteres especiales o numeros';
            }
        }
       
    }
    sendingDataServerSide('#fntClientCreate',validatorServerSide,fieldsToValidate,true,table_client);
    sendingDataServerSide('#fntClientUpdate',validatorServerSide,fieldsToValidate,true,table_client);
    deleteDataofServerSide('#fntClientDelete',true,table_client);
});