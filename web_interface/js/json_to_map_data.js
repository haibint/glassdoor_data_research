'use strict';

const fs = require('fs');

let rawdata = fs.readFileSync('json/GE_by_state_year.json');  
let data = JSON.parse(rawdata);  
// console.log(student); 
let map_data = {}

data.forEach(function (data_point, index) {
    const modified_state_name = "US-"+ data_point.state;
    if (modified_state_name in map_data) {

    }else {
        // !! now it takes only the first occurency into account
        map_data[modified_state_name] = data_point.year + "             " + data_point.net_sentiments_ave
    }
});

console.log(map_data)
// console.log(Object.keys(map_data).length)