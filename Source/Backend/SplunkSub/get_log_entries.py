import splunklib.client as client
from splunklib import results

HOST = "localhost"
PORT = 8089
USERNAME = "menny"
PASSWORD = "Manuel27!"

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Create a job instance and query the first five events(log entries)
job = service.jobs.create("search * | head 5")
rr = results.ResultsReader(job.preview())

log_entries = []

for entry in rr:
    log_entries.append([entry['_serial'], entry['_raw'], entry['_time'], entry['source'], entry['_serial']])

print(log_entries)
