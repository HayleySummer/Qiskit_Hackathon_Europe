# Proposal


## Judging Criterion 1 - Excellence
Weight: 40.00%
Compared to what you’ve seen before, how original/unique is this proposal? 
How relevant is the research question and project?

Slide 1 - Project Idea
- Which field of quantum computing is your proposal about? 
- Which is the topic of your proposal? 
- Which question/s do you want to address? 
- Provide a technical description of the proposal. 

## Project idea:
Games provide an interesting test bed for artificial intelligence research, as they provide a self-contained environment with fixed rules. DeepBlue, Watson and AlphaGo are only a few examples of algorithms that were put through their paces in games before applying them to different problems.

Othello (also called Reversi) is a perfect information, zero-sum, two-player strategy game played on an 8x8 board, and has already been used in classical artificial intelligence research. The board stages are highly volatile, because each new move can change a large area of the board. Despite its simple rules, the game of Othello is not trivial, containing a number of legal positions of approximately 10<sup>28</sup>. The game tree itself has approximately 10<sup>58</sup> nodes.[1]

Othello is seen as a Markov Decision Problem in literature, marking an important section of reinforcement learning [2]. In addition, the mixed aplication of Convolutional Neural Nets result in a better accuracy predicting moves [3].

We propose the implementation of a Quantum Othello game using quantum computing together with classical machine learning techniques to create a (self-improving) computer opponent players can compete against.

The Quantum opponent creates winning strategies using a Variational Quantum Circuit for Deep Reinforcement Learning.  The implementation will utilise PyTorch to train a Deep Q-Learning neural network with a Quantum Computing based hidden layer.  


## Peculiarity of the project:
- combining classical ML approaches with quantum advantages in a classical problem -> towards an application of hybrid solutions
- showing problem solving on 8x8 board, rather than a 4x4 board



## Judging Criterion 2 - Impact
Weight: 30.00%
How well does the proposal advance research and open source science in the field of quantum computing? 
How useful is this idea? Does it have prospects for future development? 
Will this project help the community at large? Will this project spark interest in the quantum computing community?


Slide 2 - Impact and Goals
- What would you like to achieve with this proposal? 
- Which value does this proposal bring to the specific field of interest (QML/ quantum games...) and to the wider quantum computing field? 
- How novel is your proposal? 
- Which are the near-term and long-term goals for this proposal?   

## Impact and goals:

- Demonstration of a quantum machine learning technique for reinforcement learning implemented in an accessible format within a game

- Provide an analysis of encoding the state of a complex game in a format suitable for use in current Quantum ML environments. 

- Convolutional Neural Networks in combination with quantum mechanics are novel to this approach where the game state and action space is large.

- The proposal brings interest in the fields of quantum machine learning and in quantum games since we are making an AI to play against the user.  

- In the near-term we will create a playable game and associated Quantum ML Agent. 

- In the long-term the Quantum ML agent can be improved for better performance and efficiency.  This work will also provide a starting point for others to advance the implemention of Quantum Machine Learning Agents using Reinforcement Learning. 

- Also the proposal shows an approach that can realistically implement a working prototype within the given time frame of 4 weeks. 
- (optional?) comparison of error rates, noise mitigation (in gates and measurement?)?

- (optional?) Execution speed of a quantum simulator running on a classical computer compared to a quantum computer running at IBM Q Experience (using the Big-O Notation or with pure computation time?)?

## Criterion 3 - Implementation
Weight: 30.00%
How feasible and effective is the work plan within the timeframe considering the allocation of tasks and resources?
How coherent and structured is the proposal? 

Slide 3 - Implementation Plan: Timeline, Tasks, & Resources
- What are the phases/steps of your project? Build the timeline of your project based on the deadline for each phase.
- Which skills are required for each phase? Who in your team has these skills? How do you plan to divide the tasks within your team? 
- Which resources do you plan to use for developing your project? (Qiskit libraries/modules, game engines, research papers references, etc) 

## Implementation plan: Timeline, tasks & resources (research papers, Qiskit libraries/modules...)

### Timeline:
(It´s only a possible timeline)
- *7  May - 14 May:* Basic Othello playable game & UI 
- *14 May - 28 May:* Implementation of the classical (AND/OR)? quantum algorithm. -> Start this simultaneuosly with the Othello implementation?
- *28 May - 4 June:* Testing and adjustments & finalizing project report

Skills: 
- (Q)ML -> David, Enda, Nouhaila
- Qiskit -> Divyanshu, Barbora, ... ?
- Python Games -> Barbora, ?
- UI -> Team
- Testing / Adjustments -> Team 
- Project Report -> Team 

### Tasks:
- Creation and implementation of the Othello mechanics and the rules.
- Implementation of the classical algorithm.
- Implementation of the quantum algorithm.
- Desing the user interface.
- Implementation of the user interface.
- Iterative testing and adjustments
- Documentation and Presentation
- Video? 

### Qiskit libraries/modules: 
- [Qiskit-Aer](https://qiskit.org/documentation/apidoc/aer.html) for getting the backend 
- [Qiskit-Ignis](https://qiskit.org/documentation/apidoc/ignis.html?highlight=ignis#module-qiskit.ignis) for noise mitigation
- [Qiskit-Aqua](https://qiskit.org/documentation/apidoc/qiskit_aqua.html) or [Qiskit-machine-learning](https://qiskit.org/documentation/machine-learning/apidocs/qiskit_machine_learning.html#qiskit-s-machine-learning-module-qiskit-machine-learning) for the implementation of Machine Learning algorithm
- [Qisikit-algorithm-Grover](https://qiskit.org/documentation/stubs/qiskit.algorithms.Grover.html?highlight=grover#qiskit.algorithms.Grover) (If we use Grover's approach )



### Bibliography:
- [1] Paweł Liskowski, Wojciech Ja´skowski, Krzysztof Krawiec (2017) "Learning to Play Othello with Deep Neural
Networks." In: IEEE TRANSACTIONS ON COMPUTATIONAL INTELLIGENCE AND AI IN GAMES
- [2] Nees Jan van Eck, Michiel van Wezel (2005): Reinforcement Learning and its Application to Othello. In: Econometric Institute Report EI 2005-47
- [3] Hlynur Davíð, H. (2017). Predicting expert moves in the game of Othello using fully convolutional neural networks (Dissertation). Retrieved from http://urn.kb.se/resolve?urn=urn:nbn:se:kth:diva-210914

