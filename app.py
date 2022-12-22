from flask import Flask,request
app = Flask(__name__)
import socket       
import os

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/getip")
def getip():
    hostname=socket.gethostname()     #Desktop Name
    IP_ADDRESS =socket.gethostbyname(hostname) #  IP Adress
    print("IP Address is:"+IP_ADDRESS) 
    return f"MY ip address is {IP_ADDRESS}""

@app.route('/upload')
def upload_file():
   return """<html>
                <body>
                    <form action = "http://localhost:5000/object_count" method = "POST" 
                        enctype = "multipart/form-data">
                        <input type = "file" name = "file" />
                        <input type = "submit"/>
                    </form>
                </body>
            </html>"""

@app.route("/object_count",methods=["POST"])
def find_obj_count():
    if request.method == "POST":
        f = request.files['file']
        f.save(f.filename)
        import subprocess
        os.chdir("./yolov4-deepsort")
        print(os.getcwd())
        cmd = f'python object_tracker.py --weights ./checkpoints/yolov4-tiny-416 --model yolov4 --video ../{f.filename} --output ../{f.filename.split(".")[0]}_tiny.avi --tiny --count'

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
        out, err = p.communicate() 
        result = str(out).split('\n')
        return f"""<html><body>
                <h1> total no of objects in image is {result[-1].strip().split()[-1][:-5]} <h2>
                </body>
                </html>
                """
