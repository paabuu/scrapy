const mongoose = require('mongoose');
mongoose.Promise = global.Promise;

const db = mongoose.connect('mongodb://127.0.0.1:27017/acfun',  { useMongoClient: true });
const schema = new mongoose.Schema({});

const News = mongoose.model('news', schema, 'news');
//
// exports.get_list = (data, callback) => {
//     News.find({}, null, { skip: data.skip, limit: data.limit }, (err, response) => {
//         !err && callback(response);
//     })
// }
exports.get_list = (data, callback) => {
    News.find({}).sort({create_time: -1}).skip(data.skip).limit(data.limit).exec((err, response) => {
        !err && callback(response);
    })
}


exports.get_news_by_id = (id, callback) => {
    News.find({ "_id": id }, (err, response) => {
        !err && callback(response);
    })
}
