import unittest
from inspect import getargspec
from ..build import q05_feature_engineering_part4 as student
from greyatomlib.time_series_day_02_project.q05_feature_engineering_part4.build import q05_feature_engineering_part4 as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        with open('q05_feature_engineering_part4/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q05_feature_engineering_part4/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q05_feature_engineering_part4/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q05_feature_engineering_part4/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/elecdemand.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
    def test_timeseries(self):
        # Input parameters tests
        args = getargspec(student)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args)))

    def test_timeseries_default(self):
        args = getargspec(student)        
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")


    def test_return_dataframe(self):
        assert_frame_equal(self.student_return, self.original_return,
                           obj="The return values do not match expected values")

