import speech_recognition as sr

r = sr.Recognizer()
while(1):
    with sr.Microphone() as source:
        print("Speak something:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        myText = r.recognize_google(audio)
        print("You said:", myText)

    except sr.UnknownValueError:
        print("can't hear")
    except sr.RequestError as e:
        print("could not request; (0)".format(e))