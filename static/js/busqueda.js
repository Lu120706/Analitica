document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("buscador-informes");
    const contenedor = document.getElementById("resultados-busqueda");
    const informes = typeof informesData !== 'undefined' ? informesData : [];

    input.addEventListener("input", (e) => {
        const busqueda = e.target.value.toLowerCase().trim();

        if (busqueda.length === 0) {
            contenedor.classList.add("d-none");
            return;
        }

        const encontrados = informes.filter(inf => {
            return inf.nombre.toLowerCase().includes(busqueda) ||
                   inf.keywords.some(p => p.includes(busqueda));
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