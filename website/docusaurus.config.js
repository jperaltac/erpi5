// @ts-check
/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Cl\u00FAsterLab Raspberry Pi 5',
  url: 'https://example.com',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  organizationName: 'example',
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
