const express = require('express')
const app = express()
const PythonShell = require('python-shell');

app.get('/predict', getPrediction);

function getPrediction(req, res) {

    PythonShell.run('./python.py', function (err, data) {
        if (err) res.send(err);
        res.json(data)
    });
}

app.listen(4000, () => console.log('Application listening on port 4000!'))