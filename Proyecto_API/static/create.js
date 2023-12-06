function habilitar(){
    document.getElementById("txtNombre").disabled = false;
    document.getElementById("txtMarca").disabled = false;
    document.getElementById("txtPrecio").disabled = false;
    document.getElementById("txtImagen").disabled = false;
    document.getElementById("txtDescripcion").disabled = false;
    document.getElementById("boton-guardar").disabled = trfalseue;
    document.getElementById("txtNombre").focus();
    } 

function deshabilitar(){
    document.getElementById("txtNombre").disabled = true;
    document.getElementById("txtMarca").disabled = true;
    document.getElementById("txtPrecio").disabled = true;
    document.getElementById("txtImagen").disabled = true;
    document.getElementById("txtDescripcion").disabled = true;
    document.getElementById("boton-guardar").disabled = true;
    document.getElementById("boton-sesion").focus();
    } 
    


function guardar() {
    let n = document.getElementById("txtNombre").value;
    let m = document.getElementById("txtMarca").value;
    let p = parseInt(document.getElementById("txtPrecio").value);
    let im = document.getElementById("txtImagen").value;
    let des=document.getElementById("txtDescripcion").value;
    if (im!=""){
        document.querySelector("#imgPreview").style.display="inline-block";
        document.querySelector("#imgPreview").src = im;
    }else{
        document.querySelector("#imgPreview").style.display="none";
    }
   
  


    let producto = {
        nombre: n,
        marca: m,
        precio: p,
        imagen: im,
        descripcion: des
    }        
    let url = "http://127.0.0.1:8000/api/productos"
    var options = {
        body: JSON.stringify(producto),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
       // redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
 
            // Handle response we get from the API
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
        deshabilitar();
}
