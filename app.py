import os
from flask import Flask, request  
  
app = Flask(__name__)  
  
@app.route('/', methods=['GET', 'POST'])  
def index():  
    return 'hello'

@app.route('/.well-known/acme-challenge/<path:input_string>', methods=['GET'])  
def return_string(input_string): 
    challenge =''
    with open('challenge.txt','r') as f_in:
        challenge = f_in.read()
    return challenge 
    
@app.route('/save_challenge/<path:input_string>', methods=['GET', 'POST'])  
def save_challenge(input_string):  
    with open('challenge.txt','w') as f_out:
        f_out.write(input_string)
    return 'challenge string saved'
 
if __name__ == "__main__":  
    app.run(host='0.0.0.0',debug=True,port=80)
