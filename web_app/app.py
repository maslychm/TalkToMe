from flask import Flask, render_template, request
from tensorflow.keras.models import Sequential
from keras.layers.normalization import layer_normalization
import tensorflow as tf
# import tensorflow_hub as hub
# import tensorflow_text as text

import numpy as np
import gpt_2_simple as gpt2

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():

    userText = request.args.get('msg')
    userText = str(userText)
    print(userText)

    print(">>>>>>>Loading...")
    GPT2_SESSION = gpt2.start_tf_sess()
    gpt2.load_gpt2(GPT2_SESSION, run_name='things2\\run1')

    print(">>>>>>>Model was loaded")

    results = gpt2.generate(GPT2_SESSION, length=75, temperature=1.0, prefix=f'Mykola: {userText} <|endoftext|> Steven: ',
                            nsamples=10, batch_size=5, return_as_list=True)

    results = [res.split('<|endoftext|>')[1] for res in results]
    print("All", results)
    result = max(results, key=len)
    
    # bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
    # bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")
    
    # fpath = 'C:/Users/masly/projects/TalkToMe/web_app/checkpoint/cp.ckpt/'
    # print(fpath)
    # model = tf.keras.models.load_model(fpath)
    # response = results[np.argmax(model.predict(results))]
    # print("Chosen: ", response)
    # ret = response.replace("Steven:", '')
    
    result = result.replace("Steven:", '')
    return result


if __name__ == "__main__":
    app.run()
