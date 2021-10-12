$(function(){
    const fieldsToValidate = ['name_skill','percentage']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=name_skill]')){
            let value= $(el).val()

            if (!validateStringLength(value,2)){
                return 'La Habilidad '+value+' debe ser mas largo';
            }
            
            if(!validString(value)){
                return 'La Habilidad'+value+' contiene caracteres especiales o numeros';
            }
        }

        if($(el).is('[name=percentage]')){
            let value= $(el).val()

            if (!validateNumbers(value)){
                return 'El porcentaje '+value+' debe ser un numero';
            }

        }
    }
    sendingDataServerSide('#fntSkillCreate',validatorServerSide,fieldsToValidate,true,table_skill);
    sendingDataServerSide('#fntSkillUpdate',validatorServerSide,fieldsToValidate,true,table_skill);
    deleteDataofServerSide('#fntSkillDelete',true,table_skill);

});