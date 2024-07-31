const redis = require('redis');
const until = require('util');
const kue = require('kue');
const express = require('express');

const client = util.promisify(redis.createClient());


async function reserveSeat(number) {
  await client.set('available_seats', number);
}
async function getCurrentAvailableSeats() {
  await client.get('available_seats');
}
const reservationEnabled = true;
reserveSeat(50);

const queue = kue.createQueue();

const app = express();

app.get('/available_seats', (req, res) => {
  res.send(getCurrentAvailableSeats());
});

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
	  res.send({"status": "Reservation are blocked"});
  }
  const job = queue.create('reserve_seat').save(function(err) {
    if (!err) {
      res.send({'status': 'Reservation failed'});
    }
    else {
      res.send({'status': 'Reservation in progress'});
    }
  });
  job.on('complete' function() {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', function(errorMessage) {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('process', (req, res) => {
  queue.process('reserve_seat', async function(job, done) {
    const seats = getCurrentAvailableSeats();
    if (seats) {
      reserveSeat();
    }
    const currSeats = getCurrentAvailableSeats();
    if (currSeats === 0) {
      reservationEnabled = false;
    }
  });
  res.send({'status': 'Queue processing'});
});

