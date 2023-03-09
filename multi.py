from speech_recognition import Microphone, Recognizer, UnknownValueError, RequestError
from time import sleep

def callback(recognizer, source):
    try: 
        recognized = recognizer.recognize_google(source)
        print("You said: ", recognized)

    except RequestError as exc:
        print(exc)
    except UnknownValueError:
        print("Unable to recognize")

def listen():
    recog = Recognizer()
    mic = Microphone()

    with mic:
        recog.adjust_for_ambient_noise(mic)

    print("Talk")
    recog.listen_in_background(mic, callback, phrase_time_limit=10)




if __name__ == '__main__':

    listen()
    
    while True:
        pass