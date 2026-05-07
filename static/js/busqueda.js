
const informes = [
    {
        nombre: "Informe de Ventas",
        url: "/informe/ventas",
        keywords: ["ventas", "ingresos", "vendedores", "comercial"]
    },
    {
        nombre: "Balance de Líneas",
        url: "/informe/balance",
        keywords: ["balance", "lineas", "produccion", "eficiencia"]
    },
    {
        nombre: "Informe Financiero",
        url: "/informe/financiero",
        keywords: ["financiero", "finanzas", "bancos", "tesoreria", "contabilidad"]
    }
];

document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("buscador-informes");
    const contenedor = document.getElementById("resultados-busqueda");

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
                item.className = "list-group-item list-group-item-action d-flex justify-content-between align-items-center";
                item.innerHTML = `<span>${inf.nombre}</span>`;
                contenedor.appendChild(item);
            });
        }
        contenedor.classList.remove("d-none");
    }

    document.addEventListener("click", (e) => {
        if (!input.contains(e.target) && !contenedor.contains(e.target)) {
            contenedor.classList.add("d-none");
        }
    });
});
