import numpy as np


class PaymentMatrix:
    def __init__(self, dd: list, dc: list, cd: list, cc: list):
        self.__payments = np.zeros((2, 2, 2))
        self.set_payments(dd, dc, cd, cc)

    @property
    def payments(self) -> np.ndarray:
        return self.__payments

    def set_payments(self, dd: list, dc: list, cd: list, cc: list) -> None:
        self.__payments[0][0] = dd
        self.__payments[0][1] = dc
        self.__payments[1][0] = cd
        self.__payments[1][1] = cc


def init_default_payment_matrix():
    return PaymentMatrix([1, 1], [5, 0], [0, 5], [3, 3])
