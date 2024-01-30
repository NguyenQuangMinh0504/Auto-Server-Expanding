from google.cloud.monitoring_v3.query import Query
from google.cloud.monitoring_v3 import MetricServiceClient


from datetime import datetime
client = MetricServiceClient()
now = datetime.now()

print(Query(client=client, project="my-website-387704", end_time=datetime.now(), minutes=15).as_dataframe())
