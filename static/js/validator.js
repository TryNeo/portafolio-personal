class Validator{
    constructor(nameForm,nameField){
        this.nameForm = nameForm;
        this.nameField = nameField;
        this.validator = $(this.nameForm).jbvalidator({
            errorMessage: true,
            successClass: true,
        });
    }

    validatorServer(){
        this.validator.validator.custom = function(el, event){
            if($(el).is('[name='+this.nameField+']')){
                let value = $(el).val();
                if (!validateStringLength(value,5)){
                    return 'El nombre de icono '+value+' debe ser mas largo';
                }
                
                if(!validString(value)){
                    return 'El nombre del icono '+value+' contiene caracteres especiales o numeros';
                }     
            }
        };
    }    
}

