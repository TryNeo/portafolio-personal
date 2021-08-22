$(function(){
    const fieldsToValidate = ['username','password']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=username]')){
            let value= $(el).val()

            if (!validateUser(value)){
                return 'El usuario ingresado no es valido';
            }
            
        }

        if($(el).is('[name=password]')){
            let value= $(el).val()

            if (!validateUser(value)){
                return 'La contraseña ingresada no es valido';
            }
            
        }
       
    }

});