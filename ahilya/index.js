var AWS = require('aws-sdk');
var ses = require('./se-elastic')
exports.handler = (event, context, callback) => {
var region='us-east-1';
var domain='https://search-open-es-search-mjlstj7e56bmyossebif2inaeu.us-east-1.es.amazonaws.com';
var index='node-test';
var type='_doc';
var id =1;
var json_d={
  "eventId" : "WMS-16217413-fa3f-473b-a390-4b5c0643e2e9",
  "eventType" : "Registration Notification",
  "eventStatus" : "Delivered",
  "sourceSystem" : "WMS",
  "amwayPartyId" : "123456ABGCD",
  "localeId" : "en-us",
  "eCommTypeCd" : "Email",
  "communicationDate" : "2018-09-17T09:42:00Z",
  "content" : "i'm an ABO"
};
// var https = require('https');
function indexDocument(document) {

  var endpoint = new AWS.Endpoint(domain);
  var request = new AWS.HttpRequest(endpoint, region);

  request.method = 'PUT';
  request.path += index + '/' + type + '/' + id;
  request.body = JSON.stringify(document);
  request.headers['host'] = domain;
  request.headers['Content-Type'] = 'application/json';

  var credentials = new AWS.EnvironmentCredentials('AWS');
  var signer = new AWS.Signers.V4(request, 'es');
  signer.addAuthorization(credentials, new Date());
  var client = new AWS.HttpClient();
  console.log(request.endpoint);
  client.handleRequest(request, null, function(response) {
    console.log(response.statusCode + ' ' + response.statusMessage);
    var responseBody = '';
    response.on('data', function (chunk) {
      responseBody += chunk;
    });
    response.on('end', function (chunk) {
      console.log('Response body: ' + responseBody);
    });
  }, function(error) {
    console.log('Error: ' + error);
  });
  
}
indexDocument(json_d);
var s3 = new AWS.S3({apiVersion: '2006-03-01'});
var markerKey = 'my-marker-key';
var params = {
  Bucket: 'gldv-360-wmsarchival-bucket',
  MaxKeys:2,
};
var files = [];
var one = false;
function replicateMyData(){
s3.listObjectsV2(params, function(err, data){
  if(err){
    console.log(err);
  }else{
    // console.log(data);
    files.concat(data.Contents);
    data.Contents.forEach(function(document){
      var objectParam = {
        Bucket: data.Name,
        Key: document.Key
      };
      s3.getObject(objectParam, function(err, data){
        if(err){
          console.log(err);
        }else{
          // console.log(typeof data.Body);
          var object = JSON.parse(new Buffer(data.Body).toString('utf-8'));
          console.log(typeof object);
          if(!one){
            ses.indexDocument(object);
            one = true;
          }
        }
      });
    });
    if(data.IsTruncated){
      params.ContinuationToken = data.NextContinuationToken;
      
      replicateMyData();
    }
  }
});
}
  // replicateMyData();
  callback(null, {'response':'Done'});
};