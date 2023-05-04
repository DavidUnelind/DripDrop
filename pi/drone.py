from flask import Flask, request
from flask_cors import CORS
import subprocess
import requests


app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'


#Give a unique ID for the drone
#===================================================================
myID = "1"
#===================================================================

# Get initial longitude and latitude the drone
#===================================================================

current_longitude = 13.20896
current_latitude = 55.71103
file = open('longlat.txt', 'w')
file.write(str(current_longitude) + "\n" + str(current_latitude))
file.close()

#===================================================================

drone_info = {'id': myID,
                'longitude': float(current_longitude),
                'latitude': float(current_latitude),
                'status': 'idle'
            }

# Fill in the IP address of the server, and send the initial location of the drone to the SERVER
#===================================================================

print(drone_info)
SERVER="http://192.168.1.3:5001/drone"
with requests.Session() as session:
    resp = session.post(SERVER, json=drone_info)
#===================================================================


@app.route('/', methods=['POST'])
def main():
    coords = request.json
    print(coords)
    # Get current longitude and latitude of the drone 
    #===================================================================
    file = open('longlat.txt', 'r')
    
    current_longitude = float(file.readline())
    current_latitude = float(file.readline())
    file.close()
    #===================================================================
    from_coord = coords['from']
    to_coord = coords['to']
    subprocess.Popen(["python3", "simulator.py", '--clong', str(current_longitude), '--clat', str(current_latitude),
                                                 '--flong', str(from_coord[0]), '--flat', str(from_coord[1]),
                                                 '--tlong', str(to_coord[0]), '--tlat', str(to_coord[1]),
                                                 '--id', myID
                    ])
    return 'New route received'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
