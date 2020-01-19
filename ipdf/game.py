import logging

from strategies.memory_based import MemoryBasedStrategy
from helper import init_logger, color_args_str, init_default_payment_matrix


init_logger()
LOGGER = logging.getLogger(__name__)


class Game():
    def __init__(self, payment_matrix, strategy1, strategy2):
        self.payment_matrix = payment_matrix
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.strategy1_responses = []
        self.strategy2_responses = []
        self.strategy1_score = 0
        self.strategy2_score = 0

    def play(self, n_moves):
        self.strategy1_responses.append(int(self.strategy2.responses[0][0]))
        self.strategy2_responses.append(int(self.strategy1.responses[0][0]))
        for _ in range(0, n_moves):
            strategy1_response = self.strategy1.get_move(self.strategy2_responses)
            strategy2_response = self.strategy2.get_move(self.strategy1_responses)
            self.strategy1_responses.append(strategy1_response)
            self.strategy2_responses.append(strategy2_response)

            payments = self.payment_matrix[strategy1_response][strategy2_response]
            self.strategy1_score += payments[0]
            self.strategy2_score += payments[1]

    def log_game_info(self):
        args = {
            f'{self.strategy1.name()} responses': self.strategy1_responses,
            f'{self.strategy2.name()} responses': self.strategy2_responses,
            f'{self.strategy1.name()} score': self.strategy1_score,
            f'{self.strategy2.name()} score': self.strategy2_score,
        }
        LOGGER.info(color_args_str(args, 'Game info'))



if __name__ == '__main__':
    matrix = init_default_payment_matrix()

    str1 = MemoryBasedStrategy(sequence_str='101')
    str2 = MemoryBasedStrategy(sequence_str='011')
    game = Game(matrix, str1, str2)
    game.play(7)
    game.log_game_info()

    str1 = MemoryBasedStrategy(sequence_str='1101011')
    str2 = MemoryBasedStrategy(sequence_str='0101100')
    game = Game(matrix, str1, str2)
    game.play(10)
    game.log_game_info()

    str1 = MemoryBasedStrategy(sequence_str='1011011')
    str2 = MemoryBasedStrategy(sequence_str='0110011')
    game = Game(matrix, str1, str2)
    game.play(13)
    game.log_game_info()
