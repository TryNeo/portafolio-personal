$(function(){

    const fieldsToValidate = ['name']
    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){
        if($(el).is('[name=description]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'La descripcion debe ser mas largo';
            }
        }


    }
    sendingDataServerSide('#fntDetailItemCreate',validatorServerSide,fieldsToValidate,true,table_item);
    sendingDataServerSide('#fntDetailItemUpdate',validatorServerSide,fieldsToValidate,true,table_item);
    deleteDataofServerSide('#fntResumeItemDelete',true,table_item);
});
