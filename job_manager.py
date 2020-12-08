import json
import subprocess
import random
from flask import Flask


app = Flask(__name__)



@app.route("/kill", methods=["POST"])
def kill():
    containers = [ 
        x.split(" ")[0]
        for x in subprocess.check_output([ "docker-compose", "ps" ]).decode().split("\n")[1:]
    ]
    killed = containers[random.randrange(len(containers))]
    subprocess.run([ "docker", "kill", killed ])
    return killed, 200


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0', debug=True)

