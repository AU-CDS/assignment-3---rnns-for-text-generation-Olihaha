# data processing tools
import string, os 
import pandas as pd
import numpy as np
import random
np.random.seed(42)

# keras module for building LSTM 
import tensorflow as tf
tf.random.set_seed(42)
import tensorflow.keras.utils as ku 
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

#import pickle to save tokenizer
import pickle

# surpress warnings
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter(action='ignore', category=FutureWarning)

#helper functions
def clean_text(txt):
    txt = "".join(v for v in txt if v not in string.punctuation).lower()
    txt = txt.encode("utf8").decode("ascii",'ignore')
    return txt 

def get_sequence_of_tokens(tokenizer, corpus):
    ## convert data to sequence of tokens 
    input_sequences = []
    for line in corpus:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)
    total_words = len(tokenizer.word_index) + 1
    return input_sequences, total_words

def generate_padded_sequences(input_sequences):
    # get the length of the longest sequence
    max_sequence_len = max([len(x) for x in input_sequences])
    # make every sequence the length of the longest on
    input_sequences = np.array(pad_sequences(input_sequences, 
                                            maxlen=max_sequence_len, 
                                            padding='pre'))

    predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
    label = ku.to_categorical(label, 
                            num_classes=total_words)
    return predictors, label, max_sequence_len

def create_model(max_sequence_len, total_words):
    input_len = max_sequence_len - 1
    model = Sequential()
    
    # Add Input Embedding Layer
    model.add(Embedding(total_words, 
                        10, 
                        input_length=input_len))
    
    # Add Hidden Layer 1 - LSTM Layer
    model.add(LSTM(100))
    model.add(Dropout(0.1))
    
    # Add Output Layer
    model.add(Dense(total_words, 
                    activation='softmax'))

    model.compile(loss='categorical_crossentropy', 
                    optimizer='nadam')
    
    return model

def generate_text(seed_text, next_words, model, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], 
                                    maxlen=max_sequence_len-1, 
                                    padding='pre')
        predicted = np.argmax(model.predict(token_list),
                                            axis=1)
        
        output_word = ""
        for word,index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " "+output_word
    return seed_text.title()



data_dir = os.path.join("data/")

all_comments = []
for filename in os.listdir(data_dir):
    if 'Comments' in filename:
        article_df = pd.read_csv(data_dir + filename)
        all_comments.extend(list(article_df["commentBody"].values))


all_comments = [h for h in all_comments if h != "Unknown"]
len(all_comments)
print(len(all_comments))

#only 1000 because otherwise the process gets killed, remove the all_comments[:1000] if not desired 
#chose 1000 random comments because it might give more fun spread :)
random.shuffle(all_comments)
all_comments = all_comments[:1000]
print(len(all_comments))

corpus = [clean_text(x) for x in all_comments]
corpus[:10]

## tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
inp_sequences, total_words = get_sequence_of_tokens(tokenizer, corpus)
inp_sequences[:10]
predictors, label, max_sequence_len = generate_padded_sequences(inp_sequences)

#CREATE MODEL
model = create_model(max_sequence_len, total_words)
model.summary()

history = model.fit(predictors, 
                    label, 
                    epochs=100,
                    batch_size=256, 
                    verbose=1)

#save the model
model.save("models/model.h5")

# Save the tokenizer
with open("models/tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

