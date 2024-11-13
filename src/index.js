const express = require('express');
const fs = require('fs');
const readline = require('readline');
const path = require('path');

const app = express();
const port = 3000;

// Set up EJS view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

let symptomMap = {};

async function loadSymptoms() {
    try {
        const csvText = fs.readFileSync('data/Symptom_Map.csv', 'utf8');
        const lines = csvText.trim().split('\n');
        symptomMap = {};

        lines.forEach(line => {
            const [symptom, id] = line.split(',');
            symptomMap[symptom.trim()] = id.trim();
        });

        console.log('Loaded symptoms:', symptomMap);
    } catch (error) {
        console.error('Failed to fetch or read CSV:', error.message);
    }
}

// Load symptoms on startup
loadSymptoms();

// Define routes
app.get('/', async (req, res) => {
    // Pass symptom map to the EJS template
    res.render('index', { symptomMap });
});

app.get('/about', (req, res) => {
    res.render('about', { text: 'About Page' });
});

// Start the server
app.listen(port, () => {
    console.log('Symptom map');
    console.log(`Server is running at http://localhost:${port}`);
});
