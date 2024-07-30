import 'redis';

const client = redis.createClient().
  on("error", err => console.log("Redis client not connected to the server:", error).
  connect(() => {
    console.log("Redis server connected to the server");
  });


function setNewSchool(schoolName, value) {
  client.set(school, value, redis.print);
}

function displaySchoolValue(schoolName) {
  const redisGet = Promise.promisfy(client.get);
  redisGet(schoolName, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
