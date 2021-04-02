# -*- utf-8 -*-


class DataLoader:
    """
    Class designed to load and format the challenge data

    :param data_dir: Data local directory path
    :type data_dir: str
    :param data: Data store reference
    :type data: list

    """

    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.data = list()
