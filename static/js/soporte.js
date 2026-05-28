document.addEventListener("DOMContentLoaded", function () {
    const formComentario = document.getElementById("formComentario");
    const txtComentario = document.getElementById("comentario");
    const badgeNotificacion = document.getElementById("badge-notificacion");
    const contenedorNotificaciones = document.getElementById("contenedor-notificaciones-list");
    const API_URL = formComentario ? formComentario.getAttribute("data-api-url") : "/api/comentarios";
    
    // --- LÓGICA DE NOTIFICACIONES ---
    function verificarNotificaciones() {
        if (!badgeNotificacion) return;
        fetch("/api/notificaciones")
            .then(res => res.json())
            .then(data => {
                if (data.count > 0) {
                    badgeNotificacion.classList.remove("d-none");
                } else {
                    badgeNotificacion.classList.add("d-none");
                }
            })
            .catch(err => console.error("Error al verificar:", err));
    }
    setInterval(verificarNotificaciones, 15000); // 15 segundos para mayor reactividad
    verificarNotificaciones();

    if (formComentario && txtComentario) {
        formComentario.addEventListener("submit", function (e) {
            e.preventDefault();
            const texto = txtComentario.value.trim();
            if (!texto) return alert("Escribe un comentario.");

            fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ comentario: texto })
            })
            .then(res => res.json())
            .then(data => {
                if (data.status === "success") {
                    alert("¡Comentario enviado!");
                    txtComentario.value = "";
                    bootstrap.Modal.getInstance(document.getElementById("modalSoporte")).hide();
                } else {
                    alert("Error: " + data.message);
                }
            });
        });
    }

    // --- MODAL NOTIFICACIONES ---
    const modalNotifEl = document.getElementById('modalNotificaciones');
    if (modalNotifEl) {
        modalNotifEl.addEventListener('shown.bs.modal', function () {
            fetch("/api/comentarios")
                .then(res => res.json())
                .then(data => {
                    const todos = data.comments || [];
                    const esAdmin = document.body.dataset.rol === 'admin';
                    // Filtramos: Admin ve pendientes, Usuario ve sus respuestas no leídas
                    let lista = esAdmin ? todos.filter(c => !c.leido_admin) : todos.filter(c => c.respuesta && !c.leido_usuario);

                    if (lista.length === 0) {
                        contenedorNotificaciones.innerHTML = '<p class="text-center my-3">Sin notificaciones nuevas.</p>';
                        return;
                    }

                    contenedorNotificaciones.innerHTML = lista.map(c => `
                        <div class="p-3 mb-2 rounded bg-light border-start border-3 border-primary">
                            <div class="text-muted small">📅 ${c.fecha_envio || 'Reciente'}</div>
                            <div class="text-dark"><strong>${esAdmin ? c.nombre_usuario : "Soporte TIC"}:</strong> "${esAdmin ? c.comentario : c.comentario}"</div>
                            ${c.respuesta ? `
                                <div class="mt-2 p-2 bg-white border border-primary-subtle">
                                    <strong class="text-primary">⚙️ ${esAdmin ? "Tu respuesta" : "Respuesta TIC"} (${c.respuesta.fecha_respuesta || 'Reciente'}):</strong>
                                    <p class="mb-0 text-secondary">"${c.respuesta.respuesta}"</p>
                                </div>
                            ` : ''}
                        </div>
                    `).join('');
                    
                    // Marcar como leído
                    lista.forEach(c => {
                        fetch(esAdmin ? "/api/notificaciones/leido_admin" : "/api/notificaciones/leido_usuario", {
                            method: "POST",
                            headers: { "Content-Type": "application/json" },
                            body: JSON.stringify({ comentario_id: c.id })
                        });
                    });
                });
        });
    }
});