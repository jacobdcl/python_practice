require('dotenv').config();
const express = require('express');
const request = require('request-promise-native');

const app = express();

const clientId = process.env.SPOTIFY_CLIENT_ID;
const clientSecret = process.env.SPOTIFY_CLIENT_SECRET;
const redirectUri = process.env.REDIRECT_URI;

// Your frontend files will be in the 'public' directory
app.use(express.static('public'));

// This endpoint will redirect to Spotify's authorization page
app.get('/login', (req, res) => {
  const scope = 'user-read-private user-read-email';
  res.redirect('https://accounts.spotify.com/authorize?' +
    new URLSearchParams({
      response_type: 'code',
      client_id: clientId,
      scope: scope,
      redirect_uri: redirectUri,
    }));
});

// This is the callback endpoint that Spotify will redirect to
app.get('/callback', async (req, res) => {
  const code = req.query.code || null;
  const options = {
    url: 'https://accounts.spotify.com/api/token',
    form: {
      code: code,
      redirect_uri: redirectUri,
      grant_type: 'authorization_code'
    },
    headers: {
      'Authorization': 'Basic ' + (Buffer.from(clientId + ':' + clientSecret).toString('base64'))
    },
    json: true
  };
  try {
    const data = await request.post(options);
    const accessToken = data.access_token;
    res.redirect('/#' +
      new URLSearchParams({
        access_token: accessToken,
      }));
  } catch (error) {
    res.redirect('/#' +
      new URLSearchParams({
        error: 'invalid_token'
      }));
  }
});

const PORT = 8888;
app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});



const express = require('express');

