function toggleZoom() {
    const cont = document.querySelector(".informe-container");
    const logos = document.querySelector(".logos-fijos");
    const soporte = document.querySelector(".btn-soporte-flotante");

    cont.classList.toggle("fullscreen");
    document.body.classList.toggle("fullscreen-active");
    
    if (cont.classList.contains("fullscreen")) {
        if (logos) logos.classList.add("ocultar-logos");
        if (soporte) soporte.classList.add("ocultar-logos");
    } else {
        if (logos) logos.classList.remove("ocultar-logos");
        if (soporte) soporte.classList.remove("ocultar-logos");
    }
}