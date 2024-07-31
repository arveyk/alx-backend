function createPushNotificationsJobs(jobs, kue) {
  if (!typeof(jobs) === Array) {
    throw new Error('Jobs is not an array');
  }
  for (const member of jobs) {
    const push_notification_code_3 = kue.create('notification', member).save(
      function(err) {
        if (!err) {
          console.log(`Notification job created: ${push_notification_code_3.id}`);
	}
	else {
	  console.log(`Notification job ${push_notification_code_3.id} failed: ${err}`);
	}
      });
    push_notification_code_3.on('failed', function(errorMessage) {
      console.log(``);
    }).on('complete', function() {
      console.log(`Notification job ${push_notification_code_3.id} completed`);
    }).on('progress', function(progress, data) {
      console.log(`Notification job ${push_notification_code_3.id} 
        ${progress}`);
    })
  }
}
module.exports = createPushNotificationsJobs;
