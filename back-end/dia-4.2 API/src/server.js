const app = require('./app');

const activities = require('./activities');

app.get('/myActivities/:id', (req, res) => {
  const { id } = req.params;
  res.status(200).json(activities[Number(id) - 1]);
});

app.listen(3001, () => console.log('server running on port 3001'));