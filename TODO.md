# TODO

- [ ] Confirmar qué páginas deben compartir el mismo estilo de logos (según `base.css`).
- [ ] Actualizar `templates/abastecimiento.html` para que:
  - [ ] No cargue `static/css/base.css` dentro de `extra_css` (ya se carga desde `base.html`).
  - [ ] Renderice `data.logos` igual que `contabilidad.html`/`contraloria.html` (condicional `if data.logos`, y manejo seguro `logo.url if logo.url is defined else logo`).
- [ ] (Si aplica) Revisar si `static/css/abastecimiento.css` pisa `.logos-fijos`, `.logo-card` o `img`.
- [ ] Ejecutar la app y verificar visualmente que el bloque de logos se vea consistente en /abastecimiento.

