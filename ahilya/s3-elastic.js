var AWS = require('aws-sdk');
uploadObject: var region='us-east-1';
var domain='https://search-open-es-search-mjlstj7e56bmyossebif2inaeu.us-east-1.es.amazonaws.com';
var index='node-test';
var type='_doc';
var id =1;
var json={
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

module.exports = {
  
indexDocument: function indexDocument(document) {
  var endpoint = new AWS.Endpoint(domain);
  var request = new AWS.HttpRequest(endpoint, region);

  request.method = 'PUT';
  request.path += index + '/' + type + '/' + id;
  request.body = JSON.stringify(document);
  request.headers['Content-Type'] = 'application/json';

  var credentials = new AWS.EnvironmentCredentials('AWS');
  var signer = new AWS.Signers.V4(request, 'es');
  signer.addAuthorization(credentials, new Date());
  var client = new AWS.HttpClient();
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
};