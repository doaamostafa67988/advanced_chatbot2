from flask import Flask, render_template
from utils import custom_chatbot 
from flask import request
from flask_cors import CORS
import random
import os
app = Flask(__name__)
CORS(app, resources={r"/": {"origins": ""}})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home():
    request.form['question']:
          
    qu=request.form['question']
    
    prediction = custom_chatbot(user_prompt=qu)
    return render_template('index.html',question=prediction,user_input=qu) 
      
            


        


        

    
if __name__ == '__main__':
    app.run(debug=True)
