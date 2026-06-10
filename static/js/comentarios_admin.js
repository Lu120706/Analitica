document.addEventListener('DOMContentLoaded', () => {
    const hash = window.location.hash.replace('#', '');
    if (hash) {
        const target = document.getElementById(hash);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'center' });
            target.classList.add('destacado');
            setTimeout(() => target.classList.remove('destacado'), 2500);
        }
    }

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
    const botones = document.querySelectorAll('.btn-enviar-respuesta');
    if (botones && botones.length > 0) {
        botones.forEach((boton) => {
            const comentarioId = boton.dataset.comentarioId;
            const textarea = document.querySelector(`textarea[data-comentario-id="${comentarioId}"]`);

            if (textarea) {
                textarea.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter' && !e.shiftKey) {
                        e.preventDefault();
                        boton.click();
                    }
                });
            }

            boton.addEventListener('click', async () => {
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
                    alert('Respuesta enviada correctamente.');
                    window.location.reload();
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

    // El filtro ya no depende del toggle, removemos la funcionalidad
    if (toggleFiltros) {
        toggleFiltros.style.cursor = 'default';
    }
    // Asegurar que el menú esté siempre visible
    if (filtroMenu) {
        filtroMenu.classList.add('active');
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
                const ordenados = Array.from(comentarios).sort((a, b) => b.dataset.id - a.dataset.id);
                comentarios.forEach((card, index) => {
                    card.style.display = index < 10 ? 'flex' : 'none';
                });
            } else if (filtro === 'archivados') {
                const ordenados = Array.from(comentarios).sort((a, b) => b.dataset.id - a.dataset.id);
                comentarios.forEach((card, index) => {
                    card.style.display = index >= 10 ? 'flex' : 'none';
                });
            }

            });

            // Mantener el menú siempre visible
            if (filtroMenu) filtroMenu.classList.add('active');
        });
    });
});
