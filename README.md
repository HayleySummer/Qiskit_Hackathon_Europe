# Beat the Quantum Machine: 

This repository is part of the Qiskit Hackathon Europe. 

##About the Project

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
