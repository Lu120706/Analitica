document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("busqueda-informes"); 
    if (!input) return; // Salir si la barra de búsqueda no existe en la página actual

    const contenedor = document.getElementById("resultados-busqueda");
    
    // Inicializar informesData si viene desde el HTML
    const dataContainer = document.getElementById('informes-data-container');
    if (dataContainer && dataContainer.dataset.informes) {
        window.informesData = JSON.parse(dataContainer.dataset.informes);
    }
    
    const informes = typeof window.informesData !== 'undefined' ? window.informesData : [];
    let selectedIndex = -1;

    input.addEventListener("input", (e) => {
        const busqueda = e.target.value.toLowerCase().trim();
        selectedIndex = -1;

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

    input.addEventListener("keydown", (e) => {
        const items = contenedor.querySelectorAll(".list-group-item");
        if (contenedor.classList.contains("d-none") || items.length === 0) return;

        if (e.key === "ArrowDown") {
            e.preventDefault();
            selectedIndex = (selectedIndex + 1) % items.length;
            updateSelection(items);
        } else if (e.key === "ArrowUp") {
            e.preventDefault();
            selectedIndex = (selectedIndex - 1 + items.length) % items.length;
            updateSelection(items);
        } else if (e.key === "Enter" && selectedIndex >= 0) {
            e.preventDefault();
            items[selectedIndex].click();
        }
    });

    function updateSelection(items) {
        items.forEach((item, index) => {
            item.classList.toggle("active", index === selectedIndex);
        });
    }

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