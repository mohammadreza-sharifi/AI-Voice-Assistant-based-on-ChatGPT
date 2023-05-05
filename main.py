import openai
import speech_recognition as sr
import pyttsx3

apiKey = open("API_KEY","r").read()

openai.api_key = apiKey

chat_log = []


def audioRecognizer():
    speech = sr.Recognizer()
    #audio = ''

    with sr.Microphone() as source:
        print("ask your question: ")
        audio = speech.listen(source)#phrase_time_limit=15
        text = ''
        #print("stop.")

        try:
            text = speech.recognize_google(audio,language="en-US")
            print("your question: ",text)
            #return text

        except:
            #assistantVoice("i can't hear your, try again")
            print("i'm waiting for you ...")
    return text


def assistantVoice(text):
    
    voice = pyttsx3.init()
    
    voice.say(text)
    voice.runAndWait()
    
assistantVoice("hi , i am chat gpt from open ai. how can i help you?")

while True:
    message = audioRecognizer().lower()
    
    if "quit" in str(message):
        break
    
    else:
        chat_log.append({"role":"user","content": message})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat_log
        )
        
        assistant_response = response['choices'][0]['message']['content']
        print("chatGPT: ",assistant_response.strip("\n").strip())
        assistantVoice(str(assistant_response))
        chat_log.append({"role":"assistant","content":assistant_response.strip("\n").strip()})
        
                
assistantVoice("ok, i will see you later.")
