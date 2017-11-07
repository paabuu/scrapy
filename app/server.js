const express = require('express');

const app = express();

const routes = require('./routes/index.js');

routes(app);

app.get('/', (req, res) => res.end('success!'));

app.listen(3000)
