const kue = require('kue');

const queue = kue.createQueue();
const obj = {
  phoneNumber: '453897012',
  message: 'This is to verify your account',
};

const push_notification_code = queue.create('job',
  obj);
push_notification_code.on('failed', () => {
  console.log('Notification job failed');
}).on('complete', function() {
  console.log('Notification job completed');
});
push_notification_code.save( function(err) {
  if (!err) console.log(push_notification_code.id);
});
//module.exports = push_notification_code;
