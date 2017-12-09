import unittest
from inspect import getargspec
from q01_load_data.build import q01_load_data as student
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data as original
import dill
import pandas as pd
from pandas.util.testing import assert_frame_equal


class Testing(unittest.TestCase):
    def setUp(self):
        with open('q01_load_data/tests/user_sol.pkl', 'wb') as f:
            dill.dump(student, f)

        with open('q01_load_data/tests/test_sol.pkl', 'wb') as f:
            dill.dump(original, f)
        with open('q01_load_data/tests/user_sol.pkl', 'rb') as f:
            self.student_func = dill.load(f)
        with open('q01_load_data/tests/test_sol.pkl', 'rb') as f:
            self.solution_func = dill.load(f)
        self.data = 'data/elecdemand.csv'
        self.student_return = self.student_func(self.data)
        self.original_return = self.solution_func(self.data)

    #  Check the arguements of the function
     def test_timeseries(self):
        # Input parameters tests
        args = getargspec(student)
        self.assertEqual(len(args[0]), 1, "Expected argument(s) %d, Given %d" % (1, len(args)))
        self.assertEqual(args[3], (None), "Expected default values do not match given default values")
    

    def test_return(self):
        self.assertEqual(self.student_return[0], self.original_return[0], "The return values do not match expected values")
    
    def test_return_dataframe(self):
        assert_frame_equal(self.student_return[1], self.original_return[1],
                           obj="The return values do not match expected values")

