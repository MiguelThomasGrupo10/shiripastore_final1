$(document).ready(function(){
    $("#form-contacto").validate({
        ignore:[],
        debug:false,
        rules:{
            email:{required: true, email: true},
            seleccion:{required: true},
            textoarea:{required: true},
        },
        messages:{
            email: "Se requiere completar este campo.",
            textoarea:{
                required:"Se requiere completar este campo.",
            },
            seleccion: "Debes elegir una opcion."
        }
    });
    $('#enviarform').on('click',function(){
        $("#form-contacto").valid()
    });
});


//Integracion de API
$(document).ready(function(){
    $("#enviar").click(function(){
        $.get("https://my-json-server.typicode.com/MiguelThomasGrupo10/Shiripa-Store-reborn_v1/db",
        function(data){
            $.each(data.Empresas, function(i,item){
                $("#Empresas").append("<tr><td>"+item.idEmpresa+"</td><td>"+
                item.nombre + "</td><td>" + item.annoColaboracion+ "</td><td>" +
                item.descripcion + "</td></tr>");
            });
        });
    });
});
