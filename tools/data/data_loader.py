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

        :return: str -- Nomalized Path

        .. obs: It does not order the given list.
        """
        return os.path.normpath(os.path.join(*parts))
