      // the post options
    var optionspost = {
        host: 'http://api.tvmaze.com/singlesearch/shows?q=mr-robot&embed=episodes',
        // path: '/'+index+'/'+type+'/id',
        method: 'GET',
        // port:443,
        // headers: {
        //     'Content-Type': 'application/json',
        // }
    };

    var reqPost = https.request(optionspost, function(res) {
        console.log("statusCode: ", res.statusCode);
        res.on('data', function (chunk) {
           console.log(res);
        });
    });
    reqPost.write(JSON.stringify(json_d));
    reqPost.end();