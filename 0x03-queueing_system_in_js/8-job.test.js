const queue = require('kue').createQueue();
const expect = require('chai').expect;
const createPushNotificationsJobs = require('./8-job.js');

before(function() {
  queue.testMode.enter(true);
});
afterEach(function() {
  queue.testMode.clear();
});
after(function() {
  queue.testMode.exit();
});

it('Do some tests', function() {
  const list = [
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ]
  const job = createPushNotificationsJobs(list, queue);
  expect(queue.testMode.jobs[0].data).to.be.an('array');
});
