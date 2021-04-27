# Proposal

## Project idea:
Games provide an interesting test bed for artificial intelligence research, as they provide a self-contained environment with fixed rules. DeepBlue, Watson and AlphaGo are only a few examples of algorithms that were put through their paces in games before applying them to different problems.

Othello (also called Reversi) is a perfect information, zero-sum, two-player strategy game played on an 8x8 board, and has already been used in classical artificial intelligence research. The board stages are highly volatile, because each new move can change a large area of the board. Despite its simple rules, the game of Othello is not trivial, containing a number of legal positions of approximately $10^28$. The game tree itself has approximately $10^58$ nodes.[1]

Othello is seen as a Markov Decision Problem in literature, marking an important section of reinforcement learning [2]. In addition, the mixed aplication of Convolutional Neural Nets result in a better accuracy predicting moves [3].

We propose the implementation of a Quantum Othello game using quantum states together with classical machine learning techniques to create a (self-improving) computer opponent players can compete against.

Quantum opponent creates winning strategies using (one of these?/all of them?):
- QCNNs, mapping each spot on the board as it were pixels in the image recognition, assigning a weight to them depending on different dynamic or static rules (dynamic, static or limited depends on the approach). [1]
- combining CNN with Monte Carlo Tree Search? (approach taken by Alpha Go)
- Grover / Monte Carlo


## Peculiarity of the project:
- combining classical ML approaches with quantum advantages in a classical problem -> towards an application of hybrid solutions
- showing problem solving on 8x8 board, rather than a 4x4 board


## Impact and goals:

- Demonstration of a quantum technique for (reinforcement learning?) implemented in an accessible format within a game

- Convolutional Neuronal Networks in combination with quantum mechanics are novel to this approach, as they were only applied to image recognition.

- comparison of error rates, noise mitigation (in gates and measurement?)?

- execution speed of a quantum simulator running on a classical computer compared to a quantum computer running at IBM Q Experience (using the Big-O Notation or with pure computation time?)?

- Explore the opportunities for mapping a the state of a complex game into the current Qiskit environment.

- The proposal bring interest in the fields of quantum machine learning as we applied QCNNs, quantum algorithms because we used the Grover´s algorithm and in quantum games since we are making an IA to play against the user.

- In the near-term we are trying to create a playable game with limited and reduced rules. This rules could be based on quantum or hybrid algorithms.

- In the long-term we will be able to finish a complete game with at least the same amount of rules we have in the classical algorithm and with better performance and efficiency.


## Implementation plan: Timeline, tasks & resources (research papers, Qiskit libraries/modules...)

### Timeline:
(It´s only a possible timeline)
- *7  May - 14 May:* Basic Othello playable game. 
- *14 May - 28 May:* Implementation of the classical (AND/OR)? quantum algortihm. 
- *28 May - 4 June:* UI.

### Tasks:
- Creation and implementation of the Othello mechanics and the rules.
- Implementation of the classical algorithm.
- Implementation of the quantum algorithm.
- Desing the user interface.
- Implementation of the user interface.

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

