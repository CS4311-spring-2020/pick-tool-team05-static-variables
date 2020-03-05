import os
import splunklib.client as client

# Hardcoded path
path = "C:\\Users\\mdelgado\\Desktop\\Log Examples"

# Constants created with log-in information
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

# Create a oneshot input

# Retrieve the index for the data
currentIndex = service.indexes["main"]

for filename in os.listdir(path):

    # Upload and index the file
    currentIndex.upload(path + "\\" + filename)


