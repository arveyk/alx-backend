const kue = require('kue');

const queue = kue.createQueue();

const blacklist = [ '4153518780', '4153518780' ];
function sendNotification(phoneNumber, message, job, done) {
  if (blacklist.includes(phoneNumber)) {
    console.log(`Phone number ${phoneNumber} is blacklisted`);
    return new Error();
  }
  if (done <= 50) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const data = job.data;
  sendNotification(data.phoneNumber, data.message, data.job, data.done);
});
