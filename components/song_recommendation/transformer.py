import os
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_KEY'] = apikey

template = PromptTemplate(
    input_variables = ['emotions'],
    template = 
    """
    Here is a list of music genres that you may use, but are not limited to: 
    Rock, Pop music, Hip hop music, Jazz, Electronic music, 
    Country music, Classical music, Rhythm and blues,
    Heavy metal, Blues, Soul music, Electronic dance music, 
    Alternative rock, Reggae, Funk, Musical theatre, Punk rock, 
    Folk music, New-age music, Easy listening, Latin music, Techno, 
    Indie rock, Disco, Contemporary R&B, Electronica, Dance music, 
    Ska, Hip hop, Progressive rock, Dubstep, Experimental music, 
    Industrial music, House music, Opera, Swing music, Rock and roll, 
    Trance music, Ambient music, New wave, Grunge, Gospel music, Instrumental, 
    Rapping, Folk music, Flamenco, Bluegrass, Dream pop, Lament, 
    Romantic, Chill-out, Electric, and Breakbeat.
    
    Pick one genres that most encapsulates a person whose facial expressions can 
    be described as {emotions}.
    """
)

llm = OpenAI(temperature=0.9)

chain = LLMChain(llm=llm, prompt=template)

def transform(emotions):
    yield chain.run(emotions)
