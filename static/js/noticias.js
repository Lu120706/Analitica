document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('formNoticia');
    if (!form) return;

    form.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            document.getElementById('btnPublicar').click();
        }
    });
});
