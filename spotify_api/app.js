document.getElementById('login-button').addEventListener('click', () => {
    window.location = '/login';
});

// After login, Spotify redirects to /callback and then that redirects to /# with the access token
if (window.location.hash) {
    const { access_token } = Object.fromEntries(new URLSearchParams(window.location.hash.substring(1)));
    if (access_token) {
        // Now you can use the access token to make requests to the Spotify API
        // For example, fetch the user's top tracks here
    }
}
