import sys
import json
import logging
import colorful as cf
import numpy as np
from logging import Formatter, StreamHandler

cf.use_style('solarized')

PALETTE = {
    'success': '#00c841',
    'info': '#1976a3',
    'error': '#d40000'
}

LINE = '-' * 100


def color_args_str(args, title=None, type='info'):
    s = cf.blue(f'\n{LINE}\n')
    if title:
        with cf.with_palette(PALETTE) as c:
            if type == 'error':
                s += f'{c.bold_error(title)}\n'
            elif type == 'success':
                s += f'{c.bold_success(title)}\n'
            else:
                s += f'{c.bold_info(title)}\n'
    for k in args:
        s += f'{cf.bold_violet(k)}: '
        s += f'{args[k]}\n'
    s += cf.blue(f'{LINE}\n')
    return s


def init_logger():
    handlers = []
    formatter = Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_handler = StreamHandler(sys.stderr)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    handlers.append(stream_handler)

    logging.basicConfig(level=logging.DEBUG, handlers=handlers)


def binary_arr_to_decimal(bit_list):
    output = 0
    for bit in bit_list:
        output = output * 2 + bit
    return output


def two_powers(num):
    return [ 1 << idx for idx, bit in enumerate(bin(num)[:1:-1]) if bit == "1" ]


def init_default_payment_matrix():
    return init_payment_matrix([1, 1], [5, 0], [0, 5], [3, 3])


def init_payment_matrix(dd, dc, cd, cc):
    payments = np.zeros((2, 2, 2))
    payments[0][0] = dd
    payments[0][1] = dc
    payments[1][0] = cd
    payments[1][1] = cc
    return payments


def load_clusters(path):
    with open(path) as json_file:
        clusters = json.load(json_file)
    return clusters['clusters']
