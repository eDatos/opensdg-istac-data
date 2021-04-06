const express = require('express');
const cors = require('cors');
const DEVELOPMENT = true

const app = express();
const port = 5000 // Si se cambia esto también hay que cambiar el remote_data_prefix en _config.yml en el repositorio del sitio.

app.use(cors());

endpoints = ['comb', 'data', 'edges', 'headline', 'meta', 'stats', 'translations', 'zip'];
languages = ['es', 'en'];

endpoints.forEach(ep => {
    languages.forEach(lan => {
        app.use(`/${lan}/${ep}`, express.static(__dirname + `/_site/es/${ep}`));
    })
});

app.use('/', express.static(__dirname + '/_site'));

app.listen(port, () => {
    if(DEVELOPMENT){
        console.log(`Escuchando en http://localhost:${port}`);
    }
});