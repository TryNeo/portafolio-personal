$(function(){
    const fieldsToValidate = ['name','icon','social_url']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){
        console.log(el)
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
        
        
        if($(el).is('[name=social_url]')){
            let value= $(el).val()
            if (!validateStringLength(value,5)){
                return 'El URL '+value+' debe ser mas largo';
            }
        }
    }
    sendingDataServerSide('#fntSocialMediaCreate',validatorServerSide,fieldsToValidate,true,table_social_media);
    sendingDataServerSide('#fntSocialMediaUpdate',validatorServerSide,fieldsToValidate,true,table_social_media);
    deleteDataofServerSide('#fntSocialMediaDelete',true,table_social_media);

});