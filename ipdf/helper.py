import json


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
