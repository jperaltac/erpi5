---
title: Compilar las presentaciones
slug: /compilar
---

Los archivos PDF se generan a partir de las fuentes \`LaTeX\`. Para
obtenerlos necesitas \`lualatex\` y las fuentes Inter, Fira Code y
Libertinus. Tambi\u00E9n se usa el paquete \`minted\`, as\u00ED que Python y
\`pygments\` deben estar instalados.

```bash
make       # compila todos los d\u00EDas
make clean # elimina temporales
```

Para detalles adicionales puedes consultar el
[README del proyecto](https://github.com/jperaltac/erpi5).
