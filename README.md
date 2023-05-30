# Assignement 3  -  Language modelling and text generation using RNNs

---
## Introduction and contents
This repository contains two scripts named "train_model.py" and "generate_text.py" which are used to fulfill the required tasks. First, Train_model.py trains a model and saves it and generate_text uses the trained model to generate text.
 

## data
The model for this project was trained using the New York Times Comments dataset which can be found here : https://www.kaggle.com/datasets/aashita/nyt-comments. The dataset consists of almost 2 million comments posted on different time frames to various New York Times article sections. The data can be found in the data folder, but must be manually downloaded given that i have "gitignored" the contents in this repository.

## models 
A recurrent neural network model that has been trained brings the text generator to life. The TensorFlow framework, which offers a setting for deep learning problems, is used to develop and construct this model. The architecture of the text generator is designed as a sequential paradigm, with multiple levels producing text that is cohesive and appropriate for the given context. The model makes use of an output layer and a hidden layer called LSTM (long short term memory). A recurrent neural network (RNN) architecture called a Long Short-Term Memory (LSTM) model is made particularly to handle sequence data and identify long-term relationships in the data. LSTM models contain an internal memory state that enables them to retain information across lengthy periods, in contrast to standard feedforward neural networks that analyze individual inputs individually.
 
this model works with three layers that can be explained in a very simple way which makes it differnet to normal RNN's.

1. the input layer decides what information is important and should be stored in memory.
2. the "forget" layer for a lack of a better term decides what information should be ignored, simply forgotten or just ends up being decided as irrelevant.
3. the output gate decides what information should be passed on to the next step in the sequencing.

LSTMs are superior to other models particularly in speech because it can selectively remember or forget information, allowing it to understand and process complex patterns in sequences better than other models. 

## script functions
The train_model.py function does the following
1. imports dependencies and loads the data.
2. preprocesses and tokenizes the data
3. Trains an RNN LSTM model and saves it to the model folder

the generate_text.py function does the following
1. loads the model and the tokenizer
2. asks the user for an input and length of the response
3. generates text based on inputs recieved


## how to replicate
### copy the repository 
git clone https://github.com/AU-CDS/assignment3-pretrained-cnns-Olihaha

make sure to be in correct directory

(cd assignment-3)

### scripts 
Run setup.sh followed up by train_model.sh or generate_text.sh

setup.sh activates a virtual environment, pip installs necessary libraries and deactives.

train_model.sh activates the virtual environment, runs the scripts, saves the model and deactives itself again.

generate_text.sh activates the virtuval environment, and runs the script generating code with the included model.


## results
very computationally intensive therefore only used 1000 of the comments which still took a ton of time. 
har to think the results are great when running the code a few times, but below i've input some reulsts.

Generated Text: (input:this is)
This Is Shades Of Trump Through His Wife Dont Dont Blame The

Generated Text: (input:this is)
Women Are Complaining In The Bottomless Pit Of The Democratic Budget That

