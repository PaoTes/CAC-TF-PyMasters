//alert(location)  // http://127.0.0.1:5500/src/update.html?id=1&nombre=Focaccia&email=1500&prioridad=15
//alert(location.search)  // devuelve de la URL desde el ? , muestra "?id=1&nombre=Focaccia&email=1500&prioridad=15"
//alert(location.search.substr(1))  // devuelve de la URL a partir del ? , muestra "id=1&nombre=Focaccia&email=1500&prioridad=15"

var args = location.search.substr(1).split('&');
//alert(args)
 
// args='id=1,nombre=Focaccia,email=1500,prioridad=15'
console.log(args)
// lee los argumentos pasados a este formulario
var parts = []
for (let i = 0; i < args.length; ++i) {
    parts[i] = args[i].split('=');
    console.log(parts[i])
}


//Para mostrar
document.getElementById("txtNombre").innerHTML= decodeURIComponent(parts[1][1]);
document.getElementById("txtDescripcion").innerHTML = decodeURIComponent(parts[2][1]);
document.getElementById("txtPrecio").innerHTML = decodeURIComponent(parts[3][1]);
document.getElementById("txtMarca").src = parts[4][1];
document.getElementById("txtImagen").innerHTML = decodeURIComponent(parts[5][1]);

var fondoFoto = document.getElementById("txtImagen").src;
function verFoto(){
    if (fondoFoto!=""){
        document.querySelector("#imgPreview").style.display="inline-block";
        document.querySelector("#imgPreview").src = fondoFoto;
    }else{
        document.querySelector("#imgPreview").style.display="none";
    }
   };
function mostrarHeader(){
 var imagen = document.querySelector(".contenedor-header-foto");
 imagen.style.backgroundImage = `url(${fondoFoto})`;
 imagen.style.backgroundSize = "cover";
 imagen.style.backgroundPosition = "center";
};

//Para modificar en el formulario
document.getElementById("txtId").value = parts[0][1];
document.getElementById("txtNombre").value = decodeURIComponent(parts[1][1]);
document.getElementById("txtDescripcion").value = decodeURIComponent(parts[2][1]);
document.getElementById("txtPrecio").value = parts[3][1];
document.getElementById("txtMarca").value = decodeURIComponent(parts[4][1]);
document.getElementById("txtImagen").value = decodeURIComponent(parts[5][1]);



function modificar() {
    let i = document.getElementById("txtId").value;
    let n = document.getElementById("txtNombre").value;
    let m = document.getElementById("txtMarca").value;
    let p = parseFloat(document.getElementById("txtPrecio").value);
    let im = document.getElementById("txtImagen").value;
    let des =document.getElementById("txtDescripcion").value;
    des =  decodeURIComponent(des);
    document.querySelector("#imgPreview").style.display="inline-block";
    document.querySelector("#imgPreview").src = im;
    let usuario = {
        id:i,
        nombre: n,
        ubicacion: m,
        prioridad: p,
        imagen: im,
        descripcion: des
    }
    let url = "http://localhost:8080/usuarios"
    var options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al Modificar")
        })      
}
