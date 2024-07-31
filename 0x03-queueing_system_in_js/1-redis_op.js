//import 'redis';
const redis = require('redis');

const client = redis.createClient()
client.connect().
  catch("error", err => console.log("Redis client not connected to the server:", error).
  connect(() => {
    console.log("Redis server connected to the server");
  }));
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
