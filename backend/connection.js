var mysql = require('mysql');
  
var con = mysql.createConnection({
    host: "mysql.labthreesixfive.com",
    user: "group6a",
    password: "NR^DH\"e<CV8*j<@h",
    database: "group6a"
});
  
// Created the Connection
/*con.connect(function(err) {
   if (err) throw err;
     console.log("Connected!");
     });*/
//create connection and switch to group database
con.connect(function (err) {
   if (err) throw err;
   console.log("Connected!");

   var showTables = "show tables";
   con.query(showTables, function (err, result) {
       if (err) throw err;
       console.log(result);
   });
});
