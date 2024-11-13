const http = require("http");
var fs = require("fs");
const hostname = "127.0.0.1";
const port = 3000;

fs.readFile('index copy.html', function (err, html) {

  if (err) throw err;    

  http.createServer(function(request, response) {  
      response.writeHeader(200, {"Content-Type": "text/html"});  
      response.write(html);  
      response.end();  
  }).listen(port);

  let selectedDataIds = [];

  async function loadSymptoms() {
      const response = await fetch('../data/Symptom_Map.csv');
      if (!response.ok) {
          console.error('Failed to fetch CSV:', response.statusText);
          return;
      }

      const csvText = await response.text();
      const symptomMap = {};

      const lines = csvText.trim().split('\n');
      lines.forEach(line => {
          const [symptom, id] = line.split(',');
          symptomMap[symptom.trim()] = id.trim();
      });

      const datalist = document.getElementById('symptoms');
      for (const symptom in symptomMap) {
          const option = document.createElement('option');
          option.value = symptom;
          option.setAttribute('data-id', symptomMap[symptom]);
          datalist.appendChild(option);
      }
  }

});
