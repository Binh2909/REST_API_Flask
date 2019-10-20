from flask import Flask, jsonify, request
import csv
import json

#import objects from the Flask model
app = Flask(__name__) #define app using Flask

file_path='C:\\Users\\BinBin\\testing\\data.json'

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})
	
@app.route('/info', methods=['GET'])
def returnAll():
	return jsonify(load_json(file_path))

@app.route('/info/cars', methods=['GET'])
def returnName():
	list = []
	array= load_json(file_path)
	list.append(array['cars'])
	return jsonify(list[0])
	#if array['name'] == name:
	#	return jsonify({'name' : array['name']})
	#return jsonify({'message' : "Bad Request!!!" })
	
@app.route('/info/cars/<string:name>', methods=['GET'])
def returnOne(name):
	array= load_json(file_path)
	data = [arr for arr in array['cars'] if arr['model'] == name]
	print(type(array))
	return jsonify(data[0])

@app.route('/info/cars', methods=['POST'])
def addOne():
	add_info = {'model' : request.json['model'], 'mpg' : request.json['mpg']}
	print(type(add_info))
	array= load_json(file_path)
	#array.append(add_info)
	array['cars'].append(add_info)
	return jsonify(array)

@app.route('/info/cars/<string:name>', methods=['PUT'])
def editOne(name):
	array= load_json(file_path)
	data = [arr for arr in array['cars'] if arr['model'] == name]
	data[0]['model'] = request.json['model']
	data[0]['mpg'] = request.json['mpg']
	return jsonify(data[0])

@app.route('/info/cars/<string:name>', methods=['DELETE'])
def removeOne(name):
	array= load_json(file_path)
	data = [arr for arr in array['cars'] if arr['model'] == name]
	array['cars'].remove(data[0])
	return jsonify(array['cars'][0])
	
def load_json(file):
   with open(file) as f:
        return(json.loads(f.read()))	
	
if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode