import os
import json
import logging

from ipdf.constants import IPDF_DATADIR


LOGGER = logging.getLogger(__name__)


def binary_arr_to_decimal(bit_list):
    output = 0
    for bit in bit_list:
        output = output * 2 + bit
    return output


def two_powers(num):
    return [1 << idx for idx, bit in enumerate(bin(num)[:1:-1]) if bit == "1"]


def load_clusters(path):
    with open(path) as json_file:
        clusters = json.load(json_file)
    return clusters['clusters']


def save_to_datadir(data, filepath):
    if not os.path.exists(IPDF_DATADIR):
        os.makedirs(IPDF_DATADIR)
    with open(filepath, 'w') as outfile:
        LOGGER.info(f'Saving info to {filepath}')
        json.dump(data, outfile, indent=4)
