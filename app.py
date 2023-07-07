from flask import Flask, render_template
from utils import custom_chatbot 
from flask import request
from flask_cors import CORS
import random
import os
app = Flask(__name__)
CORS(app, resources={r"/": {"origins": ""}})
prediction=None
file=None
def allowed_file(filename):
    ALLOWED_EXTS = ['mp3']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTS
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['question']:
          
            qu=request.form['question']
            
            prediction = custom_chatbot(user_prompt=qu)
            return render_template('index.html',question=prediction,user_input=qu) 
        if "file" in request.files:

            uploaded_file = request.files['file']
            #if uploaded_file and allowed_file(uploaded_file.filename):
            
            destination = os.path.join('audio/',uploaded_file.filename)
            uploaded_file.save(destination)
                
            

            file= custom_chatbot(destination=str(uploaded_file.filename))
            return render_template('index.html',file=file)
      



        


        

    
if __name__ == '__main__':
    app.run(debug=True)