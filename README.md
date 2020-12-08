# CHAOS TESTING SUITE
This setup assumes you have Docker running on your machine. 
Please download Docker for your platform if you don't.
You can download it here https://www.docker.com/get-started
Also these are Linux containers so please run commnands on Linux or WSL on Windows.

With this packaged conatiner we have two servers that accepts jobs as POST requests.

 
To get up and running, open terminal and type:

```
docker-compose up --build
```

This will instatiate the docker containers and startup the servers. They will remain running in the background.

You can send sample jobs to either server by typing these commands in another terminal instance:

For server_1:

```
curl -X POST -d '{"name": "pie","action": "kpansh"}' \-H  'Content-Type: application/json' \localhost:5000/add_job
```

For server_2:

```
curl -X POST -d '{"name": "pie","action": "kpansh"}' \-H  'Content-Type: application/json' \localhost:5004/add_job
```

Our system works! 

Now lets add some chaos, install pipenv and make:

```
 pip install pipenv
 sudo apt install make
 ```


 Then:

 ```
 make
 ```

 The above command will run an engine that can manage our jobs

 To kill a random container, send this request:

 ```
curl -X POST -d '{"name": "pie","action": "kpansh"}' \-H  'Content-Type: application/json' \localhost:8080/kill
```

