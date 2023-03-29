# LP3 Drone Project - Lab 2
Intall the requied Python packages, redis is added in the list
```
pip3 install -r requirements.txt
```

## On the Server Pi:
Go to `/webserver`, start your Redis server and run the two flask servers:
1. On Terminal 1, start your redis server
2. On Terminal 2, run `database.py`
```
export FLASK_APP=database.py
export FLASK_ENV=development
flask run --port=5001 --host 0.0.0.0
```
3. On Terminal 3, run `build.py`
```
export FLASK_APP=build.py
export FLASK_ENV=development
flask run --host 0.0.0.0
```
4. On Terminal 4, run `route_planner.py`
```
export FLASK_APP=route_planner.py
export FLASK_ENV=development
flask run --port=5002 --host 0.0.0.0
```

## On the Drone Pis:
You need to install the Python packages in the requirements if you havn't done any. 

Go to `/pi`, run `drone.py`
```
export FLASK_APP=drone.py
export FLASK_ENV=development
flask run --host 0.0.0.0
```

Note: Don't user `python3 build.py` to run the servers, since this does not porvide all the functionalities requied by the application.

