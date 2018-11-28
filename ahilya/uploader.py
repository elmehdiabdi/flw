import boto3

s3 = boto3.client('s3', aws_access_key_id='AKIAIQLJZVRYH6JNLBZA', aws_secret_access_key='zZhnsykmP6+XeU+UT659zEpwt7BVkSYncHpUdQ/t')

for i in range(200, 2000):
	s3.upload_file('dataset/'+str(i)+'.json', 'sample-elastic-dataset', str(i)+'.json')
	print('uploaded')