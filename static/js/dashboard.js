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

                // Definir el orden fijo
                const ordenLogos = {
                    "https://cdn.phototourl.com/free/2026-05-08-c4138ab4-2de9-48d8-a38a-0c85bc40a293.png": 0,
                    "https://cdn.phototourl.com/free/2026-05-08-5729c248-9b06-4eec-85a9-656cabf66c54.png": 1,
                    "https://cdn.phototourl.com/free/2026-05-08-96a31c18-592e-4d88-ad11-2b32bc4c58aa.png": 2
                };

                const logosOrdenados = data.logos.sort((a, b) => (ordenLogos[a.url] || 99) - (ordenLogos[b.url] || 99));

                logosOrdenados.forEach(logo => {
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