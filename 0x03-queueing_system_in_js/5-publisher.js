import redis from 'redis';
import { setInterval } from 'timers/promises';

const publisher = redis.createClient();


publisher.on('error', (err) => console.log(err));
client.connect(() => console.log());

function publishMessage(message, time => {
  console.log(`About to send ${message}`);
  setInterval(() => {
    publisher.publish('holberton school channel', message);
  }, time);
});
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
