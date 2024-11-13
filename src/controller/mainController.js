const axios = require('axios');

const index = async function (req, res){
    res.render('index', { text: '`Th`is is EJS'})
}

const about = async function (req, res){
    res.render('about', { text: 'About Page'})
}
const fs = require('fs');
const readline = require('readline');

module.exports = { index, about }