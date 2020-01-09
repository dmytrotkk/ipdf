from strategies.abstract import AbstractStrategy
from helper import two_powers, binary_arr_to_decimal

class MemoryBasedStrategy(AbstractStrategy):
    def __init__(self, sequence_str):
        super().__init__(sequence_str)
        self.__sequence_str = sequence_str
        self.generate_responces()
        self.responses_len = len(self.responses)

    def generate_responces(self):
        self.responses = []
        strategy_list = list(self.__sequence_str)
        parts_len = self.calc_parts_len()
        for part in parts_len:
            resp = [strategy_list.pop(0) for _ in range(part)]
            strategy_list[:part]
            self.responses.append(resp)

    def calc_parts_len(self):
        mem_depth = self.sequence_len_to_md(len(self.__sequence_str))
        md = mem_depth + 2
        return [2 ** x for x in range(0, md)]

    def sequence_len_to_md(self, sequence_len):
        return len(two_powers(sequence_len)) - 2

    def get_move(self, opponent_responses):
        opponent_responses_len = len(opponent_responses)    
        strategy_responses_len = self.responses_len - 1

        s_part_ind = strategy_responses_len if opponent_responses_len >= strategy_responses_len else opponent_responses_len
        s_part = self.responses[s_part_ind]

        offset = opponent_responses_len - strategy_responses_len
        s_slice = opponent_responses[offset:]
        response_index = binary_arr_to_decimal(s_slice)

        return int(s_part[response_index])


if __name__ == '__main__':
    strategy_1 = MemoryBasedStrategy(sequence_str='101')
    print(strategy_1.name(), '=>', strategy_1.responses)
    strategy_2 = MemoryBasedStrategy(sequence_str='1011011011011011011011011011011')
    print(strategy_2.name(), '=>', strategy_2.responses)
