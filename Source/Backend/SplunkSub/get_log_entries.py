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
for result in rr:
    if isinstance(result, results.Message):
        # Diagnostic messages may be returned in the results
        print('%s: %s' % (result.type, result.message))
    elif isinstance(result, dict):
        # Normal events are returned as dicts
        print(result)
if rr.is_preview:
    print("Preview of a running search job.")
else:
    print("Job is finished. Results are final.")