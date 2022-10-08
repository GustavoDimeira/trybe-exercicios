const app = require('./app');

const activities = require('./activities');

app.get('/myActivities/:id', (req, res) => {
  const { id } = req.params;
  res.status(200).json(activities[Number(id) - 1]);
});

app.get('/myActivities', (_req, res) => {
  res.status(200).json(activities);
});

app.get('/filter/myActivities', (req, res) => {
  const { status } = req.query;
  let filteredActivities = activities;

  if (status) {
    filteredActivities = activities.filter((activity) => activity.status === status);
  }

  res.status(200).json({ activities: filteredActivities });
});

app.listen(3001, () => console.log('server running on port 3001'));