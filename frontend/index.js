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

function handleInput(event) {
    const input = document.getElementById('symptom');
    const selectedSymptomsList = document.getElementById('selectedSymptoms');
    
    if (event.key === 'Enter') {
        const inputValue = input.value.trim();
        const options = document.querySelectorAll('#symptoms option');

        let isValid = false;
        let selectedId = null;
        options.forEach(option => {
            if (option.value === inputValue) {
                isValid = true;
                selectedId = option.getAttribute('data-id');
            }
        });

        if (isValid) {
            const listItem = document.createElement('li');
            listItem.textContent = inputValue;
            selectedSymptomsList.appendChild(listItem);
            selectedDataIds.push(selectedId);
            input.value = '';
            console.log(selectedDataIds);
        } else {
            alert('Invalid symptom');
        }
    }
}

function resetList() {
    const selectedSymptomsList = document.getElementById('selectedSymptoms');
    selectedSymptomsList.innerHTML = '';
    selectedDataIds = [];
}

function submitList() {
    
}

window.onload = () => {
    loadSymptoms();
    document.getElementById('symptom').addEventListener('keypress', handleInput);
    document.getElementById('resetButton').addEventListener('click', resetList);
    document.getElementById('submitButton').addEventListener('click', submitList);
};
