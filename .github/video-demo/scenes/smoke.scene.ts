import { scene } from 'video-demo/scene';

scene('smoke', {
  title: 'product-ui public repo preview',
  blurb: 'Verify a real public GitHub repository renders before recording a guided scene.',
}, async ({ actor, shot }) => {
  await actor.beat(250);
  await shot('readme');
});
