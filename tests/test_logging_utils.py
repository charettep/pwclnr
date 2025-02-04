import unittest
import os
import pandas as pd
from scripts.logging_utils import log_removed_rows

class TestLoggingUtils(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "url": ["http://example.com"],
            "username": ["user1"],
            "password": ["pass1"]
        })
        if os.path.exists("output/removed_rows.csv"):
            os.remove("output/removed_rows.csv")

    def tearDown(self):
        if os.path.exists("output/removed_rows.csv"):
            os.remove("output/removed_rows.csv")

    def test_log_removed_rows_logging_utils(self):
        file_path = log_removed_rows(self.df.copy(), "LoggingTest", "E001")
        self.assertTrue(os.path.exists(file_path))
        df_logged = pd.read_csv(file_path)
        self.assertIn("Domain", df_logged.columns)
        # Verify the added error code and reason
        self.assertEqual(df_logged.loc[0, "ErrorCode"], "E001")
        self.assertEqual(df_logged.loc[0, "Reason"], "LoggingTest")

if __name__ == '__main__':
    unittest.main()
