import pyttsx3 

# initialise the pyttsx3 engine 
engine = pyttsx3.init() 

# convert text to speech 
engine.say("I love Python for text to speech, and you?") 
engine.runAndWait() 
