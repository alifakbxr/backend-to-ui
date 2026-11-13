import { scene } from 'video-demo/scene';

scene('voice-track', {
  title: 'Narration for the end-to-end product-ui demonstration',
  blurb: 'A truthful walkthrough: install command, example prompt, same-data before and after, and real fixture interactions.',
}, async ({ actor }) => {
  await actor.say('First, install the backend to UI skill from the product UI repository.');
  await actor.beat(240);
  await actor.say('Then ask your coding agent to improve your existing frontend, without changing its framework.');
  await actor.beat(240);
  await actor.say('Here is the starting point. The actual packing queue is buried under dashboard charts.');
  await actor.beat(240);
  await actor.say('The redesigned workbench uses the same order data, but puts the task first.');
  await actor.beat(240);
  await actor.say('Search by customer or order. Empty results have a clear way back.');
  await actor.beat(240);
  await actor.say('Select an order, mark it packed, and see the queue update.');
  await actor.beat(240);
  await actor.say('Even error states have a recovery path.');
  await actor.beat(240);
  await actor.say('The same flow also works on narrow screens.');
  await actor.beat(240);
  await actor.say('This is a functional demo fixture, not a recording of a coding agent generating the app.');
});
