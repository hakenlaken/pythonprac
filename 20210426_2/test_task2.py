# -*- coding: utf-8 -*-

import unittest
from unittest.mock import MagicMock
from task2 import AppModel, AppControl


class TestMo(unittest.TestCase):

    def setUp(self):
        self.view = MagicMock()
        self.view.Sresult = {}
        self.model = AppModel(self.view)
        self.control = AppControl(self.model)

    def set_coefficients(self, a, b, c):
        self.view.Sa.get = MagicMock(return_value=a)
        self.view.Sb.get = MagicMock(return_value=b)
        self.view.Sc.get = MagicMock(return_value=c)

    def test_0_init(self):
        """проверка на инициализацию"""
        assert self.model.view is self.view
        assert self.control.model is self.model

    def test_1_call(self):
        """проверка на вызов основной функции"""
        self.model(self.control)
        self.view.assert_called_once_with(self.control)
        self.assertEqual(self.view.Sresult['text'], "Missing some coefficients")

    def test_2_missingCoef(self):
        """проверка на случай с пропущенными коэф."""
        self.model(self.control)
        self.view.Sa.get = MagicMock(return_value=3)
        self.view.Sb.get = MagicMock(return_value='')
        self.view.Sc.get = MagicMock(return_value='')
        self.control.calculate()
        self.assertEqual(self.view.Sresult['text'], "Missing some coefficients")

    def test_3_twoRoot(self):
        """проверка на квадратное уравнение с двумя корнями"""
        self.model(self.control)
        self.set_coefficients(1, -3, -4)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], (-1.0, 4.0))

        self.set_coefficients(1, 2, -3)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], (-3.0, 1.0))

    def test_4_oneRoot(self):
        """проверка на один корень уравнения"""
        self.model(self.control)
        self.set_coefficients(1, -6, 9)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], 3.0)
        self.model(self.control)

        self.set_coefficients(1, 6, 9)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], -3.0)

        self.set_coefficients(0, 6, 9)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], -1.5)

    def test_5_noRoot(self):
        """проверка на отсутсвие корней"""
        self.model(self.control)
        self.set_coefficients(5, 2, 3)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], '∅')

        self.set_coefficients(0, 0, 3)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], '∅')

    def test_6_infRoot(self):
        """проверка на бесконечное множество корней"""
        self.model(self.control)
        self.set_coefficients(0, 0, 0)
        self.control.calculate()
        self.view.Sa.get.assert_called_once()
        self.view.Sb.get.assert_called_once()
        self.view.Sc.get.assert_called_once()
        self.assertEqual(self.view.Sresult['text'], '∞')

    def test_7_wrongInput(self):
        """проверка на неправильный ввод"""
        self.model(self.control)
        self.set_coefficients("abc", "number", "five")
        self.control.calculate()
        self.assertEqual(self.view.Sresult['text'], "could not convert string to float: 'abc'")

        self.set_coefficients("7", "number", "five")
        self.control.calculate()
        self.assertEqual(self.view.Sresult['text'], "could not convert string to float: 'number'")

        self.set_coefficients("5", "6", "7five")
        self.control.calculate()
        self.assertEqual(self.view.Sresult['text'], "could not convert string to float: '7five'")
