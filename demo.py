import os
import docker

client = docker.from_env()

container = client.containers.run("mudaliar20/html:latest", "run /etc/newman/Titan.postman_collection.json --ignore-redirects -r cli,json,htmlextra",volumes={os.getcwd(): {'bind': '/etc/newman/', 'mode': 'rw'}}, detach=True)