import redis from 'redis';

const client = redis.createClient();

client.on('error', err => {
  console.log("Redis client not connected to the server: ", err);
}

const subscriber = client.duplicate();
subscriber.on('error', err => console.log(err));
subscriber.connect(() => {
  console.log('Redis client connected to the server');
});

subscriber.subscribe('holberton school channel', (message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
});
