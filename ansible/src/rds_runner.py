import boto3
import sys
import json
import os
import logging as logger


def get_client(aws_skey, aws_akey, region):
    client = boto3.client('rds', aws_access_key_id=aws_akey, aws_secret_access_key=aws_skey, region_name=region)
    return client


def file_loader(file_name):
    myfile = open(file_name, 'r')
    data = myfile.read()
    return json.loads(data)


def create():
    pass


def log_request(request_data):
    logger.info('******************************************************** DB modify request *********************************************************************')
    logger.info(request_data)


def log_response(response):
    logger.info('******************************************************** DB modify response ********************************************************************')
    logger.info(response)


def modify():
    configs = file_loader(os.path.dirname(os.path.abspath(__file__)) + '/vars/confs/modify.json')
    request_data = {}
    if not configs['INSTANCE_NAME']:
        print('Instance name is missing, please check modify.json file')
    else:
        request_data["DBInstanceIdentifier"] = configs['INSTANCE_NAME']

    if configs['SIZE']:
        request_data['AllocatedStorage'] = configs['SIZE']

    if configs['DB_CLASS']:
        request_data['DBInstanceClass'] = configs['DB_CLASS']

    if configs['SUBNET']:
        request_data['DBSubnetGroupName'] = configs['SUBNET']

    if configs['SECURITY_GROUPS'] and len(configs['SECURITY_GROUPS']) > 0:
        request_data['DBSecurityGroups'] = configs['SECURITY_GROUPS']

    if configs['VPC_SECURITY_GROUPS'] and len(configs['VPC_SECURITY_GROUPS']) > 0:
        request_data['VpcSecurityGroupIds'] = configs['VPC_SECURITY_GROUPS']

    if configs['APPLY_IMD'] is not None:
        request_data['ApplyImmediately'] = configs['APPLY_IMD']

    if configs['PASSWORD']:
        request_data['MasterUserPassword'] = configs['PASSWORD']

    if configs['PARAMETER_GROUP']:
        request_data['DBParameterGroupName'] = configs['PARAMETER_GROUP']

    if configs['BACKUP_RETENTION']:
        request_data['BackupRetentionPeriod'] = configs['BACKUP_RETENTION']

    if configs['BACKUP_WINDOW']:
        request_data['PreferredBackupWindow'] = configs['BACKUP_WINDOW']

    if configs['MAINTENANCE_WINDOW']:
        request_data['PreferredMaintenanceWindow'] = configs['MAINTENANCE_WINDOW']

    if configs['MULTI_ZONE'] is not None:
        request_data['MultiAZ'] = configs['MULTI_ZONE']

    if configs['DB_VERSION']:
        request_data['EngineVersion'] = configs['DB_VERSION']

    if configs['ALLOW_MAJOR'] is not None:
        request_data['AllowMajorVersionUpgrade'] = configs['ALLOW_MAJOR']

    if configs['ALLOW_MINOR'] is not None:
        request_data['AutoMinorVersionUpgrade'] = configs['ALLOW_MINOR']

    if configs['LICENSE_MODEL']:
        request_data['LicenseModel'] = configs['LICENSE_MODEL']

    if configs['OPTION_GROUP']:
        request_data['OptionGroupName'] = configs['OPTION_GROUP']

    if configs['NEW_NAME']:
        request_data['NewDBInstanceIdentifier'] = configs['NEW_NAME']

    if configs['STORAGE_TYPE']:
        request_data['StorageType'] = configs['STORAGE_TYPE']

    if configs['PUBLICLY_ACCESSIBLE'] is not None:
        request_data['PubliclyAccessible'] = configs['PUBLICLY_ACCESSIBLE']

    if configs['PORT']:
        request_data['DBPortNumber'] = configs['PORT']

    if configs['IOPS']:
        request_data['Iops'] = configs['IOPS']

    print(
        '******************************************************** DB modify request *********************************************************************')
    print(request_data)
    log_request(request_data)
    client = get_client(configs['AWS_SECRET_KEY'], configs['AWS_ACCESS_KEY'], configs['AWS_REGION'])
    response = client.modify_db_instance(**request_data)
    print(
        '******************************************************** DB modify response ********************************************************************')
    print(response)
    log_response(response)


def reboot():
    configs = file_loader(os.path.dirname(os.path.abspath(__file__)) + '/vars/confs/reboot.json')
    print(configs)
    request_data = {}
    if configs['INSTANCE_NAME']:
        request_data['DBInstanceIdentifier'] = configs['INSTANCE_NAME']

    if configs['FORCE_FAILOVER'] is not None:
        request_data['ForceFailover'] = configs['FORCE_FAILOVER']

    print(
        '******************************************************** DB modify request *********************************************************************')
    print(request_data)
    log_request(request_data)
    client = get_client(configs['AWS_SECRET_KEY'], configs['AWS_ACCESS_KEY'], configs['AWS_REGION'])
    response = client.reboot_db_instance(**request_data)
    print(
        '******************************************************** DB modify response ********************************************************************')
    print(response)
    log_response(response)


def stop():
    configs = file_loader(os.path.dirname(os.path.abspath(__file__)) + '/vars/confs/stop.json')
    print(configs)
    request_data = {}
    if configs['INSTANCE_NAME']:
        request_data['DBInstanceIdentifier'] = configs['INSTANCE_NAME']

    if configs['SNAPSHOT_NAME'] is not None:
        request_data['DBSnapshotIdentifier'] = configs['SNAPSHOT_NAME']

    print(
        '******************************************************** DB modify request *********************************************************************')
    print(request_data)
    log_request(request_data)
    client = get_client(configs['AWS_SECRET_KEY'], configs['AWS_ACCESS_KEY'], configs['AWS_REGION'])
    response = client.stop_db_instance(**request_data)
    print(
        '******************************************************** DB modify response ********************************************************************')
    print(response)
    log_response(response)


def delete():
    configs = file_loader(os.path.dirname(os.path.abspath(__file__)) + '/vars/confs/delete.json')
    print(configs)
    request_data = {}
    if configs['INSTANCE_NAME']:
        request_data['DBInstanceIdentifier'] = configs['INSTANCE_NAME']

    if configs['SKIP_FINAL_SNAPSHOT'] is not None:
        request_data['SkipFinalSnapshot'] = configs['SKIP_FINAL_SNAPSHOT']

    if configs['FINAL_DB_SNAPSHOT_ID']:
        request_data['FinalDBSnapshotIdentifier'] = configs['FINAL_DB_SNAPSHOT_ID']

    print(
        '******************************************************** DB modify request *********************************************************************')
    print(request_data)
    log_request(request_data)
    client = get_client(configs['AWS_SECRET_KEY'], configs['AWS_ACCESS_KEY'], configs['AWS_REGION'])
    response = client.delete_db_instance(**request_data)
    print(
        '******************************************************** DB modify response ********************************************************************')
    print(response)
    log_response(response)


def start():
    configs = file_loader(os.path.dirname(os.path.abspath(__file__)) + '/vars/confs/start.json')
    print(configs)
    request_data = {}
    if configs['INSTANCE_NAME']:
        request_data['DBInstanceIdentifier'] = configs['INSTANCE_NAME']

    print(
        '******************************************************** DB modify request *********************************************************************')
    print(request_data)
    log_request(request_data)
    client = get_client(configs['AWS_SECRET_KEY'], configs['AWS_ACCESS_KEY'], configs['AWS_REGION'])
    response = client.start_db_instance(**request_data)
    print(
        '******************************************************** DB modify response ********************************************************************')
    print(response)
    log_response(response)


def describe():
    configs = file_loader(os.path.dirname(os.path.abspath(__file__)) + '/vars/confs/describe.json')
    print(configs)
    request_data = {}
    if configs['INSTANCE_NAME']:
        request_data['DBInstanceIdentifier'] = configs['INSTANCE_NAME']
    elif configs['KEY'] and configs['VALUES']:
        request_data['Filters'] = [{'Name': x, 'Values': y} for x in configs['KEY'] for y in configs['VALUES']]

    print(
        '******************************************************** DB modify request *********************************************************************')
    print(request_data)
    log_request(request_data)
    client = get_client(configs['AWS_SECRET_KEY'], configs['AWS_ACCESS_KEY'], configs['AWS_REGION'])
    response = client.describe_db_instances(**request_data)
    print(
        '******************************************************** DB modify response ********************************************************************')
    print(response)
    log_response(response)


def restore():
    pass


def snapshot():
    pass


if __name__ == '__main__':
    tasks = sys.argv[1:]
    # logger.path_render = os.path.dirname(os.path.abspath(__file__)) + '/vars/confs/modify.json'
    # logger.init(__name__)
    for task_name in tasks:
        file_path = os.path.dirname(os.path.abspath(__file__)) + '/logs/' + task_name + '.log'
        FORMAT = '%(asctime)-15s %(message)s'
        logger.basicConfig(filename=file_path, level=logger.INFO, format=FORMAT)
        print(task_name + 'ing..........')
        logger.info(task_name + 'ing...........')
        if task_name == 'create':
            create()
        elif task_name == 'modify':
            modify()
        elif task_name == 'reboot':
            reboot()
        elif task_name == 'delete':
            delete()
        elif task_name == 'start':
            start()
        elif task_name == 'stop':
            stop()
        elif task_name == 'describe':
            describe()
        elif task_name == 'restore':
            restore()
