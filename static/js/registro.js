function validar()
{
    var nombreInput = document.formularioRegistro.nombre;
    var apellidoInput = document.formularioRegistro.apellido;
    var usuarioInput = document.formularioRegistro.usuario;
    var claveInput = document.formularioRegistro.clave;
    var correoInput = document.formularioRegistro.correo;
    var confirmCorreoInput = document.formularioRegistro.comprobar_correo;
    

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;

    var swErrores=false;



    if(nombreInput.value.length == 0 || apellidoInput.value.length == 0)
    {
        document.getElementById("errorNombre").innerHTML=" \n Por favor ingrese su nombre.";
        nombreInput.focus();
        swErrores=true;
    }


    if(usuarioInput.value.length == 0 || usuarioInput.value.length < 4)
    {
        document.getElementById("errorusuario").innerHTML="El nombre de usuario debe tener mínimo 8 caracteres.";
        usuarioInput.focus();
        swErrores=true;
    }

    if(claveInput.value.length == 0 || claveInput.value.length < 8)
    {
        
        document.getElementById("errorClave").innerHTML="La clave debe tener mínimo 8 caracteres.";
        claveInput.focus();
        swErrores=true;
    }

    if(!correoInput.value.match(formato_email))
    {
        
        document.getElementById("errorMail").innerHTML="Por favor escriba un correo válido.";
        correoInput.focus();
        swErrores=true;
    }

    if(confirmCorreoInput.value != correoInput.value)
    {
        
        document.getElementById("errorMail").innerHTML="Los correos electrónicos no coinciden, por favor verifique.";
        confirmCorreoInput.focus();
        swErrores=true;
    }


    if( swErrores==true)
    {
        return false;
    }
    else{
        alert("registro exitoso")
        return true;
        
    }

}


// alert("Registro exitoso") pendiente por poner alert y redirigir al login