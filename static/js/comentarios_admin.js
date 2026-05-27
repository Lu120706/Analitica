document.addEventListener('DOMContentLoaded', () => {
    const comentarios = document.querySelectorAll('.comentario-card');
    comentarios.forEach(card => {
        if (card.classList.contains('respondido')) {
            card.style.display = 'none';
        } else {
            card.style.display = 'flex';
        }
    });

    const filtroBtns = document.querySelectorAll('.filtro-btn');
    filtroBtns.forEach(b => b.classList.remove('active'));
    const btnPendiente = document.querySelector('[data-filter="pendientes"]');
    if (btnPendiente) btnPendiente.classList.add('active');

    // En esta pantalla el admin ya no tiene botón/textarea de respuesta (solo vista).
    // Si existieran botones por algún render antiguo, evitamos errores.
    const botones = document.querySelectorAll('.btn-enviar-respuesta');
    if (botones && botones.length > 0) {
        botones.forEach((boton) => {
            boton.addEventListener('click', async () => {
                const comentarioId = boton.dataset.comentarioId;
                const textarea = document.querySelector(`textarea[data-comentario-id="${comentarioId}"]`);
                if (!textarea) return;

                const respuesta = textarea.value.trim();
                if (!respuesta) {
                    alert('Debes escribir una respuesta antes de enviar.');
                    return;
                }

                boton.disabled = true;
                boton.innerText = 'Enviando...';

                try {
                    const request = await fetch('/api/responder-comentario', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ comentario_id: comentarioId, respuesta: respuesta })
                    });
                    const data = await request.json();

                    if (!request.ok) {
                        alert(data.message || 'Error al enviar');
                        boton.disabled = false;
                        boton.innerText = 'Enviar Respuesta';
                        return;
                    }

                    // Si el UI no existe, no intentamos manipular DOM.
                    boton.disabled = false;
                    boton.innerText = 'Enviar Respuesta';
                } catch (error) {
                    console.error(error);
                    alert('Error de conexión');
                    boton.disabled = false;
                    boton.innerText = 'Enviar Respuesta';
                }
            });
        });
    }

    const toggleFiltros = document.getElementById('toggleFiltros');
    const filtroMenu = document.getElementById('filtroMenu');

    if (toggleFiltros) {
        toggleFiltros.addEventListener('click', () => {
            filtroMenu.classList.toggle('active');
        });
    }

    filtroBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filtroBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filtro = btn.dataset.filter;
            const avisoPlaceholder = document.querySelector('.no-comentarios-placeholder');
            if (avisoPlaceholder) avisoPlaceholder.remove();

            comentarios.forEach(card => {
                if (filtro === 'todos') {
                    card.style.display = 'flex';
                } else if (filtro === 'respondidos') {
                    card.style.display = card.classList.contains('respondido') ? 'flex' : 'none';
                } else if (filtro === 'pendientes') {
                    card.style.display = card.classList.contains('pendiente') ? 'flex' : 'none';
                } else if (filtro === 'recientes') {
                    card.style.display = 'flex';
                }
            });

            if (filtroMenu) filtroMenu.classList.remove('active');
        });
    });
});

