---
title: Compilar las presentaciones
slug: /compilar
---

Los archivos PDF se generan a partir de las fuentes \`LaTeX\`. Para
obtenerlos necesitas \`lualatex\` y las fuentes Inter, Fira Code y
Libertinus. Tambien se usa el paquete \`minted\`, asi que Python y
\`pygments\` deben estar instalados.

```bash
make       # compila todos los dias
make clean # elimina temporales
```

Para detalles adicionales puedes consultar el
[README del proyecto](https://github.com/jperaltac/erpi5).
