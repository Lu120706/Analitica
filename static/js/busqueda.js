document.addEventListener("DOMContentLoaded", () => {
    // Corregido: el ID en el HTML es 'busqueda-informes'
    const input = document.getElementById("busqueda-informes"); 
    const contenedor = document.getElementById("resultados-busqueda");
    // Asumimos que informesData viene de informes_data.js incluido en el template
    const informes = typeof informesData !== 'undefined' ? informesData : [];

    input.addEventListener("input", (e) => {
        const busqueda = e.target.value.toLowerCase().trim();

        if (busqueda.length === 0) {
            contenedor.classList.add("d-none");
            return;
        }

        const encontrados = informes.filter(inf => {
            return inf.nombre.toLowerCase().includes(busqueda) ||
                   inf.keywords.some(p => p.toLowerCase().includes(busqueda));
        });

        mostrarResultados(encontrados);
    });

    function mostrarResultados(lista) {
        contenedor.innerHTML = "";
        if (lista.length === 0) {
            contenedor.innerHTML = '<div class="list-group-item text-muted">No se encontraron informes</div>';
        } else {
            lista.forEach(inf => {
                const item = document.createElement("a");
                item.href = inf.url;
                item.className = "list-group-item list-group-item-action";
                item.innerHTML = `<span>${inf.nombre}</span>`;
                contenedor.appendChild(item);
            });
        }
        contenedor.classList.remove("d-none");
    }
});