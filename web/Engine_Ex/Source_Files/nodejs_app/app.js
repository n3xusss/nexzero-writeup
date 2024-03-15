const express = require('express');

const app = express();

app.get('/', (req, res) => {
    res.send(`
        <br><br><br><br><br><br>
        <h1 style='text-align:center;'>Welcome!</h1>
        <p style='text-align:center;'>The flag is hidden somewhere... Can you find it?</p>
    `);
});

app.get('/flag', (req, res) => {
    res.send(`
        <br><br><br><br><br><br>
        <h1 style='text-align:center;'>Here You Go :</h1>
        <br>
        <p style='text-align:center;'>nexus{Pr0x1y1ng_C4n_B3_D4ng3r0uS$ssss}</p>
    `);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
