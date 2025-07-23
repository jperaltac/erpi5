// @ts-check
/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Cl\u00FAsterLab Raspberry Pi 5',
  // Update these values with your GitHub organisation/user if needed
  url: 'https://your-org.github.io',
  baseUrl: '/erpi5/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  organizationName: 'your-org',
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
  themeConfig: {
    navbar: {
      title: 'Raspberry Pi 5',
      items: [
        {
          href: 'https://github.com/your-org/erpi5',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
  },
};

module.exports = config;
