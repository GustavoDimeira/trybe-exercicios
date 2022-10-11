const express = require('express');
const cors = require('cors');
require('express-async-errors');

const activities = [{
  name: 'Trekking',
  price: 0,
  description: {
    rating: 5,
    difficulty: 'Fácil',
    createdAt: '10/08/2022',
  },
  token: 1,
}];

const app = express();
app.use(express.json());
app.use(cors());

const { addActivite } = require('./services/functions');
const { checkDescription, checkName, checkPrice } = require('./services/middlewares');
const generateToken = require('./services/randomKey');

app.post('/activities', checkName, checkPrice, checkDescription, (req, res) => {
  const { name, price, description } = req.body;
  addActivite(activities, { name, price, description, token: generateToken() });
  console.log('adicionado com sucesso');
  res.status(200).json(activities);
});

module.exports = app;
