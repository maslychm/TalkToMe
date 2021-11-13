# TalkToMe
Talk to a person based on a Transformer model of them

## Running backend
First developed on windows, but will be adapted to run in WSL within a few hours
### Installation
1. `cd backend`
2. `python -m venv venv`
3. `venv\Scripts\activate`
4. `pip install -r requirements.txt`

### Running
1. `venv\Scripts\activate`
2. `set FLASK_APP=app.py`
3. `flask run`