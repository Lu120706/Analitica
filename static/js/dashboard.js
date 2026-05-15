document.addEventListener('DOMContentLoaded', function() {

    fetch('/api/dashboard')

        .then(response => response.json())

        .then(data => {

            if (data.status === 'success') {

                document.getElementById('saludo').textContent =
                    data.saludo + ', ' + data.usuario;

                const noticiasDiv =
                    document.getElementById('noticias-content');

                if (data.noticias.length > 0) {

                    noticiasDiv.innerHTML = '';

                    data.noticias.forEach(n => {

                        noticiasDiv.innerHTML += `
                            <p>
                                <strong>${n.titulo}</strong><br>
                                ${n.texto}
                            </p>
                            <hr>
                        `;
                    });

                } else {

                    noticiasDiv.innerHTML =
                        '<p>No hay noticias disponibles.</p>';
                }

                const contactosDiv =
                    document.getElementById('contactos-tic');

                contactosDiv.innerHTML = '';

                data.contactos_tic.forEach(c => {

                    contactosDiv.innerHTML += `
                        <div class="col-md-4 mb-2">
                            <strong>${c.nombre}</strong><br>
                            <span>${c.rol}</span><br>
                            <small>${c.email}</small>
                        </div>
                    `;
                });

                const logosDiv =
                    document.getElementById('logos-content');

                logosDiv.innerHTML = '';

                data.logos.forEach(logo => {

                    logosDiv.innerHTML += `
                        <a href="/empresa/${logo.nombre}" class="logo-card">
                            <img src="${logo.url}" alt="logo ${logo.nombre}">
                        </a>
                    `;
                });

            } else {

                alert('Error al cargar datos: ' + data.message);
            }
        })

        .catch(error => {

            console.error('Error:', error);

            alert('Error al conectar con la API');
        });
});