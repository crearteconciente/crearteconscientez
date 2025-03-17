document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        document.querySelector(".door.left").style.transform = "translateX(-100vw)";
        document.querySelector(".door.right").style.transform = "translateX(100vw)";
    }, 100); // Pequeña espera para asegurarse de que los estilos están aplicados
});
