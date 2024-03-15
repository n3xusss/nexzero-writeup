const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const handlebars = require('express-handlebars');
const puppeteer = require('puppeteer');
const ssrfFilter = require('ssrf-req-filter');
const axios = require('axios');
const dns = require('dns');

app.engine('handlebars', handlebars({ layoutsDir: __dirname + '/views/layouts', defaultLayout: false }));
app.set('view engine', 'handlebars');

app.use(bodyParser.json());
app.use(express.static('public'));

app.get('/', (req, res) => {
    res.render('index');
});

app.post('/generate', async (req, res) => {
    const name = req.body.name;

    const data = `
    <!DOCTYPE html>
        <html>
        <head>
            <title>Nexzero CTF Participation Certificate</title>
        </head>
        <style>
            body {
                background-color: #1B1919;
                color: #666; 
                font-family: Arial, sans-serif;
                text-align: center;
            }
            h1, h2, h3 {
                color: #F05323; 
            }
            .container {
                border: 2px solid #F05323;
                padding: 20px;
                max-width: 600px;
                margin: 0 auto;
            }
        </style>
        <body>
        <br>
        <br>
        <br>
        <br>
            <div class="container">
                <h1>Nexzero CTF Participation Certificate</h1>
                <p>This certifies that</p>
                <h2>${name}</h2>
                <p>has participated in the Nexzero Capture The Flag (CTF) event.</p>
                <p>Awarded on this day,</p>
                <p>${new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</p>
                <br>
            </div>
        </body>
        </html>
    `
    const browser = await puppeteer.launch({
        executablePath: '/usr/bin/google-chrome',
        args: ['--no-sandbox']
      });
    const page = await browser.newPage();

    await page.setRequestInterception(true);
    page.on('request', async (request) => {
        let result = await isUrlSafe(request.url())
        console.log('result: ' + result)
        if (result) {
            if (result == '169.254.169.254') {
                request.respond({status: 200, contentType: 'text/plain', body: 'nexus{1f_Y0u_$33_Th1s_Th3n_Y0u_4r3_4_L3g3nd}'});
            } else {
                request.continue();
            }
        } else {
            request.respond({status: 200, contentType: 'text/plain', body: 'NO NO...Not That Easy!'});        
        }
    });

    try {
        await page.setContent(data, {timeout: 5000});
        await page.pdf({ path: 'certificate.pdf', format: 'A4' });
        await browser.close();
        res.download('certificate.pdf', 'certificate.pdf');
    } catch (error) {
        res.json(error)
    }
});


async function isUrlSafe(url) {
    try {
        await axios.get(url, {httpAgent: ssrfFilter(url), httpsAgent: ssrfFilter(url)});
    } catch (error) {
        console.log('Request Blocked: ' + url)
        return false;
    }
    
    let domain = new URL(url).hostname;

    if (domain) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        const addresses = await dns.promises.resolve4(domain);
        if (addresses) {
            console.log(addresses)
            return addresses[0];  
        }
    }
    return '0.0.0.0'
}

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
