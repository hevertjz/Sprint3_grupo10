var password = document.formRegistro.password;

var passid_len = password.value.length;
  if (passid_len == 0 || passid_len < 8) {
    alert("Debes ingresar una password con mas de 8 caracteres");
    passid.focus();
  }

function mostrarPassword(obj) {
  var obj = document.getElementById("password");
  obj.type = "text";
}
function ocultarPassword(obj) {
  var obj = document.getElementById("password");
  obj.type = "password";
}