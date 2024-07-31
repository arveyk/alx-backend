//import { createClient } from 'redis';
redis = require('redis');

const client = redis.createClient();
client.connect();

client.hSet = ('HolbertonSchools', {
  Portland: 50,
  Seattle: 80,
  'New York' : 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
}, redis.print);

client.hGetAll('HolbertonSchools');
