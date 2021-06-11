document.addEventListener('DOMContentLoaded', function () {
        let formContacto = document.querySelector('#formContacto');
        if (formContacto != null) {
            $(formContacto).on('submit', function (e) {
                e.preventDefault();
                let form_data = $(this).serializeArray();
                document.getElementById('mb-3').innerHTML = "<div class='loading' id='loading'>Cargando..</div>";
                $.ajax({
                    url: 'http://127.0.0.1:8000/contact/',
                    type: 'POST',
                    data: form_data,
                    dataType: 'json'
                }).done(function (data) {
                    setTimeout(function(){
                        let loading = document.getElementById('loading');
                        if (data['status']){
                            loading.remove()
                            setTimeout(function(){
                                document.getElementById('mb-3').innerHTML = '<div class= "sent-message" id="sent-message">'+data['message']+'</div>';
                                setTimeout(function(){
                                    let sent_message = document.getElementById('sent-message');
                                    sent_message.remove();
                                },2000);
                            },2000);
                            document.getElementById('formContacto').reset();
                        }else{
                            mensaje_json('error','Oops..',data['message']);
                            loading.remove();
                        }
                    },1000);
                }).fail(function (jqXHR, textStatus, errorThrown) {
                    console.log(textStatus, errorThrown);
                })
            })
        }
    },
    false);