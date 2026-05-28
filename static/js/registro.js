document.getElementById("registroForm").addEventListener("submit", function(e){

    e.preventDefault();

    let usuario = document.getElementById("nuevoUsuario").value;
    let password = document.getElementById("nuevaPassword").value;

    localStorage.setItem("usuario", usuario);
    localStorage.setItem("password", password);

    alert("Cuenta creada correctamente");

    window.location.href = "index.html";
});