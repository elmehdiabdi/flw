1. Create a simple API Gateway on the AWS with GET support.
Follow screenshot step1-4
2. Create a simple lambda function with nodejs@6.10 and choose compromising role like admin or (es + vpc + s3 + lambda). Don't forget to set lambda timeout to 1 minute or so on
3. Paste the code to the lambda function, given in the requir.sj file
4. Go back to the API gateway and select newly created APi endpoint
5. Follow the step5-6
	P.S: in the Lambda Function selection, choose the correct lambda for API Gateway integration
6. Go to the Method Request
	a. Choose Request Validator : Validate Query string parameters and headers
	b. In URL Query String Parameters , add query string parameter : q
	c. See Step7.png
7. Go to the Integration request tab
	a. Go to the Mapping Templates and add mapping template
		i. Set content-type : application/json
		ii. Add following template and save
		
		{
    		"q":"$input.params('q')"
		}

8. And then deploy the API from Actions drop down


For the testing, just use URL like this
https://<your-host>/<stage-name>?q=<your-query-text> or <your-api-endpoint>?q=<your-query>
example : https://5xk08ekugd.execute-api.us-east-1.amazonaws.com/dev?q=Kidman