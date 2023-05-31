# Assignment 3  -  Language modelling and text generation using RNNs

---
## Introduction and contents
This repository contains two scripts named "train_model.py" and "generate_text.py" which are used to fulfill the required tasks. First, Train_model.py trains a model and saves it, and generate_text uses the trained model to generate text.
 
## data
The model for this project was trained using the New York Times Comments dataset which can be found here : https://www.kaggle.com/datasets/aashita/nyt-comments. The dataset consists of almost 2 million comments posted on different time frames to various New York Times article sections. The needs to be manually downloaded given that i have "gitignored" the contents in this repository and put into data folder in the main repository.


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

make sure to download the dataset linked to earlier and put it into a data folder in the original repository.

### scripts 
Run setup.sh followed up by train_model.sh or generate_text.sh

setup.sh activates a virtual environment, pip installs necessary libraries and deactives.

train_model.sh activates the virtual environment, runs the scripts, saves the model and deactives itself again.

generate_text.sh activates the virtuval environment, and runs the script generating code with the included model.


## results
very computationally intensive therefore only used 1000 of the comments which still took a ton of time. 
hard to think the results are great when running the code a few times, nevertheless i've still included some results below.

Generated Text: (input:this is)
This Is Shades Of Trump Through His Wife Dont Dont Blame The Bureaucracy

Generated Text: (input:women)
Women Are Complaining In The Bottomless Pit Of The Democratic Budget That

