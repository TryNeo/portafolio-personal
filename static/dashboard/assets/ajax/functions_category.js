$(function(){
    const fieldsToValidate = ['name']

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
       
    }
    sendingDataServerSide('#fntCategoryCreate',validatorServerSide,fieldsToValidate,true,table_category);
    sendingDataServerSide('#fntCategoryUpdate',validatorServerSide,fieldsToValidate,true,table_category);
    deleteDataofServerSide('#fntCategoryDelete',true,table_category);

});