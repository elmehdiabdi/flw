var http = require('http');
exports.handler = (event, context, callback) => {
let requestData = {
    "query": {
        "query_string" : {
            "query" : event['q']
        }
    }
}
        const options = {
            host: 'search-simple-es-2ji7mlt4mv42eh5jk6bcrdmux4.us-east-1.es.amazonaws.com', // api endpoint without http/https specification
            path: '/_search',
            method: 'POST',
            headers: {
            "Content-Type": "application/json",
            }
        };

        const req = http.request(options, (res) => {
            console.log('waiting for it');
            let data = ''; 
    
              // A chunk of data has been recieved.
              res.on('data', (chunk) => {
                data += chunk;
              });
            
              // The whole response has been received. Print out the result.
              res.on('end', () => {
                data = JSON.parse(data);
                console.log('Search response :: ' + JSON.stringify(data));
                let sourceParsing = data['hits']['hits'];
                var response = [];
                sourceParsing.forEach(function eachItem(item) {
                   console.log(item);
                   response.push(item._source);
                });
                callback(null, response);
              });
        });
        
        req.write(JSON.stringify(requestData));
        // send the request
        req.end();

};