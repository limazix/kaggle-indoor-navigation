# -*- utf-8 -*-

import os

from unittest import TestCase

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
