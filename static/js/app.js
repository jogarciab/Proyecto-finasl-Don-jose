const menu = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

function toggleMenu(){
    menu.classList.toggle("active");
    overlay.classList.toggle("active");
}
/* CERRAR MENU */
overlay.addEventListener("click", () => {
    menu.classList.remove("active");
    overlay.classList.remove("active");
});
/* IR A VENTAS */
function goVentas(){
    window.location.href = "/venta";
}
/* IR A FACTURACION*/
function goFacturacion(){
    window.location.href = "/facturacion";
}
/* IR A REPORTES*/
function Reportes(){
    window.location.href = "/reportes";
}
/* IR A COMPRAS*/
function Compras(){
    window.location.href = "/compras";
}