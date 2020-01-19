import logging
import itertools

from ipdf.strategies.memory_based import MemoryBasedStrategy
from ipdf.logs import init_logger, color_args_str
from ipdf.constants import ELEMENTS

init_logger()
LOGGER = logging.getLogger(__name__)


class MemoryStrategiesStorage():
    def __init__(self, mem_depth):
        self.mem_depth = mem_depth - 1
        self.calc_strategy_len()
        self.generate_strategies()

    def calc_strategy_len(self):
        md = self.mem_depth + 2
        strategy_length = 1
        for x in range(1, md):
            strategy_length += 2 ** x
        self.strategy_len = strategy_length

    def generate_strategies_names(self):
        return [subset for subset in itertools.product(ELEMENTS, repeat=self.strategy_len)]

    def generate_strategies(self):
        self.__strategies = []
        sequences = self.generate_strategies_names()
        for sequence in sequences:
            self.__strategies.append(MemoryBasedStrategy(sequence_str=''.join(map(str, sequence))))

    def log_storage_info(self):
        args = {
            'Memory depth': self.mem_depth, 
            'Strategy length': self.strategy_len, 
            'Number of strategies': len(self.__strategies)
        }
        LOGGER.info(color_args_str(args, 'Strategies storage info'))

    def strategies(self):
        return self.__strategies


if __name__ == '__main__':
    strategies_st = MemoryStrategiesStorage(1)
    strategies_st.log_storage_info()

    for strategy in strategies_st.strategies():
        print(strategy.responses)
