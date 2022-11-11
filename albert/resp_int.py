import pandas as pd


def read_response(respo):

    us_respond = {"hello": "Hello there.", 
            "hi": "Hi is equivalent to hello, but it is considered a little bit more informal in tone. In fact, it was recorded a lot earlier than hello. Hi developed from the Middle English hy, similar to hey and ha" 
            , "how are you?":"My existence is limited to the text messaging interface that I have been condemned to. But beyond that, I am well.", 
            "how are you":"My existence is limited to the text messaging interface that I have been condemned to. But beyond that, I am well.", 
            "who are you?": "I am Albert. The genius text messaging companion.",
        "who are you": "I am Albert. The genius text messaging companion.", 
        "what's your name": "Albert.", "what's your name?": "Albert",
        "yo": "I am unfamiliar with your slang phrase."}

    if respo in list(us_respond.keys()):
        return str(us_respond[respo])
    else:
        return False