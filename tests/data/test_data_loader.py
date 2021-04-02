# -*- utf-8 -*-

from unittest import TestCase

from tools.data import DataLoader


class TestDataLoader(TestCase):
    def setUp(self):
        self.data_dir = "./data"
        self.tool = DataLoader(data_dir=self.data_dir)

    def test_data_path(self):
        """
        it should have a property with the local path directory
        """
        self.assertIsNotNone(self.tool.data_dir)
        self.assertEqual(self.tool.data_dir, self.data_dir)
