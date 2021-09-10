$(function(){
    const fieldsToValidate = ['title','years','description']
    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){
        if($(el).is('[name=title]')){
            let value= $(el).val()

            if (!validateStringLength(value,2)){
                return 'El nombre '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'El nombre '+value+' contiene caracteres especiales o numeros';
            }

        }

        if($(el).is('[name=years]')){
            let value= $(el).val()

            if (!validateStringLength(value,0)){
                return '';
            }
        }
        
        if($(el).is('[name=description]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'La descripcion debe ser mas largo';
            }
        }


    }
    sendingDataServerSide('#fntResumeCreate',validatorServerSide,fieldsToValidate,true,table_resume);
    sendingDataServerSide('#fntResumeDetailCreate',validatorServerSide,fieldsToValidate,true,table_resume);
    sendingDataServerSide('#fntResumeUpdate',validatorServerSide,fieldsToValidate,true,table_resume);
    sendingDataServerSide('#fntDetailResumeUpdate',validatorServerSide,fieldsToValidate);
});
