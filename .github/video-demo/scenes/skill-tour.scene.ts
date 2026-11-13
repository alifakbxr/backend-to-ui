import { scene } from 'video-demo/scene';

scene('skill-tour', {
  title: 'Use your frontend, not a template',
  blurb: 'Real source in product-ui: existing frontend support and the mandatory stack choice.',
}, async ({ page, actor, shot }) => {
  const intro = page.getByText('Build product-specific interfaces for existing frontend apps', { exact: false }).first();
  await actor.to(intro);
  await actor.say('It starts with the frontend you already have, not an empty template.');
  await shot('existing-frontend');

  const policy = page.getByRole('link', { name: 'stack decision policy' }).first();
  await actor.click(policy);
  await page.getByRole('heading', { name: 'Mandatory frontend stack selection' }).waitFor({ state: 'visible', timeout: 20000 });
  await actor.spotlight(
    page.getByRole('heading', { name: 'Mandatory frontend stack selection' }),
    'If you haven\'t chosen a stack, it asks before changing your UI.',
    { scale: 1.15, stay: true }
  );
  await shot('stack-policy');
});
