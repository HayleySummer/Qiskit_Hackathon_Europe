![alt text](https://github.com/HayleySummer/Qiskit_Hackathon_Europe/blob/main/Hackathon.jpeg "Qiskit Hackathon")

# Team Beat the Quantum Machine
*Reinforcement Learning powered by Quantum Mechanics and controlled by Qiskit*



## The Proposal
Games are an interesting test bed for artificial intelligence research, as they provide a self-contained environment with fixed rules. DeepBlue, Watson and AlphaGo are only a few examples of algorithms that were put through their paces in games before applying them to different problems.


Othello is a perfect information, zero-sum, two-player strategy game played on an 8x8 board, and has already been used in classical artificial intelligence research. The board stages are highly volatile, each new move can change a large area of the board. Despite its simple rules, the game of Othello is not trivial, containing of approximately 10^28 legal positions.


We propose the implementation of a Quantum Othello game using quantum computing together with classical machine learning techniques to create a (self-improving) computer opponent players can compete against. Othello is also seen as a Markov Decision Problem in reinforcement learning. In addition, the mixed application of Convolutional Neural Networks result in a better accuracy predicting moves. The Quantum opponent creates winning strategies using a Variational Quantum Circuit for Deep Reinforcement Learning. The implementation utilises PyTorch to train a Deep Q-Learning Neural Network with a Quantum Computing based hidden layer.


## The Approach

Our approach uses Reinforcement learning powered by Quantum Mechanics controlled by Qiskit. We have designed a Hybrid Quantum Neural Network finding the best spot to place tiles in the game of Othello. In this approach, our Quantum Neural Network, or QNN, consists of 5 different Layers.

* The Input Layer (recieves the 8x8 Othello Board in a tensor torch format. It also recieves information about the current state, the action taken, rewards and it evaluates the next state)

* The Convolutional Layer (used to convolute the input and pass it to the next layer)

* The Fully Connected Layer (recieves the batch normalisation of the Convolutional Layer and connects all nodes of the Convolutional Layer with the Quantum Layer)

* The Quantum Layer (maps the segments of the board to 4 Qubits. A classical approach is then used to evaluate the allowed moves in that segment.)

* The Output Layer (performs optimisation routines and returns the values to the board)

We have mainly used Pytorch for machine learning and Qiskit for adding the Quantum layer in our game. 

![alt text](https://github.com/HayleySummer/Qiskit_Hackathon_Europe/blob/main/Project%20Report/Pictures/Nodes.png "QNN Nodes")

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
```

## Folder Structure
In this repository you'll find the following parts: 

| Folder        | Contains      | 
| ------------- |-------------|
| Game       | Othello Game written in Python. Can be used for various Quantum ML approaches |
| QNN     | Quantum Neural Network presented in the Project Report     |
| Proposal | Contains the Proposal for the Hackathon Phase 1      |
| Project Report  |  Contains a Summary of the Project      |
| Notebooks |  Contains a backup of the first Qiskit implementations of the board to image representation     |
| Video |  Video Representation](https://www.powtoon.com/c/fQej7mYq04Z/1/m )     |

Each section has an own README file.
Our approach is designed following modular principles. The individual components can thus be flexibly adapted to the needs of the Qiskit Community. 

