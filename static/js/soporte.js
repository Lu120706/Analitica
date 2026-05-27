document.addEventListener("DOMContentLoaded", function () {
    const formComentario = document.getElementById("formComentario");
    const txtComentario = document.getElementById("comentario");
    const badgeNotificacion = document.getElementById("badge-notificacion");
    const contenedorNotificaciones = document.getElementById("contenedor-notificaciones-list");
    const API_URL = formComentario ? formComentario.getAttribute("data-api-url") : "/api/comentarios";
    const nombreUsuario = formComentario ? formComentario.getAttribute("data-nombre-usuario") : "";
    if (formComentario && txtComentario) {
        formComentario.addEventListener("submit", function (e) {
            e.preventDefault();

            const texto = txtComentario.value.trim();
            if (!texto) {
                alert("Por favor, escribe un comentario.");
                return;
            }

            fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ comentario: texto })
            })
            .then(res => res.json())
            .then(data => {
                if (data.status === "success") {
                    alert("¡Comentario enviado con éxito!");
                    txtComentario.value = "";
                    const modalEl = document.getElementById("modalSoporte");
                    const modalInstance = bootstrap.Modal.getInstance(modalEl);
                    if (modalInstance) modalInstance.hide();
                } else {
                    alert("Error: " + data.message);
                }
            })
            .catch(err => {
                console.error("Error al enviar:", err);
                alert("Error de conexión con el servidor.");
            });
        });
    }

    if (nombreUsuario && badgeNotificacion) {
        verificarNuevasRespuestas();
        setInterval(verificarNuevasRespuestas, 60000);
    }

    function verificarNuevasRespuestas() {
        fetch(API_URL)
            .then(res => res.json())
            .then(data => {
                const comentarios = data.comentarios || [];
                const respondidos = comentarios.filter(c => c.usuario === nombreUsuario && c.respuesta);
                const vistas = parseInt(localStorage.getItem(`vistas_${nombreUsuario}`) || "0");

                badgeNotificacion.classList.toggle("d-none", respondidos.length <= vistas);
            })
            .catch(err => console.error("Error al verificar:", err));
    }

    const modalNotifEl = document.getElementById('modalNotificaciones');
    if (modalNotifEl) {
        modalNotifEl.addEventListener('shown.bs.modal', function () {
            fetch(API_URL)
                .then(res => res.json())
                .then(data => {
                    const lista = data.comentarios.filter(c => c.usuario === nombreUsuario && c.respuesta);
                    if (lista.length === 0) {
                        contenedorNotificaciones.innerHTML = '<p class="text-muted text-center my-3">Sin respuestas nuevas.</p>';
                        return;
                    }

                    contenedorNotificaciones.innerHTML = lista.map(c => `
                        <div class="p-3 mb-2 rounded bg-light border-start border-3 border-success">
                            <div class="text-muted small">📅 ${c.fecha || 'Reciente'}</div>
                            <div class="text-dark"><strong>Tu mensaje:</strong> "${c.texto}"</div>
                            <div class="mt-2 p-2 bg-white border border-success-subtle">
                                <strong class="text-success">⚙️ Respuesta TIC:</strong>
                                <p class="mb-0 text-secondary">"${c.respuesta.respuesta || c.respuesta}"</p>
                            </div>
                        </div>
                    `).join('');
                    
                    localStorage.setItem(`vistas_${nombreUsuario}`, lista.length);
                    badgeNotificacion.classList.add("d-none");
                });
        });
    }
});