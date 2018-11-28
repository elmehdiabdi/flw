# MOM Notes : 
  - for create, use `ansible-playbook ./src/rds.yml --tags "load,create" -vvv > src/logs/create.log`
  - for anything else, use `ansible-playbook ./src/rds.yml --tags "describe|start|stop|<anything>"`

## Points before start
> Setting Retention period 0 indicates that it's not a automated backup, change it manually
> Backup window and maintainence window should be length of 30 minutes least
> Valid A_types are prod and dev
> Storage types are (standard | gp2 | io1)
> Port valid value should be from this range 1150-65535
> IOPS constrains : Constraints: Must be a multiple between 1 and 50 of the storage amount for the DB instance.

## IOPS has to be integrated, because I was not having IOPS available account
## Pre-requists
	boto with python - python2 (alreayd in reahat), create a small installation task in this playbook itself
	pip, pip install boto, boto3, botocore
	ansible, yum install ansible


## First instrcution,
 - Job is scheduled on the basis of tag and template for example I want to create a database the use
 	> ansible-playbook rds.yml --tags "load, create"
 	If I want to modify database
 	> ansible-playbook rds.yml --tags "load, modify"
 - Both operations use same template file so sample template for the creating/modifying is in samples. You have to write configurations and put your JSON in the `vars/template.json` file

## Parameters to remember
1. DB-Engine Type - mariadb
					MySQL
					oracle-se1
					oracle-se2
					oracle-se
					oracle-ee
					sqlserver-ee
					sqlserver-se
					sqlserver-ex
					sqlserver-web
					postgres
					aurora

2. Regions - 
			Region Name 					Region 							Endpoint 						Protocol 	Amazon Route 53 Hosted Zone ID*
			US East (Ohio) 					us-east-2 			apigateway.us-east-2.amazonaws.com 			HTTPS 			ZOJJZC49E0EPZ
			US East (N. Virginia) 			us-east-1 			apigateway.us-east-1.amazonaws.com 			HTTPS 			Z1UJRXOUMOOFQ8
			US West (N. California) 		us-west-1 			apigateway.us-west-1.amazonaws.com 			HTTPS 			Z2MUQ32089INYE
			US West (Oregon) 				us-west-2 			apigateway.us-west-2.amazonaws.com 			HTTPS 			Z2OJLYMUO9EFXC
			Asia Pacific (Mumbai) 			ap-south-1 			apigateway.ap-south-1.amazonaws.com 		HTTPS 			Z3VO1THU9YC4UR
			Asia Pacific (Osaka-Local)** 	ap-northeast-3 		apigateway.ap-northeast-3.amazonaws.com 	HTTPS 			Z2YQB5RD63NC85
			Asia Pacific (Seoul) 			ap-northeast-2 		apigateway.ap-northeast-2.amazonaws.com 	HTTPS 			Z20JF4UZKIW1U8
			Asia Pacific (Singapore) 		ap-southeast-1 		apigateway.ap-southeast-1.amazonaws.com 	HTTPS 			ZL327KTPIQFUL
			Asia Pacific (Sydney) 			ap-southeast-2 		apigateway.ap-southeast-2.amazonaws.com 	HTTPS 			Z2RPCDW04V8134
			Asia Pacific (Tokyo) 			ap-northeast-1 		apigateway.ap-northeast-1.amazonaws.com 	HTTPS 			Z1YSHQZHG15GKL
			Canada (Central) 				ca-central-1 		apigateway.ca-central-1.amazonaws.com 		HTTPS 			Z19DQILCV0OWEC
			China (Beijing) 				cn-north-1 			apigateway.cn-north-1.amazonaws.com.cn 		HTTPS 			None
			China (Ningxia) 				cn-northwest-1 		apigateway.cn-northwest-1.amazonaws.com.cn 	HTTPS 			None
			EU (Frankfurt) 					eu-central-1 		apigateway.eu-central-1.amazonaws.com 		HTTPS 			Z1U9ULNL0V5AJ3
			EU (Ireland) 					eu-west-1 			apigateway.eu-west-1.amazonaws.com 			HTTPS 			ZLY8HYME6SFDD
			EU (London) 					eu-west-2 			apigateway.eu-west-2.amazonaws.com 			HTTPS 			ZJ5UAJN8Y3Z2Q
			EU (Paris) 						eu-west-3 			apigateway.eu-west-3.amazonaws.com 			HTTPS 			Z3KY65QIEKYHQQ
			South America (São Paulo) 		sa-east-1 			apigateway.sa-east-1.amazonaws.com 			HTTPS 			ZCMLWB8V5SYIT

3. Naming Convention for Instance  - 
```
	for postgres Dev instance, the rds instance name should be like : post-<name>-dev
	for postgres Prod instance, the rds instance name should be like : post-<name>-prd 

	for SQL Server Dev instance, the rds instance name should be like : sqls-<name>-dev
	for SQL Server Prod instance, the rds instance name should be like : sqls-<name>-prd
```

4. Size - <number> in GB

5. Version - version of the database, refer [here](https://aws.amazon.com/rds/faqs/)
	Example - 10.5 for posgres

6. Instance Type - Optional for modify/replicate/restore, required in create (example: db.m1.small)

7. Username and Password - (master) - your convension :)

8. iops > 1000

9. Licence Model - Select any of the licence type
					license-included
					bring-your-own-license
					general-public-license
					postgresql-license

10. Maintance Window - ddd:hh24:mi-ddd:hh24:mi
11. Multi Zone - specifie whether deployment is multizone or not (yes/no) (create/modify)
12. New Instance Name - for modifying 
13. Option Group - the group you want to use for this RDB
14. Parameter Group - associate parameter group to a DB instance. (Create/Modify)
15. Port Number - only when you create 
			conventional ports - 	3306 for mysql, 
									1521 for Oracle, 
									1433 for SQL Server,
									5432 for PostgreSQL.
16. Security groups - Comma separated list (Create/Modify)
17. Public accessibility - (Create) - can be changed by replication
18. Subnet - standard entry point
19. Tags - A dict format {'me': 'not', 'another': 'ok'} (Create)
20. Minor Upgrade - (yes/no) 10.5 -> 10.5.7 (Create)
21. Wait - (yes/no) wait to db come in available state ?
22. Wait Time - time to wait for above operation - in seconds
23. Zone - example us-east-1b, check through health status and configure this

For modifying, you can choose your operations latency, instant or queue through apply immediately option (yes/no)