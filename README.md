# Cl\xC3\xBAsterLab Raspberry Pi 5 Slides

This repository contains the Beamer slides used for the "Cl\xC3\xBAsterLab" workshop focusing on Raspberry Pi 5. The material is organized per day (`D01` to `D10`) and written in Spanish. Each directory includes the corresponding `.tex` sources and precompiled PDFs.

## Building

A simple `Makefile` is provided in each day directory to build the slides using `lualatex`. Run `make` inside a directory to compile that day's slides, or from the repository root to build them all:

```bash
make       # builds all days
make clean # removes PDFs and temporary files
```

Ensure `lualatex` and the required fonts (Inter, Fira Code, Libertinus) are installed on your system. The slides rely on `minted`, so Python and `pygments` are also needed.

## License

This project is distributed under the terms of the GNU General Public License v3. See [LICENSE](LICENSE) for details.

## Website

A minimal [Docusaurus](https://docusaurus.io) site is provided under `website/`.
Run `npm install` in that folder followed by `npm run build` to generate the
static site for GitHub Pages. Update the organisation name and `baseUrl` in
`website/docusaurus.config.js` if your repository lives under a different
account.
