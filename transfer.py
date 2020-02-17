from flask import Flask, jsonify, request
from syncrepository import getDestinationServer 
from ftplib import FTP 
import os
import fileinput

app = Flask(__name__)

# @app.route("/transfer", methods=["GET"])
def transfer():
    # img_location = request.json("pic_location")
    # source_server_name = request.json("source_server_name")
    # destination_server = getDestinationServer(source_server_name)
    ftp = FTP()
    ftp.connect('localhost', 1026) 
    ftp.login('user','1234567')
    ftp.cwd('/')
    localfile ="getrequest.py"
    fp = open(localfile, 'rb')
    ftp.storbinary('STOR %s' % os.path.basename(localfile), fp, 1024)
    fp.close
    return

# if(__name__ == '__main__'):
    # app.run(port=8081)
transfer()
