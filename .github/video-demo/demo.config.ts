import { defineDemo } from 'video-demo/define';

export default defineDemo({
  name: 'product-ui-public-repo',
  site: 'https://github.com',
  stage: { width: 1920, height: 1080 },
  clock: { timezone: 'UTC', locale: 'en-US' },
  themes: ['light'],
  entries: {
    app: {
      path: '/alifakbxr/product-ui',
      signedIn: false,
      ready: async (page) => {
        await page.locator('article.markdown-body').first().waitFor({ state: 'visible', timeout: 30000 });
      },
    },
  },
  tour: ['smoke'],
});
