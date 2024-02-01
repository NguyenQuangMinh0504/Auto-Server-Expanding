from google.cloud import compute_v1

attached_disk = compute_v1.AttachedDisk()

attached_disk_initialize_param = compute_v1.AttachedDiskInitializeParams()
attached_disk_initialize_param.disk_size_gb = 10
attached_disk_initialize_param.source_image = "projects/debian-cloud/global/images/debian-12-bookworm-v20240110"

attached_disk.boot = True
attached_disk.disk_size_gb = 10
attached_disk.auto_delete = True
attached_disk.initialize_params = attached_disk_initialize_param
