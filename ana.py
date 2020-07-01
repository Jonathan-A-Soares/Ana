# -*- coding: utf-8 -*-
import speech_recognition as sr
from gtts import gTTS
import datetime
from subprocess import call

##### configurações #####

hotword = 'ana'
with open('config/sistema-intelige-1537185170980-b86ebc917520.json') as credenciais_google:
    credenciais_google = credenciais_google.read()


##### funções principais #####

def monitora_audio():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:

        while True:
            print("Estou aqui: ")
            audio = microfone.listen(source)

            try:

                trigger = microfone.recognize_google_cloud(audio, credentials_json=credenciais_google, language='pt-BR')
                trigger = trigger.lower()

                if hotword in trigger:
                    print('Comando: ', trigger)
                    responde('feedback')
                    ### fazer algo ###
                    break

            except sr.UnknownValueError:
                print("Google not understand audio")
                #responde('naoentende')

            except sr.RequestError as e:
                print("Could not request results from Google Cloud Speech service; {0}".format(e))
                responde('errodeconecao')

    return trigger   

def responde(arquivo):
    call(['ffplay','-nodisp','-autoexit','audios/'+arquivo+'.mp3'])
"""
def hora(hora1):
    tts = gTTS('agora são:'+hora1, lang='pt-br')
    tts.save('audios/hora.mp3')     
    call(['ffplay','-nodisp','-autoexit','audios/hora.mp3'])
"""
def main():
    monitora_audio()

main()