var sesion;
var botonLogin = document.querySelector(".boton-login");
var contenedorLogin=document.querySelector(".container-login");
var contenedorListado=document.querySelector(".container-listado");
var botonSesion=document.querySelector("#boton-sesion");
function validarSesion(){
  localStorage.setItem("sesion", 1);
document.getElementById("boton-sesion").href = "admin.html";
}
function cerrarSesion() {
  localStorage.setItem("sesion", 0);
  document.getElementById("irAdmin").href = "admin.html";
}


// capturando eventos con aaddEventLisener
botonLogin.addEventListener("click", function(event){ //funcion anonima, que se utiliza solamente una vez en un componente
    event.preventDefault();//En el caso del boton, evita que se recargue
    var usuario = document.querySelector("#txtEmail").value;
    var contrasena = document.querySelector("#txtPassword").value;
    
    if (usuario==="Admin" && contrasena==="secretKey"){
      mostrarListado();
      alert("Admin: Bienvenido al Sistema!!");
    }else{
        alert("Error: El Usuario o la Contraseña no son válidos ");
    }
});



function mostrarListado(){
  contenedorLogin.style.display="none";
  contenedorListado.style.display="block";
}

function ocultarListado(){
  contenedorLogin.style.display="block";
  contenedorListado.style.display="none";
}

var valorSesion=localStorage.getItem("sesion");


function ver(){
  if (valorSesion==1){ 
    mostrarListado();
  }else{
    ocultarListado();
  }
 }