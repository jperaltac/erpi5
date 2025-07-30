// @ts-check
/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Escuela ClusterLab',
  tagline: 'Material del taller Raspberry Pi 5',
  url: 'https://jperaltac.github.io',
  baseUrl: '/erpi5/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  organizationName: 'jperaltac',
  projectName: 'erpi5',
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */ ({
        docs: {
          routeBasePath: '/',
          sidebarPath: require.resolve('./sidebars.js'),
        },
        blog: false,
      }),
    ],
  ],
};

module.exports = config;
