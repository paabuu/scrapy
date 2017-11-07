const mongoose = require('mongoose');
mongoose.Promise = global.Promise;

const db = mongoose.connect('mongodb://127.0.0.1:27017/acfun',  { useMongoClient: true });
const schema = new mongoose.Schema({});

const News = mongoose.model('news', schema, 'news');

exports.get_list = (callback) => {
    News.find({}, (err, data) => {
        if (err) {
            console.log(err);
        } else {
            callback(data);
        }
    })
}
