const express = require('express');
const rateLimit = require('express-rate-limit');
const app = express();
const cookieParser = require('cookie-parser');
app.use(cookieParser());
const crypto = require('crypto');
const hash = crypto.createHash('sha224');
require('dotenv').config();
const jwt = require('jsonwebtoken');
const router = express.Router();
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const bodyParser = require('body-parser');
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
const port = 3000;
app.use(express.static('public'));

const db = new sqlite3.Database('./mydatabase.db');

const createTableQuery = `
  CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      is_admin INTEGER NOT NULL,
      username TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL
  )
`;

const insertDataQuery = `
  INSERT OR IGNORE INTO users (is_admin, username, password) VALUES
      (1, 'LUIS', 'hardpasswordforanyone1ooo1012389213882'),
      (0, 'visitor', 'visitor')
`;


db.exec(createTableQuery, (err) => {
  if (err) {
    console.error('Error creating table:', err.message);
  } else {
    console.log('Table created successfully');
    // Now execute the data insertion query
    db.exec(insertDataQuery, (insertErr) => {
      if (insertErr) {
        console.error('Error inserting data:', insertErr.message);
      } else {
        console.log('Data inserted successfully');
      }
    });
  }
});


const authenticate = (req, res, next) => {
  const token = req.cookies.access_token;

  if (!token) {
    return res.status(401).send('Unauthorized.');
  }

  try {
    const decoded = jwt.verify(token, 'unique');
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(401).send('Invalid token.');
  }
};

// No sqlmap

const loginLimiter = rateLimit({
  windowMs: 2 * 60 * 1000, // 15 minutes
  max: 10, // limit each IP to 5 requests per windowMs
  message: 'Too many login attempts from this IP, please try again after 2 minutes',
});

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/visitor', authenticate, (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'visitor.html'));
});

// Login endpoint
app.post('/login', loginLimiter, (req, res) => {
  const { username, password } = req.body;

  db.all('SELECT * FROM users WHERE username = ? AND password = ?', [username, password], (error, results) => {
    if (error) {
      res.status(500).send('An error occurred while executing the query.');
    } else if (results.length > 0) {
      results.forEach((row) => {
        if (row.is_admin == 1) {
          const user = 'LUIS';

          const token = jwt.sign({ user_type: user }, 'unique', { expiresIn: '24h' });

          return res
            .cookie('access_token', token, {
              httpOnly: true,
              secure: process.env.NODE_ENV === 'production',
            })
            .status(200)
            .redirect('/protected');
        } else {
          const user = 'guest';
          const token = jwt.sign({ user_type: user }, 'unique', { expiresIn: '24h' });

          return res
            .cookie('access_token', token, {
              httpOnly: true,
            })
            .status(200)
            .redirect('/protected');
        }
      });
    } else {
      res.send('Invalid username or password.');
    }
  });
});

// Protected endpoint
app.get('/protected', authenticate, (req, res) => {
  const user = req.user.user_type;
  const hash = crypto.createHash('sha224').update(user).digest('hex');
  const regex = /^[a-zA-Z]+$/;

  if (regex.test(user)) {
    if (hash == 0) {
      res.sendFile(__dirname + '/public/flag.html');
    } else if (user === 'LUIS') {
      res.send(`<!DOCTYPE html>
            <html>
            
            <head>
                <title>Login Page</title>

                <link rel="stylesheet" href="style.css">
            </head>
            
            <body>
                <h1>Welcome to Luis Laboratory</h1>
                <form method="get" action="/protected">
                <p>Welcome Luis! your payload is {'user_type':${hash}}<p>  to secure our data I made a puzzle only me know the asnwer : <br> <br> hash = somehashalgorithm(user_type) <br>  const regex = /^[a-zA-Z]+$/; <br>
                if (regex.test(user_type)) { <br>
                        if (hash == 0) {* SENSITIVE DATA *}}<br>

                    
                    <button type="submit">GET THE KEY</button>
                </form>

            </body>
            
            </html>
            `);
    } else {
      res.redirect('/visitor');
    }
  } else {
    res.send('Sorry, no digits.');
  }
});

app.listen(port, () => {
  console.log(`Listening to port ${port}...`);
});


