// เรียกใช้ dependencies
const express = require("express");
const sqlite3 = require('sqlite3').verbose();
const multer = require("multer");
const session = require('express-session');
const env = require('dotenv').config();

//route


// เริ่มใช้งาน
const app = express();
const port = process.env.PORT;

// เสิร์ฟไฟล์จากโฟลเดอร์ public
app.use(express.static('public'));
app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(session({
    secret: 'mysecretkey',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 3600000 } // 1 ชั่วโมง
}));


// authentication middleware
function authen(req, res, next){
    if(req.session.user){
        return next();
    }
    res.redirect('/login');
}

// path url
app.get('/', (req, res) => {
    res.render('login');
});

// start web
app.listen(port, () => {
  console.log(`Server is running on port http://localhost:${port}`);
});
