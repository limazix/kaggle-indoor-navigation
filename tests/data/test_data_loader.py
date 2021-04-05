# -*- utf-8 -*-

import os

from unittest import TestCase
from unittest.mock import patch

from tools.data import DataLoader


class TestDataLoader(TestCase):
    def setUp(self):
        self.data_dir = "./data/train"
        self.tool = DataLoader(data_dir=self.data_dir)

    def test_data_path(self):
        """
        it should have a property with the local path directory
        """
        self.assertIsNotNone(self.tool.data_dir)
        self.assertEqual(self.tool.data_dir, self.data_dir)

    def test_data(self):
        """
        it should have a property to store the data in memory
        """
        self.assertIsNotNone(self.tool.data)
        self.assertIsInstance(self.tool.data, list)

    def test_normalize_path(self):
        """
        it should have a method to normalize a list of strings to a directory path
        """
        parts = ["data", "train", "1234"]
        expected = os.path.normpath("./data/train/1234")

        result = self.tool.normalize_path(parts)
        self.assertEqual(result, expected)

    def test_normalize_path_empty(self):
        """
        it should return the project root folder if no path part is provided
        """
        parts = []
        expected = os.path.normpath(".")

        result = self.tool.normalize_path(parts)
        self.assertEqual(result, expected)

    @patch.object(DataLoader, "normalize_path")
    def test_load_data(self, mock_normalize_path):
        """
        it should run over the given path folder and print each subdir name
        """
        self.tool.load_data()
        mock_normalize_path.assert_called()

    @patch.object(os, "listdir")
    def test_load_data_base_dir(self, mock_listdir):
        """
        it should run over the given base dir instead of the class data dir
        """
        base_dir = "./data/test"
        self.tool.load_data(base_dir=base_dir)
        mock_listdir.assert_called_with(base_dir)
