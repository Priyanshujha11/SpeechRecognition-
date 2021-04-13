import speech_recoginition as sr
import webbrowser as wb
chrome_path = 'C:/Program Files (x86)/Google'
r = sr.recognizer()
with sr.microphone()as source:
    print('Hi friend what you want to know')
    audio= r.listen(source)
    print('Looking for it')
5
try:
    text = r.recognize_google(audio)
    print('Looking for:\n' + text)

    f_text = 'https://www.google.com/search' + text
    wb.get( chrome_path).open(f_text)

except sr.Exception as e:
    print('could not look for it'),format(e)
