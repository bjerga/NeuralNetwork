# NeuralNetwork
Simple neural network for MNIST-recognition.
Created for Machine Leaning-course at Seoul National University.


### Requirements
The code is written in Python 3.4.3. 
To run the code, libraries numpy and matplotlib are needed. These can be easily installed using "pip install numpy" and "pip install matplotlib" in command window.


### How the code works
neural_network.py can either load old networks or train a new one. This choice can be performed by choosing value of network_number in main-function (how is specified in code). To train a new network, parameter values must be chosen. These are amount of hidden units and amount of training epochs. Hidden unit amount can be specified in the second argument in neural network initialization and epochs are given in a seperate variable. Runtime for 100 hidden units with 50 epochs is ~600 seconds.

The code is meant to firstly train for the given number of epochs, and then classify the images in both the training set and a given test set. It will finally output a percentage of correct classification for both sets, as well as a specific number of correctly classified images.


### Useful links
Theory and concept: 

http://cs231n.github.io/

Other repositories:

https://github.com/jorgenkg/python-neural-network

https://github.com/FlorianMuellerklein/Machine-Learning
