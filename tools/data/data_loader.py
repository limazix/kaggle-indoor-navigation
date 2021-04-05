# -*- utf-8 -*-

import os


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

    def normalize_path(self, parts: list):
        """
        Method used to join and normalize a list of paths parts to a single one

        :param parts:
        :type parts: list

        :return: str -- Normalized Path

        .. obs: It does not order the given list.
        """
        if len(parts) == 0:
            parts.append(".")
        return os.path.normpath(os.path.join(*parts))

    def load_data(self, base_dir: str = None):
        """
        Method used to load the data based on the given path

        :param base_dir: Directory path to run over
        :type base_dir: str

        """
        base_dir = base_dir if base_dir is not None else self.data_dir

        for subdir in os.listdir(base_dir):
            print(self.normalize_path([base_dir, subdir]))
