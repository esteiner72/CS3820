const express = require('express');
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const app = express();
const port = 3000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.json());
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, '..', 'public')));
app.use('/data', express.static(path.join(__dirname, '..', 'data')));

app.get('/', (req, res) => {
    res.render('index');
});

app.post("/run-classifier", (req, res) => {
  exec("python3 classifier.py", (error) => {
      if (error) {
        exec("python classifier.py"), (error) => {
            if (error) {
                console.error(`Error: ${error.message}`);
            res.status(500).send("No symptoms entered.");
            return;
            }
        }
      }

      fs.readFile("data/result.csv", "utf8", (err, data) => {
          if (err) {
              console.error(`Error reading result.csv: ${err.message}`);
              res.status(500).send("Error reading the result.");
              return;
          }

          res.send(data);
      });
  });
});

app.post('/submit-data', (req, res) => {
    const { selectedDataIds } = req.body;
    const csvData = selectedDataIds.join(',');
    
    const userInputFilePath = path.join(__dirname, '..', 'data', 'User_Input.csv');
    
    fs.writeFile(userInputFilePath, csvData, 'utf8', (err) => {
        if (err) {
            console.error('Failed to write to User_Input.csv:', err);
            return res.status(500).send('Failed to save data');
        }
        res.send('Data saved successfully');
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});