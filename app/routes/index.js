const path = require('path');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const multer = require('multer'); // v1.0.5
const upload = multer(); // for parsing multipart/form-data

const db = require('../db/mongodb');
const r = require('../db/redis_db');

module.exports = (app) => {
    app.use(cookieParser());
    app.use(bodyParser.json({limit: '50mb'}));
    app.use(bodyParser.urlencoded({limit: '50mb', extended: true, parameterLimit:50000}));

    app.post('/api/news_list', upload.array(), (req, res) => {
        const data = req.body;
        db.get_list(data, (response) => res.json({
            data: response,
            end: data.skip + data.limit
        }));
    });

    app.get('/api/get_news_by_id', (req, res) => {
        const id = req.param('id');
        db.get_news_by_id(id, (response) => {
            res.json({
                data: response
            })
        })
    });

    app.get('/api/get_img_list', (req, res) => {
        r.send_command('SRANDMEMBER', ['jiandan_pic', 10], function(err, response) {
            res.json({
                data: response
            })
        });
    })

    app.post('/api/get_img_list', upload.array(), (req, res) => {
        const data = req.body;
        r.lrange('pengfu_list', data.skip, data.skip + data.limit, function(err, response) {
            res.json({
                data: response,
                end: data.skip + data.limit
            });
        });
    })
}
