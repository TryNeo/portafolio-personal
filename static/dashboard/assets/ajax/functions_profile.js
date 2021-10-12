$(function(){
    const fieldsToValidate = ['first_name','last_name','username','email']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=first_name]')){
            let value= $(el).val()
            if (!validateStringLength(value,5)){
                return 'El nombre '+value+' debe ser mas largo';
            }

            if (!validString(value)){
                return 'El nombre '+value+' contiene caracteres especiales';
            }

            
        }

        if($(el).is('[name=last_name]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El apellido '+value+' debe ser mas largo';
            }

            if (!validString(value)){
                return 'El apellido '+value+' contiene caracteres especiales';
            }
        }

        if($(el).is('[name=email]')){
            let value= $(el).val()

            if (!validateEmail(value)){
                return 'El email '+value+'ingresado no es valido';
            }
            
        }


        if($(el).is('[name=username]')){
            let value= $(el).val()

            if (!validateUser(value)){
                return 'El usuario ingresado no es valido';
            }
            
        }
    }

});