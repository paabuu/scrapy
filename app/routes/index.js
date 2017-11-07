const path = require('path');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const multer = require('multer'); // v1.0.5
const upload = multer(); // for parsing multipart/form-data

const db = require('../db/mongodb');

module.exports = (app) => {
    app.use(cookieParser());
    app.use(bodyParser.json({limit: '50mb'}));
    app.use(bodyParser.urlencoded({limit: '50mb', extended: true, parameterLimit:50000}));

    app.get('/list', (req, res) => {
        db.get_list((data) => {
            res.json({data})
        });
    })
}
