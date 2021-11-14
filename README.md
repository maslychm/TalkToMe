# TalkToMe
__Talk to a person based on a Transformer model of them.__

This application scrapes chat logs between two users from Discord and inputs one of the user's data through a GPT-2-medium model to generate a relatively complex language model. The dataset, found under ```training_2_.txt```, contains 300 lines of conversation between Mykola and Steven, two friends from UCF. Because the training data is multilingual, GPT-2 can still adapt to these changes and generate fairly reasonable text. 

## Web Application Used
We utilize Python's Flask as our backend to receive user's input text. It passes it through the GPT-2 model to retrieve the output and forwards to the front-end UI. The front-end was inspired by this [project](https://github.com/huzaifsayed/coronabot-chatterbot) and we use his front-end, developed with HTML, CSS and JavaScript as our template. 

### Running Web Application
1. `cd web_app`
2. `pip install -r requirements.txt`
3. `python app.py`
