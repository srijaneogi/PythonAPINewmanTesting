import os
import docker
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-coll_run', '--coll_run')
args = parser.parse_args()
coll_run = args.coll_run

client = docker.from_env()

container = client.containers.run("mudaliar20/html:latest", "run  /etc/newman/" +coll_run+ " --ignore-redirects -r cli,json,htmlextra",volumes={os.getcwd(): {'bind': '/etc/newman/', 'mode': 'rw'}}, detach=True)
