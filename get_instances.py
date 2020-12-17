import boto3
import sys

def get_instances():
    # Establish an EC2 session
    ec2 = boto3.client("ec2", "ap-southeast-2")

    # Store the running instances here
    running_instances = []

    # Get the list of running instances
    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}], MaxResults=123, DryRun=False)

    # Iterate through the object, store the results in the 'running_instances' list
    for instance in instances["Reservations"][0]["Instances"]:
        if "InstanceId" in instance:
            running_instances.append(instance["InstanceId"])

    # Return the objects for use later
    for instance in running_instances:
        return instance

def stop_instances():
    # Establish EC2 session
    ec2 = boto3.client("ec2", "ap-southeast-2")

    # Store the running instances here    
    running_instances = get_instances()

    #Shut the instances down    
    ec2.stop_instances(InstanceIds=[running_instances],DryRun=False)

if __name__ == "__main__":
    # The Main method
    get_instances()
    stop_instances()