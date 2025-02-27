const express = require('express');
const { exec } = require('child_process');
const app = express();

app.get('/run-python', (req, res) => {
    exec('python3 script.py', (error, stdout, stderr) => {
        if (error) return res.status(500).send(error.message);
        res.send(stdout);
    });
});

app.listen(3000, () => console.log('Server running on port 3000'));
