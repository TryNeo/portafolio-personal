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
        ],
        "columnDefs":[
            {
                targets:[2],
                orderable:false,
                render:function(data,type,row){
                    return '<i class="'+row.icon+'"></i>'
                }
            }
        ],
        "order":[[0,"desc"]]
    });

    table_social_media.ajax.reload();
});