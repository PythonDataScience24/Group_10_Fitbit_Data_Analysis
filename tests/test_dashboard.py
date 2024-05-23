import unittest
from src.dashboard import select_subject, select_date_range, select_resolution, calculate_summary_statistics
import pandas as pd

class TestDashboard(unittest.TestCase):
    def test_select_subject(self):
        # Prepare test data
        test_df = pd.DataFrame({'Id': [1, 2, 3, 4, 5]})
        test_subject = [1, 2]

        # Call the function with the test data
        result_df = select_subject(test_df, test_subject)

        # Assert that the result is as expected
        self.assertEqual(test_subject, result_df['Id'].tolist())

    def test_select_date_range(self):
        test_df = pd.DataFrame({'DateTime': pd.date_range(start='2016-03-11', end='2016-05-12')})
        test_start_date = '2016-04-10'
        test_end_date = '2016-04-12'

        # Call the function with the test data
        result_df = select_date_range(test_df, test_start_date, test_end_date)

        # Assert that the result is as expected
        self.assertEqual(pd.to_datetime(test_start_date), result_df['DateTime'].min())
        self.assertEqual(pd.to_datetime(test_end_date), result_df['DateTime'].max())

    def test_select_resolution(self):
        # Prepare test data
        test_df = pd.DataFrame({
            'Id': [1] * 1440,
            'DateTime': pd.date_range(start='1/1/2022', periods=1440, freq='min'),
            'Steps': [i for i in range(24) for _ in range(60)]
        })
        test_resolution = 'Hours'

        # Call the function with the test data
        result_df = select_resolution(test_df, test_resolution)

        # Assert that the result is as expected
        self.assertEqual(result_df['Steps'].tolist(), [i*60 for i in range(24)])

    def test_calculate_summary_statistics(self):
        # Prepare test data
        test_df = pd.DataFrame({
            'Steps': [100, 200, 300, 400, 500],
            'Calories': [1000, 2000, 3000, 4000, 5000],
            'Intensity': [1, 2, 3, 4, 5],
            'Sleep': [6, 7, 8, 9, 10],
            'Heartrate': [60, 70, 80, 90, 100]
        })
        test_metric = 'Steps'

        # Call the function with the test data
        result = calculate_summary_statistics(test_df, test_metric)

        # Assert that the result is as expected
        expected_result = """Steps: \n Total: 1500.00 \n Mean: 300.00 \n Median: 300.00"""
        self.assertEqual(result.strip(), expected_result.strip())

if __name__ == '__main__':
    unittest.main()
