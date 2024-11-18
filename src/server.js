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

app.post('/run-notebook', (req, res) => {
    const jupyterPath = '/opt/homebrew/lib/python3.10/site-packages/jupyter';
    const notebookPath = path.join(__dirname, 'model_test.ipynb');
    const command = `${jupyterPath} nbconvert --to notebook --execute ${notebookPath} --output result.ipynb`;
  
    exec(command, (err, stdout, stderr) => {
      if (err) {
        console.error('Error executing notebook:', stderr);
        return res.status(500).send('Error executing notebook');
      }
  
      console.log('Notebook executed successfully:', stdout);
  
      const resultFilePath = path.join(__dirname, 'result.csv');
  
      if (fs.existsSync(resultFilePath)) {
        // Read the CSV file and send its content as text
        const csvContent = fs.readFileSync(resultFilePath, 'utf8');
        res.type('text/csv').send(csvContent);
      } else {
        res.status(500).send('No result file generated');
      }
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