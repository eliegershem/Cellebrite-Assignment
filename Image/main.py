# imports
import re
from fastapi import FastAPI

app = FastAPI()

@app.get("/{ip}")
def morse_translate(ip):
    
    # define dict with numbers translated to morse
    morse_nums = {'1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....','6':'-....',
              '7':'--...', '8':'---..', '9':'----.','0':'-----', '.':'.-.-.-'}
    
    # Basic string check
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip):
        
        # Runs on each char in ip and addes morse translation to morseip
        morseip = ""
        for char in ip:
            morseip = morseip + morse_nums[char]
        return morseip
    else:
        return {"Error" : "invalid IP address"}