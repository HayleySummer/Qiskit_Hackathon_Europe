Welcome to Beat the Quantum Machine in the IBM Qiskit Hackathon Europe

### Games in AI

Games have always played an important role in AI research. When we think of AI in video games, we think of non-player characters, which are characters with intelligence that evolve with or against the player during the game. These programs are driven by specific statistical algorithms: we can mention the Finite State Machine and Monte Carlo Search Tree models for example, which give the illusion of a reactive and adaptive intelligence. These algorithms, however sophisticated, do not use the most advanced AI technologies.


### DeepBlue/Watson/AlphaGo

The capabilities of artificial intelligence in games have been shown before. DeepBlue, a chess supercomputer developed by IBM in the 1990s is one of them. It was designed to master the game of chess, beating Grandmaster Garri Kasparow in an impressive match in 1997. Other examples are  AlphaGo or Watson. These machines combine great computing power and machine learning techniques to learn from humans in specialised fields. In the field of games, they beat professionals in Jeopardy, Go and chess. Today algorithms and machine learning techniques derived from machines like Watson are reused for other tasks, for example in medical research.


### Quantum Computing

Besides the continuous development of video games, in recent years, an increasing number of works have been published with the aim of combining the disciplines of quantum information processing and Machine Learning. The question that can be asked is how can we use the power of quantum computing together with machine learning in order to play the game Othello. 


### Our Approach

Our Approach uses the best of both Worlds: Reinforcement learning powered by Quantum Mechanics. We have  designed a Hybrid Quantum Neural Network finding the best spot to place tiles in the game of Othello.
In this approach, our Quantum Neural Network, or QNN, consists of 5 different Layers. 

The Input Layer recieves the 8x8 Othello Board in a tensor torch format. It also recieves information about the current state, the action taken, rewards and it evaluates the next state. 

The Convolutional Layer 

Fully Connected Layer

The Quantum Layer
which maps the segments of the board to 4 Qubits. A classical approach is then used to evaluate the allowed moves in that segment. 

The Output Layer

We have mainly used Pytorch for machine learning and Qiskit for adding the Quantum layer in our game.  

##
Thanks for listening. If you want to join this exciting field of AI powered by quantum mechanics and controlled by Qiskit, feel free to get in touch with us or join us on GitHub. 


