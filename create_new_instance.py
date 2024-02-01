from google.cloud import compute_v1

from disk import attached_disk
from network_interface import network_interface
zone = "us-central1-a"
machine_type = "e2-micro"

client = compute_v1.InstancesClient()
new_instance = compute_v1.Instance()

print(dir(attached_disk))
print(type(attached_disk.source))
new_instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
new_instance.name = "test-instance"
new_instance.disks = [attached_disk]
new_instance.network_interfaces = [network_interface]
insert_request = compute_v1.InsertInstanceRequest()
project_id = "my-website-387704"
insert_request.project = project_id
insert_request.zone = zone
insert_request.instance_resource = new_instance
client.insert(request=insert_request)
