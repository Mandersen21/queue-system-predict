const express = require('express')
const app = express()
const cors = require('cors');
const bodyParser = require("body-parser");
const config = require('config');
const winston = require('winston');
const PythonShell = require('python-shell');

app.use(cors())
app.use(bodyParser.json());
app.use(express.urlencoded({ extended: true }));

// Python endpoint.
app.get('/predict', getPrediction);

function getPrediction(req, res) {

    // Options to script
    var options = {
        args:
        [
          req.body.triage, // triage colour
          req.body.week, // week day
          req.body.time, // time at day
          req.body.avgWait // average waiting time for last 3 patients
        ]
      }

    PythonShell.run('./python.py', options, function (err, data) {
        if (err) res.send(err);
        if (data) {
            var prediction = data.toString()
            prediction = prediction.split("[")[1].split("]")[0]
            res.send(prediction)
        }
        else res.send(null)
    });
}

const port = process.env.PORT || 4000;
const server = app.listen(port, () => winston.info('Listening on port ' + port))

module.exports = server;