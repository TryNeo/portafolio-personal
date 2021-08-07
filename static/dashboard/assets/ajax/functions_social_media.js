$(function() {

    let table_social_media = $('.tableSocialMedia').DataTable({
        "aProcessing":true,
        "aServerSide":true,
        "paginate":false,
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningun dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "<span class='fa fa-angle-double-left'></span>",
                "sLast": "<span class='fa fa-angle-double-right'></span>",
                "sNext": "<span class='fa fa-angle-right'></span>",
                "sPrevious": "<span class='fa fa-angle-left'></span>"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        "responsive":true,
        "destroy": true,
        "ajax":{
            "url" :url_social,
            "dataSrc":""
        },
        "columns":[
            {"data":"id_social_media"},
            {"data":"name"},
            {"data":"icon"},
            {"data":"social_url"},
            {"data":"opciones"}
        ],
        "columnDefs":[
            {
                targets:[2],
                orderable:false,
                render:function(data,type,row){
                    return '<i class="'+row.icon+'"></i>'
                }
            },
            {
                targets:[4],
                orderable:false,
                render:function(data,type,row){
                    let url_edit = url_social+"edit/"+row.id_social_media
                    let base_opcion = '<div class="d-flex justify-content-center">'+
                    '<a href="#" class="text-primary"><i class="fa fa-edit"></i></a>'+
                    '<a href="#" class="text-danger"><i class="fa fa-trash"></i></a></div>';
                    // let base_opcion = '<button type="button" onclick=abrir_modal("#popup","'+url_edit+'"); class="close text-secondary"><i class="fa fa-edit"></i></button>'
                    return base_opcion;
                }

            }
        ], 
        "order":[[0,"desc"]]
    });


    const fieldsToValidate = ['name','icon','social_url']

    let validatorServerSide = $('form.needs-validation').jbvalidator({
        errorMessage: true,
        successClass: true,
    });


    validatorServerSide.validator.custom = function(el, event){
   
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
   
    sendingDataServerSide('#fntSocialMediaCreate',validatorServerSide,fieldsToValidate,true,table_social_media)

});