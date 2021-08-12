# imports
import re
from fastapi import FastAPI

app = FastAPI()

# define dict with numbers translated to morse
morse_nums = {'1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....','6':'-....',
              '7':'--...', '8':'---..', '9':'----.','0':'-----', '.':'.-.-.-'}


@app.get("/{ip}")
async def morse_translate(ip, morse_nums):
    # Basic string check 
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip):
        morseip = ""
        for char in ip:
            morseip = morseip + morse_nums[char]
        return {"morse_ip" : morseip}
    else:
        return {"Error" : "invalid IP address"}