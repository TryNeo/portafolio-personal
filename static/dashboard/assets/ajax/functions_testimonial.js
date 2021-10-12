$(function(){
    const fieldsToValidate = ['commentary']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });
    validatorServerSide.validator.custom = function(el, event){

        if($(el).is('[name=commentary]')){
            let value= $(el).val()

            if (!validateStringLength(value,40)){
                return 'El comentario '+value+' debe ser mas largo';
            }
            
        }
    }
    sendingDataServerSide('#fntTestimonialCreate',validatorServerSide,fieldsToValidate,true,table_testimonial);
    sendingDataServerSide('#fntTestimonialUpdate',validatorServerSide,fieldsToValidate,true,table_testimonial);
    deleteDataofServerSide('#fntTestimonialDelete',true,table_testimonial);

});