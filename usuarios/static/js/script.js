//VALIDACION micuenta.html FORMULARIO HTML
//VALIDACION micuenta.html FORMULARIO HTML

function Ingreso(){
    var user,password,chk,txt;
    
    user = document.getElementById("username").value;
    password = document.getElementById("pwd").value;
    chk = document.getElementById("chkHtml").checked;
    
    //USUARIO
    if (user.length == 0){
        txt = 'Usuario no debe estar vacío';
    }else{
        txt = "";
    }
    document.getElementById("valida_usuario").innerHTML = txt;

    //CONTRASEÑA
    if (password.length == 0){
        txt = "Escriba una contraseña"; 
    }else if (password.length > 1 && password.length < 6){
        txt = "La contraseña es muy corta";
    }else{
        txt ="";
    }
    document.getElementById("valida_contraseña").innerHTML = txt;

    
    //CHECKBOX
    if (!chk){
        txt = "Sesion no recordada";
    }else{
        txt = "";
    }
    document.getElementById("valida_checkbox").innerHTML = txt;
    
}

//VALIDACION formRegistro.html FORMULARIO HTML Y CSS
//VALIDACION formRegistro.html FORMULARIO HTML Y CSS
function Registro(){
    var expRegNombre=/^[a-zA-ZÑñÁáÉéÍíÓóÚúÜü\s]+$/;
    var expRegApellidos=/^[a-zA-ZÑñÁáÉéÍíÓóÚúÜü\s]+$/;
    var expRegCorreo=/^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/; 
    var expRegCon = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]).{8,}$/;
    
       var nombre = document.getElementById("nombres");
       var apellidos = document.getElementById("apellidos");
       var correo = document.getElementById("correoHtml");
       var password1 = document.getElementById("password1");
       var password2 = document.getElementById("password2");

       if(!nombre.value)
       {
        txt = "El campo nombre es requerido";
        
       }
       else if (!expRegNombre.exec(nombre.value))
       {
        txt = "El campo nombre admite letras y espacios."
        
       }else{
        txt = "";
        
       }
       document.getElementById("errorNombre").innerHTML = txt;

       //Campo apellido
       if(!apellidos.value)
       {
        txt = "El campo apellido es requerido";
        
       }
       else if(!expRegApellidos.exec(apellidos.value))
       {
        txt = "El campo apellidos admite letras y espacios.";
         
       }else{
        txt = "";
        
       }
       document.getElementById("errorApellido").innerHTML = txt;
  
       //campo email
       if(!correo.value)
       {
        txt = "El campo correo es requerido";
        
       }
       else if(!expRegCorreo.exec(correo.value))
       {
        txt = "El campo correo no tiene el formato correcto.";
        
       }else{
        txt = "";
        
       }
       document.getElementById("errorCorreo").innerHTML = txt;

       //campo contraseña 1
       if(!password1.value){
        txt = "El campo contraseña es requerido"
        
       }
       else if(!expRegCon.exec(password1.value)){
        txt = "El campo contraseña no tiene el formato correcto.";
        
       }else{
        txt = "";
        
       }
       document.getElementById("errorPass1").innerHTML = txt;

       //campo contraseña 2 y validación ambas contraseñas
       if(!password2.value){
        txt = "Reingrese su contraseña"
        
       }
       else if(password1.value != password2.value){
        txt = "Las contraseñas no coinciden";
        
       }else{
        txt = "";
       }
       document.getElementById("errorPass2").innerHTML = txt;

       //si todo esta correcto se envia el form
       if (txt === "") {
        document.getElementById("formRegistro").submit();
      }
       }
      
      
      
       
       
       
