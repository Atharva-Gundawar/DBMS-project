var mysql = require('mysql');
var express = require('express');

const db = mysql.createConnection({
    host: "localhost",
    user: "atharva",
    password: "aaaAAA2#",
    database: "cardatabse"
  });

db.connect((err)=>{
  console.log('MySql connected');
})

let sqlQ = 'USE cardatabse';
db.query(sqlQ , (err,result) =>{
  console.log(result);
});

const app = express()

app.get('/',(req,res) => {
    let sqlQ = 'selct * from Driver_Bank';
    db.query(sqlQ , (err,result) => {
        
    })
})

app.listen('3000' ,() => {
    console.log('server started on port 3000')
  })