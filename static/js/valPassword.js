function validar()
{
    var nombreUsuario = document.formulariouser_profile.usuario;
    var claveInput = document.formulariouser_profile.clave;
    //var correoInput = document.formularioRegistro.correo;

    /*var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;*/

    var swErrores=false;

    console.log(nombreUsuario.value + "-"+claveInput.value);

    if(nombreUsuario.value.length == 0 || nombreUsuario.value.length < 8)
    {
        document.getElementById("errorusuario").innerHTML="El nombre de usuario debe tener mínimo 8 caracteres.";
        nombreUsuario.focus();
        swErrores=true;
    }

    if(claveInput.value.length == 0 || claveInput.value.length < 8)
    {
        document.getElementById("errorClave").innerHTML="La clave debe tener mínimo 8 caracteres.";
        claveInput.focus();
        swErrores=true;
    }

    if( swErrores==true)
    {
        return false;
    }
    else{
        return true;
    }

}
