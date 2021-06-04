# Beat the Quantum Machine: 

This repository is part of the Qiskit Hackathon Europe. 

## About the Project
Games are an interesting test bed for artificial intelligence research, as they provide a self-contained environment with fixed rules. DeepBlue, Watson and AlphaGo are only a few examples of algorithms that were put through their paces in games before applying them to different problems.
Othello is a perfect information, zero-sum, two-player strategy game played on an 8x8 board, and has already been used in classical artificial intelligence research. The board stages are highly volatile, each new move can change a large area of the board. Despite its simple rules, the game of Othello is not trivial, containing of approximately  legal positions. The game tree itself has approximately  nodes.
We propose the implementation of a Quantum Othello game using quantum computing together with classical machine learning techniques to create a (self-improving) computer opponent players can compete against.
Othello is also seen as a Markov Decision Problem in reinforcement learning. In addition, the mixed application of Convolutional Neural Networks result in a better accuracy predicting moves. 
The Quantum opponent creates winning strategies using a Variational Quantum Circuit for Deep Reinforcement Learning. The implementation will utilise PyTorch to train a Deep Q-Learning neural network with a Quantum Computing based hidden layer.


## Structure
that implementations 1 and 3 come with python scripts, while implementation 2 consists of Jupyter Notebooks.
You'll find the following parts: 

* Game -> Contains the Othello Game written in Python.
* Notebooks -> Contains the Qiskit implementations of the board to image representation  
* Proposal -> Contains the Proposal for the Hackathon Phase 1 
* Project Report -> Contains a Summary of the Project
* QNN -> Contains the Quantum Hybrid Network 
* Video Representation -> https://www.powtoon.com/c/fQej7mYq04Z/1/m 

Each section has an own README file.

## Dependencies

Run `model-simple-gpu.py` in the QNN Folder (preferebaly on a Linux Machine, the `.c` file causes some issues on Mac).
All the files asociated with it need to be in same directory. 

Dependencies you need to install beforehand (for Linux Machines):

```pip install sklearn
   pip install matplotlib
   pip install torch 
   pip install torchinfo
   pip install torchvision
   pip install qiskit[all]
