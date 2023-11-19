require('dotenv').config()
const SECRETS = process.env;

const mysql = require('mysql');

const conn = mysql.createConnection({
    host:"pi4B1",
    user:SECRETS.DB_USER,
    password:SECRETS.DB_USER_PWD,
    database: SECRETS.DB_NAME
})

let sql = "";

conn.connect(function(err) {
    if (err) throw err;
    console.log("Connected")
    sql = "ALTER TABLE pltf_users ADD COLUMN user_email VARCHAR(255)";
    conn.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Result: Table created")
        console.log("Result: " + result)
    })
});




/*
Create table:
sql = "CREATE TABLE pltf_users (name VARCHAR(255), password CHAR(64))";

Alter table:
sql = "ALTER TABLE pltf_users ADD COLUMN user_id INT AUTO_INCREMENT PRIMARY KEY";

 */