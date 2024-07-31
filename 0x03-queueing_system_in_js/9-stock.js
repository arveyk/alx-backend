const express = require('express');
const redis = require('redis');

const client = redis.createClient().connect();
const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  },

];
const app = express();
const port = 1245;

function getItemById (id) {
  const item listProducts.find((idN) => idN === id);
  return item.name
}

app.listen(post, () => {
});

app.get('/list_products', (req, res) => {
  res.send(JSON.jsonify(listProducts));
});

function reserveStockById(itemId, stock) {
  for (const item of listProducts) {
    if (item.id === itemId) {
      client.set(item.id, stock);
    }
}

async function getCurrentReservedStockById(itemId) {
  const item listProducts.find((idN) => idN === id);
  return item.stock
}
app.get('/list_products/:itemId', (req, res) => {
  const product = getItemById(req.itemId)
  const stock = getCurrentReservedStockById(req.itemId);
  res.send(JSON.jsonify(product, stock));
});

app.get('/reserve_product/:itemId', (req, res) => {
  const item = getItemById(req.itemId);
  if (!item) {
    return;
  }
  const stock = getCurrentReservedStockById(req.itemId);
  if (stock < 1) {
    return;
  }
  reserveStockById(req.itemId);
});
