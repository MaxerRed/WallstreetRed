const { exec } = require('child_process');
exec('python3 script.py', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error: ${error.message}`);
        return;
    }
    console.log(`Output: ${stdout}`);
});
