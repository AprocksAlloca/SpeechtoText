import speech_recognition as sr
from datetime import datetime
import streamlit as st



st.markdown("<h1 style='text-align: center;'>Speech To Text</h1>", unsafe_allow_html=True)

start = st.button("Start Recording")
stop = st.button("Stop Recording")
st.write(start)
st.write(stop)
r = sr.Recognizer()


    
if start== True:
    stop = False
    while True:
        with sr.Microphone(device_index=0) as source:
            print("Listening")
            audio = r.listen(source)
            print("Converting...")
            try:
                text = r.recognize_google(audio).capitalize()
                print(text)
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                text[0].capitalize()
                st.write(dt_string+" : "+"\"" +text+"\""+"\n")
                #file = open('Data.txt', 'a')
                #file.writelines(dt_string+" : "+"\"" +text+"\""+"\n")
                #file.close()
            except:
                st.write("**Unable to understand audio**")
    

if stop== True:
    start = False 

