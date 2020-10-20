var mysql = require('mysql');
var express = require('express');



const db = mysql.createConnection({
    host: "localhost",
    user: "atharva",
    password: "aaaAAA2#",
    database: "cardatabse"
  });

db.connect((err)=>{
  // if(err){
  //   throw err;
  // }
  console.log('MySql connected');
})

const app = express()

app.get('/getdatabases', (req,res) => {
  
  let sqlQ = 'USE cardatabse';
  db.query(sqlQ , (err,result) =>{
    // console.log(result);
    // res.send('look in console')
  });

  let sqlQ1 = "Insert into driver_details values('D002', 'HARISH KALE', STR_TO_DATE('06-01-1987', '%m-%d-%Y'), 'BANER HOMES, BANER', 'MH12KL1365', STR_TO_DATE('06-01-2019', '%m-%d-%Y'));";
  // let sqlQ1 = 'select * from driver_details'
  db.query(sqlQ1 , (err,result) =>{
    // if(err){
    //   throw err;
    // }
    // console.log(result);

    res.send(err)
  });
});

app.get('/test', (req,res) => {
  let sqlQ = 'select * from Driver_Details';
  db.query(sqlQ , (err,result) =>{
    // console.log(result);
    // res.send('look in console')
    res.send(result)
  });
});

app.listen('3000' ,() => {
  console.log('server started on port 3000')
})
