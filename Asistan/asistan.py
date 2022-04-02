# Asistan Konuştuktan 1 Saniye  Sonra Sizde Konuşun, Yoksa Sizi Anlamayacaktır
import os
import sys
import random 
import webbrowser
import time
import datetime
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr



#Sistem Hataları İçin Gerekli Olan Kodlar
def record(ask = False):
    c = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = c.listen(source)
        voice = ''
        try:
            voice = c.recognize_google(audio, language='tr')
        
        except sr.RequestError():
            speak('yanlış giden bir şeyler var')
            
        return voice



#Asistan ile Konuşmak İçin
def response(voice):
    import datetime
    while True:
        global szlr
        szlr = ['Ders çalışırken müzik dinleyemiyorum, ders dikkatimi dağıtıyor','Kurbağalar niye mayo giymezler, Zıpladıklarında düşmesin diye','Kirpiler nasıl uyur?Diken üstünde']        
        
            
        if 'nasılsın' in voice:
            speak('iyiyim saol')
            break

    

        if 'Canım sıkıldı'  in voice:
            rs = record('yapabilceğim bişey var mı')
                

            if (rs == 'var'):
                nn = record('seni mutlu etmek için yapabilceğim ne var ')

                if nn == 'şaka' :
                    lf = random.choice(szlr)
                    speak(lf)
                    break
                    
                if nn == 'yok':
                    speak('ben gidiyorum görüşürüz')
                    break
                    sys.exit()
            
            if rs == 'yok':
                break
                sys.exit()




        if 'saat kaç' in voice:
            suan = datetime.datetime.year()
            speak(suan)
            break


        if 'şaka yap'  in voice:
            
            lf = random.choice(szlr)
            speak(lf)
            break


        if 'arama yap' in voice:
            search = record('ne aramak istersin')
            url = 'https://google.com/search?q='+ search 
            webbrowser.get().open(url)
            speak(search + ' Arama İçin Bulduklarım')
            break

        
        if 'şarkı aç' in voice:       
            sarki = record('hangi şarkıyı açmamı istersin')
            ur = 'https://www.youtube.com/search?q=' + sarki
            webbrowser.get().open(ur)
            speak(sarki + 'İçin Bulduklarım ')
            break

        
        if 'adın ne' in voice:
            global name 
            name = record('benim adım asistan peki senin adın ne')
            speak('menmun oldum {}'.format(name))
            break
        
        

        if 'adım ne' in voice:
            speak('sen sana {} dememi istedin'.format(name))
            break
        

        if 'hobin ne' in voice:
            speak('insanlara yardım etmek')
            break

        
        if 'nerelisin' in voice:
            speak('ben sadece sanal bi asistanım')
            break


        if 'yardım eder misin' in voice:
            pg = record('ne hakkında yardım istersin')
            
            # try:
            #     if pg == 'klosör oluştur':
            #         speak('lütfen dizin seç')
            #         dizin = os.chdir(input('lütfen dizin seç'))
            #         prgrm = record('hangi isimde oluşturmamı  istersin')
            #         speak('{} oluşturuluyor'.format(prgrm))
            #         os.mkdir(prgrm)
            # except FileNotFoundError:
            #         speak('Geçersiz Dizin')

            
            if pg == 'ayarlar':
                os.system("start ms-settings:")



        if 'görüşürüz'  in voice:
            speak('kendine iyi bak')
            sys.exit()



#Asistanın Sesi Her Kaydedildiğinde Eski Ses İle Çakışmaması İçin 1 ile 10000 Arasında Random Başlık Veriyoruz
def speak(string):
    ss = gTTS(string,lang = 'tr')
    rand = random.randint(1, 10000)
    file = 'audio-'+str(rand)+'.mp3'
    ss.save(file)
    playsound(file)
    os.remove(file)




speak('Nasıl Yardımcı Olabilirim')
time.sleep(0.5)
while True:


    voice = record()
    print(voice)
    response(voice)        