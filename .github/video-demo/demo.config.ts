import { defineDemo } from 'video-demo/define';

export default defineDemo({
  name: 'product-ui-skill',
  site: 'https://github.com',
  stage: { width: 1920, height: 1080 },
  clock: { timezone: 'UTC', locale: 'en-US' },
  themes: ['light'],
  entries: {
    app: {
      path: '/alifakbxr/product-ui/blob/main/skills/backend-to-ui/SKILL.md',
      signedIn: false,
      ready: async (page) => {
        await page.getByText('Mandatory frontend stack gate', { exact: false }).first().waitFor({ state: 'visible', timeout: 30000 });
      },
    },
  },
  tour: ['smoke'],
});
