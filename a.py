import pyttsx3

def SpeakText(command):
    engine= pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
def text_to_speech(text, gender):

    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 120)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    SpeakText(text)

