from flask import Flask, render_template, request

import gpt_2_simple as gpt2
# GPT2_SESSION = None

app = Flask(__name__)
app.static_folder = 'static'


# def load_model():
#     print(">>>>>>>Loading...")
#     global GPT2_SESSION
#     GPT2_SESSION = gpt2.start_tf_sess()
#     gpt2.load_gpt2(GPT2_SESSION, run_name='things2\\run1')
    
#     print(">>>>>>>Modal was loaded")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    # global GPT2_SESSION
    userText = request.args.get('msg')
    userText = str(userText)
    print(userText)

    print(">>>>>>>Loading...")
    GPT2_SESSION = gpt2.start_tf_sess()
    gpt2.load_gpt2(GPT2_SESSION, run_name='things2\\run1')
    
    print(">>>>>>>Modal was loaded")
    
    results = gpt2.generate(GPT2_SESSION, length=75, temperature=1.0, prefix=f'Mykola: {userText} <|endoftext|> Steven: ',
                            nsamples=10, batch_size=5, return_as_list=True)
    
    ret = max(results, key=len)
    print(ret, results)
    
    ret = results[2].split('<|endoftext|>')[1]
    ret = ret.replace("Steven:", '')
    return ret


if __name__ == "__main__":
    # load_model()
    app.run()

