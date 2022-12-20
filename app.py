from flask import Flask
app = Flask(__name__)
import socket       

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/getip")
def getip():
    hostname=socket.gethostname()     #Desktop Name
    IP_ADDRESS =socket.gethostbyname(hostname) #  IP Adress
    print("IP Address is:"+IP_ADDRESS) 
    return f"MY ip address is {IP_ADDRESS}"
