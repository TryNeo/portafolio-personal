$(function(){
    const fieldsToValidate = ['project_url','backgroud_image','description','title',
    'subtitle','client','preview_image_one','preview_image_two','preview_image_three']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=title]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El titulo '+value+' debe ser mas largo';
            }

            if (!validString(value)){
                return 'El titulo '+value+' contiene caracteres especiales o numeros';
            }
            
            
        }


        if($(el).is('[name=description]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'La descripcion debe ser mas largo';
            }
        }

        if($(el).is('[name=subtitle]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El subtitulo '+value+' debe ser mas largo';
            }

            if (!validString(value)){
                return 'El subtitulo '+value+' contiene caracteres especiales o numeros';
            }
            
        }



        if($(el).is('[name=client]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El nombre del cliente '+value+' debe ser mas largo';
            }

            if (!validString(value)){
                return 'El nombre del cliente '+value+' contiene caracteres especiales o numeros';
            }
            
        }


        if($(el).is('[name=project_url]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El URL '+value+' debe ser mas largo';
            }
        }

        if($(el).is('[name=backgroud_image]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El URL '+value+' debe ser mas largo';
            }
        }

        if($(el).is('[name=preview_image_one]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El URL '+value+' debe ser mas largo';
            }
        }

        if($(el).is('[name=preview_image_two]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El URL '+value+' debe ser mas largo';
            }
        }

        if($(el).is('[name=preview_image_three]')){
            let value= $(el).val()

            if (!validateStringLength(value,5)){
                return 'El URL '+value+' debe ser mas largo';
            }
        }
    }
    sendingDataServerSide('#fntPortfolioCreate',validatorServerSide,fieldsToValidate,true,table_portfolio);
    sendingDataServerSide('fntPortfolioUpdate',validatorServerSide,fieldsToValidate,true,table_portfolio);
});