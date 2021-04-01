import handler as hd
import db

from flask import Flask, jsonify, render_template, request, redirect, url_for
app = Flask(__name__,  template_folder='templates')

@app.route("/", methods=['GET'])
def primeiro_endpoint_get():
  a = {"id": 1, "name": "Alexandre Vardai", "cellphone_number": "123"}
	return render_template('./index.html', navigation=a)

#TODO: solve sqlite db problem, maybe migrate to dynamoDB
@app.route("/create", methods=['POST'])
def create():
    return jsonify(message="TESTANDO")
