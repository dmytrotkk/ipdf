# IPDF - Iterated Prisoner's Dilemma Framework

Library for the iterated evolutionary tournaments between memory-based agents.

## Usage

### Strategies

#### Memory Based

Create new instance of the memory based strategy (from responses sequence):

```python
from strategies.memory_based import MemoryBasedStrategy

strategy = MemoryBasedStrategy(sequence_str='101')
print(strategy.name(), '=>', strategy_1.responses)
```

### Game

Game class allows users to emulate interactions between two strategies

Usage example:

```python
from game import Game
from strategies.memory_based import MemoryBasedStrategy
from helper import init_default_payment_matrix

matrix = init_default_payment_matrix()
n_moves = 20

str1 = MemoryBasedStrategy(sequence_str='1011011')
str2 = MemoryBasedStrategy(sequence_str='0110011')
game = Game(matrix, str1, str2)
game.play(n_moves)
game.log_game_info()
```

## Development

Python version: 3.6+

Install dependencies:
```bash
pip install -r requirements.txt
```

### Author

M.S. CS Dmytro Tkachuk  
[https://dmtk.app](https://dmtk.app)
