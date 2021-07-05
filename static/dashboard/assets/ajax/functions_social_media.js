let table_social_media;
$(function() {
    table_social_media = $('.tableSocialMedia').DataTable({
        "aProcessing":true,
        "aServerSide":true,
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
                    let base_opcion = '<ul class="d-flex justify-content-center">'+
                    '<li class="mr-3"><button type="button" onclick=abrir_modal("#popup","'+url_edit+'"); class="close text-secondary"><i class="fa fa-edit"></i></button></li></ul>';
                    return base_opcion;
                }

            }
        ], 
        "order":[[0,"desc"]]
    });

    let formSocialMedia = document.querySelector('#fntSocialMediaCreate');

    if (formSocialMedia != null) {
        let url = $(formSocialMedia).attr("action");
        $(formSocialMedia).on('submit', function (e) {
            e.preventDefault();
            let form_data = $(this).serializeArray();
            $.ajax({
                url: url,
                type: 'POST',
                data: form_data,
                dataType: 'json'
            }).done(function (data) {
                $('#popup').modal('hide');
                mensaje('success','Exitoso',data['message']);
                table_social_media.ajax.reload();
            }).fail(function (error) {
                mensaje_json('error','Campos no validos',error.responseJSON['message']);
            })
        })
    }

});