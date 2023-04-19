import pyperclip3
import json
from time import sleep

pyperclip3.copy("")
sleep(1)
print(
    'create a dict.json file beside the exe file and write json for your replacement.\neg: {"a":"o","b":"k"}')

replaceDict = {"A":"А","a":"а","B":"В","b":"В","E":"Е","e":"е","K":"К","k":"К","M":"М","m":"М","H":"Н","O":"О","o":"о","P":"Р","p":"р","C":"С","c":"с","T":"Т","y":"у","X":"Х","x":"х"}

try:
    f = open("./dict.json", "r", encoding='utf-8')
    wholeText = f.read()
    f.close()
    replaceDict = json.loads(wholeText)
except:
    print("parse dict.json failed, use default.")

while 1 < 2:
    try:
        content = pyperclip3.paste(text=True)
        for key in replaceDict:
            content = content.replace(key, replaceDict[key])
        pyperclip3.copy(content)
    except:
        pass
    sleep(1)
