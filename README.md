# IPDF - Iterated Prisoner's Dilemma Framework

Library for the iterated evolutionary tournaments between memory-based agents.

## Installation

```bash
pip install ipdframework
```

## Usage

### Strategies

#### Memory Based

Create new instance of the memory based strategy (from responses sequence):

```python
from ipdf.strategies.memory_based import MemoryBasedStrategy

strategy = MemoryBasedStrategy(sequence_str='101')
print(strategy.name(), '=>', strategy_1.responses)
```

### Game

Game class allows users to emulate interactions between two strategies

Usage example:

```python
from ipdf.game import Game
from ipdf.strategies.memory_based import MemoryBasedStrategy
from ipdf.payment_matrix import init_default_payment_matrix

matrix = init_default_payment_matrix()
n_moves = 20

str1 = MemoryBasedStrategy(sequence_str='1011011')
str2 = MemoryBasedStrategy(sequence_str='0110011')
game = Game(matrix, str1, str2)
game.play(n_moves)
game.log_game_info()
```

### Memory based strategies storage

```python
from ipdf.memory_strategies_storage import MemoryStrategiesStorage

mem_depth = 1
strategies_st = MemoryStrategiesStorage(mem_depth)
strategies_st.log_storage_info()

for strategy in strategies_st.strategies():
    print(strategy.responses)
```

## Development

Python version: 3.6+

Install w/ dev dependencies:

```bash
pip install -e .[dev]
```

### Author

M.S. CS Dmytro Tkachuk  
[https://dmtk.app](https://dmtk.app)
