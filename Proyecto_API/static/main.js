


if (document.getElementById("app")){
    const app=new Vue({
        el:"#app",
        data(){
            return{
            productos:[],
            errored:false,
            loading:true,
            }
        },
        created(){
            var url="http://127.0.0.1:8000/api/productos"
            this.fetchData(url);
        },
        methods:{
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.usuarios = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(usuario) {
                localStorage.setItem("sesion", 1);
                const url = "http://127.0.0.1:8000/api/productos/borrar" + producto;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                    })
            }
        }
    })
}
