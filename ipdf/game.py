import logging

from ipdf.strategies.abstract import AbstractStrategy
from ipdf.strategies.memory_based import MemoryBasedStrategy
from ipdf.payment_matrix import init_default_payment_matrix
from ipdf.logs import init_logger, color_args_str


init_logger()
LOGGER = logging.getLogger(__name__)


class StrategyWrapper:
    def __init__(self, strategy):
        self.strategy = strategy
        self.responses = []
        self.score = 0


class Game():
    """Impements basic interactions between two strategies using given payment matrix"""

    def __init__(self, payment_matrix, strategy1: AbstractStrategy, strategy2: AbstractStrategy):
        self.payment_matrix = payment_matrix
        self.st1 = StrategyWrapper(strategy1)
        self.st2 = StrategyWrapper(strategy2)

    def play(self, n_moves):
        self.st1.responses.append(int(self.st2.strategy.responses[0][0]))
        self.st2.responses.append(int(self.st1.strategy.responses[0][0]))
        for _ in range(0, n_moves):
            strategy1_response = self.st1.strategy.get_move(self.st2.responses)
            strategy2_response = self.st2.strategy.get_move(self.st1.responses)
            self.st1.responses.append(strategy1_response)
            self.st2.responses.append(strategy2_response)

            payments = self.payment_matrix.payments[strategy1_response][strategy2_response]
            self.st1.score += payments[0]
            self.st2.score += payments[1]

    def log_game_info(self):
        args = {
            f'{self.st1.strategy.name()} responses': self.st1.responses,
            f'{self.st2.strategy.name()} responses': self.st2.responses,
            f'{self.st1.strategy.name()} score': self.st1.score,
            f'{self.st2.strategy.name()} score': self.st2.score,
        }
        LOGGER.info(color_args_str(args, 'Game info'))


if __name__ == '__main__':
    matrix = init_default_payment_matrix()

    str1 = MemoryBasedStrategy(sequence_str='101')
    str2 = MemoryBasedStrategy(sequence_str='011')
    game = Game(matrix, str1, str2)
    game.play(7)
    game.log_game_info()

    str1 = MemoryBasedStrategy(sequence_str='1011011')
    str2 = MemoryBasedStrategy(sequence_str='0110011')
    game = Game(matrix, str1, str2)
    game.play(13)
    game.log_game_info()
