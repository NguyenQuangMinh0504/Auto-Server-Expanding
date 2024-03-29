from collections.abc import Iterable
from google.cloud import compute_v1


def list_instances(project_id: str, zone: str) -> Iterable[compute_v1.Instance]:
    """
    List all instances in the given zone in the specified project.

    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        zone: name of the zone you want to use. For example: “us-west3-b”
    Returns:
        An iterable collection of Instance objects.
    """
    instance_client = compute_v1.InstancesClient()
    instance_list = instance_client.list(project=project_id, zone=zone)

    print(type(instance_list))

    print(f"Instances found in zone {zone}:")
    for instance in instance_list:
        print(f" - {instance.name} ({instance.machine_type})")

    return instance_list


if __name__ == "__main__":
    list_instances(project_id="my-website-387704", zone="us-central1-a")
    client = compute_v1.DisksClient()
    print(client.list(zone="us-central1-a", project="my-website-387704"))
