document.addEventListener("DOMContentLoaded", () => {
    const formComentario = document.getElementById("formComentario");
    const comentarioInput = document.getElementById("comentario");

    if (!formComentario || !comentarioInput) {
        return;
    }

    formComentario.addEventListener("submit", async (e) => {
        e.preventDefault();

        const textoComentario = comentarioInput.value.trim();
        if (!textoComentario) {
            return;
        }

        const fechaEnvio = new Date().toISOString();
        const data = {
            comentario: textoComentario,
            fecha: fechaEnvio
        };

        try {
            const response = await fetch("/api/comentarios", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                alert("¡Comentario enviado con éxito!");
                formComentario.reset();
                const modalElement = document.getElementById("modalSoporte");
                const modalInstance = bootstrap.Modal.getInstance(modalElement);
                if (modalInstance) {
                    modalInstance.hide();
                }
                return;
            }

            let errorText = response.statusText;
            try {
                const errorData = await response.json();
                if (errorData?.detail) {
                    errorText = errorData.detail;
                } else if (errorData?.message) {
                    errorText = errorData.message;
                }
            } catch (jsonError) {
                // no-op
            }

            console.error("Error al enviar el comentario", response.status, errorText);
            alert("No se pudo enviar el comentario. " + errorText);
        } catch (error) {
            console.error("Error al enviar el comentario", error);
            alert("Ocurrió un error al enviar el comentario.");
        }
    });
});
