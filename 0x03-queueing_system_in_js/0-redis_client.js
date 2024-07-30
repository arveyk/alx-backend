//const createClient = require('redis').createClient;
import { createClient } from 'redis';

const client = createClient().
  on("error", err => console.log("Redis client not connected to the server:", error).
  connect(() => {
    console.log("Redis server connected to the server");
  });
