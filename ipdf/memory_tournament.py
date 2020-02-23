import os
import datetime
import json
import logging
import time

from ipdf.game import Game
from ipdf.memory_strategies_storage import MemoryStrategiesStorage
from ipdf.payment_matrix import init_default_payment_matrix
from ipdf.logs import init_logger, color_args_str


init_logger()
LOGGER = logging.getLogger(__name__)

DATA_DIR = 'tournament_results'


class MemoryStrategiesTournament():
    """Encapsulates evolutionary tournament logic"""

    def __init__(self, mem_depth, payment_matrix):
        self.mem_depth = mem_depth
        self.memory_strategies_storage = MemoryStrategiesStorage(mem_depth)
        self.payment_matrix = payment_matrix
        self.scores = []

    def play(self, n_moves):
        self.iterations = n_moves
        for strategy1 in self.memory_strategies_storage.strategies():
            args = {
                'Strategy name': strategy1.name(),
                'Number of competitors': len(self.memory_strategies_storage.strategies()) - 1
            }
            LOGGER.info(color_args_str(args, 'Running tournament set'))
            strategy_score = 0
            for strategy2 in self.memory_strategies_storage.strategies():
                if strategy1.responses == strategy2.responses:
                    LOGGER.info(f'Skipping {strategy1.name()}...')
                    continue
                game = Game(self.payment_matrix, strategy1, strategy2)
                game.play(n_moves)
                strategy_score += game.st1.score
            self.scores.append({'name': strategy1.name(), 'score': strategy_score})
            LOGGER.info(f'{strategy1.name()} total: {strategy_score}')

    def save(self):
        info = {
            'memory_depth': self.mem_depth,
            'iterations': self.iterations,
            'results': self.scores
        }
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        filename = f'evolution_tournament_{time}.json'

        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, 'w') as outfile:
            LOGGER.info(f'Saving info to {filename}')
            json.dump(info, outfile, indent=4)


if __name__ == '__main__':
    payment_matrix = init_default_payment_matrix()
    memory_strategies_tournament = MemoryStrategiesTournament(2, payment_matrix)
    time1 = time.time()
    memory_strategies_tournament.play(50)
    time2 = time.time()
    memory_strategies_tournament.save()

    print('timediff:', time2 - time1)
