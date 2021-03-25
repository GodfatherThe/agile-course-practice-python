#!/usr/bin/env python
# coding: utf-8

import unittest

from ShutinaSvetlana.model.batcher import Sorting


class TestBatcherSortClass(unittest.TestCase):
        def test_sort_5(self):
            arr = [5, 6, 1, 2, 0]
            result = Sorting(arr)
            result.batcher_sort()
            self.assertEqual('0 1 2 5 6', str(result.result_str()))

        def test_sort_15(self):
            arr = [5, 6, 1, 2, 0, 100, -5, 6, -10, 20, 5, 6, 1, 36, 25]
            result = Sorting(arr)
            result.batcher_sort()
            self.assertEqual('-10 -5 0 1 1 2 5 5 6 6 6 20 25 36 100', str(result.result_str()))

        def test_sort_10(self):
            arr = [5, 6, 1, 2, 0, 0.5, -2.5, 10, 20, 9, 10]
            result = Sorting(arr)
            result.batcher_sort()
            self.assertEqual('-2.5 0 0.5 1 2 5 6 9 10 10 20', str(result.result_str()))

        def test_sort_litter(self):
            arr = ['a', 'g', 'b', 'ad']
            result = Sorting(arr)
            result.batcher_sort()
            self.assertEqual('a ad b g', str(result.result_str()))

        def test_wrong_input(self):
            arr = 9
            with self.assertRaises(TypeError):
                Sorting(arr)

        def test_wrong_input_diff_type1(self):
            arr = [9, 'a']
            with self.assertRaises(TypeError):
                Sorting(arr)

        def test_wrong_input_diff_type2(self):
            arr = ['a', 9]
            with self.assertRaises(TypeError):
                Sorting(arr)

        def test_1_element(self):
            arr = [9]
            result = Sorting(arr)
            result.batcher_sort()
            self.assertEqual('9', str(result.result_str()))

        def test_wrong_elem_of_array(self):
            arr = [[1, 2], [2, 3]]
            with self.assertRaises(TypeError):
                Sorting(arr)
