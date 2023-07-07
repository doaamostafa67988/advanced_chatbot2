## Import Libraries, and read the key-token
import openai
import os
from dotenv import load_dotenv
import time

## Load the Key token
_ = load_dotenv()
key_token = os.getenv('OpenAI_KEY_TOKEN')

## Assign that key_token to api_key of OpenAI
openai.api_key = key_token


## Looping to make it much more easier
all_messages = list()
'''
you are ai assistant answer only in these feilds computer science and 
all programming languges for example java ,python, c# . do not answer any question not related to these topics(progamming languge - computer science - software engineering )
'''
## Create system prompt
system_prompt = '''You are an AI specialized in Mentor. Please ask me anything related to software engineering.'''
all_messages.append({'role': 'system', 'content': system_prompt})
os.makedirs('audio', exist_ok=True)
#AUDIO_FOLDER_PATH = os.path.join(os.getcwd(), 'audio')
def rename_audio(filename):
    audio_path_old = os.path.join('audio/',filename)
    print(1)
    basename_old = os.path.basename(audio_path_old)
    name_old, exten_old = os.path.splitext(basename_old)
    name_old = name_old.lower().replace(' ', '-')

    ## From mp4 to mp3 and 
    audio_path_new = f'{name_old}.mp3'
    audio_path_new = os.path.join(os.getcwd(), 'audio', audio_path_new)
    os.rename(audio_path_old, audio_path_new)
            ## Rename the audio file
    

   
    return audio_path_new
## ------------------------------ Call the API -------------------------------- ##

def custom_chatbot(user_prompt:str=None,destination:str=None):
    
    if destination:
            ## Call the above function
            audio_path=rename_audio(destination)
            
            ## Trancribe if the language is_english else translate to english
            
                ## Transcrip using whipser
            with open(audio_path, 'rb') as file:
                transcribt = openai.Audio.transcribe('whisper-1', file)
                print(2)
            
           
            ## delete the audio file
            os.remove(audio_path)
            user_prompt=str(transcribt)
            print(user_prompt)
            
  
    
    ## Looping while true
    while True:
        
    
     
        print(4)
              
        ## If the user wants to exit the chatbot -> break
        if user_prompt.lower() in ['quit', 'exit', 'ex', 'out', 'escape']:
            time.sleep(2)  ## wait 2 seconds

            ## If the user exit the chatbot, Clear it.
            all_messages.clear()
            return 'Thanks for using my ChatBot'
        
        ## If the user doesn't write any thing -> Continue
        elif user_prompt.lower() == '': 
            continue

        ## Answer
        else:
            print(5)
            
            ## append the question of user to message as a user roke
            all_messages.append({'role': 'user', 'content': user_prompt})
            
            ## Call the API
            each_response = openai.ChatCompletion.create(
                            model='gpt-3.5-turbo',           
                            messages=all_messages,
                            temperature=0.7,  
                            max_tokens=2048,   
                                )
            each_response = each_response['choices'][0]['message']['content']
            print(6)
            
            ## We must append this respond to the messages
            all_messages.append({'role': 'assistant', 'content': each_response})
            print(7)
    
            return each_response  ## return the response of the api
    
            
