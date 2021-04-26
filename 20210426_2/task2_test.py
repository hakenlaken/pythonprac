import tkinter as tk
import unittest
from unittest.mock import MagicMock
from task2 import Model


class TestMo(unittest.TestCase):
    CHKSTR = "QWERT"

    def setUp(self):
        self.view = MagicMock()
        self.view.E.get = MagicMock(return_value=self.CHKSTR)
        self.view.L = {}
        self.model = Model()

    def test_A(self):
        self.model.setup(self.view)
        assert self.model.view is self.view
        # self.assertEqual(self.model.view, self.view)

    def test_B(self):
        self.model.setup(self.view)
        self.model.copy()
        self.view.E.get.assert_called_once()
        self.assertEqual(self.view.L["text"], self.CHKSTR)
        # assert self.model.view is self.view
        # self.assertEqual(self.model.view, self.view)
