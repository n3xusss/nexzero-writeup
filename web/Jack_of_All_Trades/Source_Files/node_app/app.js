const express = require('express');
const { createSigner, createVerifier } = require('fast-jwt')
const fs = require('fs');
const path = require('path');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;
const publicKeyPath = path.join(__dirname, 'public_key.pem');
const publicKey = fs.readFileSync(publicKeyPath, 'utf8');
const privateKeyPath = path.join(__dirname, 'key');
const privateKey = fs.readFileSync(privateKeyPath, 'utf8');

app.use(express.json());
app.use(bodyParser.json({ type: 'application/json' }));

const handlebars = require('express-handlebars');
app.engine('handlebars', handlebars({ layoutsDir: __dirname + '/views/layouts', defaultLayout: false }));
app.set('view engine', 'handlebars');

app.get('/generateToken', async (req, res) => {
    const payload = { admin: false, name: req.query.name };

    const signSync = createSigner({ algorithm: 'RS256', key: privateKey });
    const token = signSync(payload);

    res.json({ token });
});

function verifyToken(req, res, next) {
    if (req.headers["x-access-token"]){
        const token = req.headers["x-access-token"];

        const verifySync = createVerifier({ key: publicKey });
        const payload = verifySync(token);

        req.decoded = payload;
        next();
    } else {
        res.send(`
        <br><br><br><br><br><br>
        <h1 style='text-align:center;font-size:50px;'>Access Denied!</h1>
        <p style='text-align:center;font-size:25px;'>Only admins can access this page!</p>
    `);
    }
}

app.get('/beta', verifyToken, (req, res) => {
    if (req.decoded.admin) {
        res.render('beta');
    }
});

app.post('/beta',verifyToken, async (req, res) => {
    if (req.decoded.admin) {
        try {
            const jsCode = req.body.code;

            const flaskResponse = await fetch('http://flask_app_jack:5000/execute-js', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ code: jsCode })
            });

            const resultData = await flaskResponse.json();
            const result = resultData.result;
            res.json(result);
        } catch (error) {
            console.error(error);
            res.status(500).json({ error: 'Internal Server Error' });
        }
    }
});



app.get('/', (req, res) => {
    res.send(`
        <br><br><br><br><br><br>
        <h1 style='text-align:center;font-size:50px;'>Welcome!</h1>
        <p style='text-align:center;font-size:25px;'>The site is still under development</p>
    `);
});


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
