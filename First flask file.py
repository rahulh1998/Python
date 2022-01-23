
#### This file acts as a server

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/Flask__1',methods =['POST']) # Flask__1 is the name of the call used in url
def first_flask_via_postman():
    if(request.method == "POST"):
        n1 = int(request.json['n1']) # .json is the input type of the values we give in postman
        n2 = int(request.json['n2'])
        result = 'Multiplication of '+ str(n1) + ' & ' + str(n2) + ' is   :     ' + str(n1*n2)
        return jsonify(result)

@app.route('/Flask__2',methods = ['POST'])
def sec_flask_via_pm():
    if (request.method == 'POST'):
        operation = request.json['operation']
        n1 = int(request.json['n1'])
        n2 = int(request.json['n2'])

        if (operation == 'add'):
            r = n1 + n2
        if (operation == 'sub'):
            r = n1 - n2
        if (operation == 'mul'):
            r = n1 * n2
        return jsonify(operation + ' of '+ str(n1) + " & " + str(n2) + ' is ' + str(r)) # Everything needs to be in string

@app.route('/Flask__3') # http://127.0.0.1:5000/Flask__3?n1=6&n2=8
def url_test():
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    n = int(n1) * int(n2)
    result = '''<h1 >Multiplication of {} & {} = :  {} </h1>'''.format(n1,n2,n)
    return result
if __name__ == '__main__': # calling the constructor sort of operation
    app.run()