document.getElementById("loginForm").addEventListener("submit", function(e){

    e.preventDefault();

    let usuario = document.getElementById("usuario").value;
    let password = document.getElementById("password").value;

    let usuarioGuardado = localStorage.getItem("usuario");
    let passwordGuardada = localStorage.getItem("password");

    if(usuario === usuarioGuardado && password === passwordGuardada){

        alert("Inicio de sesión exitoso");

        window.location.href = "inicio.html";

    }else{

        alert("Usuario o contraseña incorrectos");
    }
});