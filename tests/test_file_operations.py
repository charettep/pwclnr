import unittest
import os
import pandas as pd
from scripts.file_operations import log_removed_rows

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # Create a DataFrame with test data
        self.df = pd.DataFrame({
            "url": ["http://example.com", "http://sub.example.com"],
            "username": ["user1", "user2"],
            "password": ["pass1", "pass2"]
        })
        # Ensure a clean output folder
        if os.path.exists("output/removed_rows.csv"):
            os.remove("output/removed_rows.csv")

    def tearDown(self):
        if os.path.exists("output/removed_rows.csv"):
            os.remove("output/removed_rows.csv")

    def test_log_removed_rows(self):
        file_path = log_removed_rows(self.df.copy(), "TestReason", "TestCode")
        self.assertTrue(os.path.exists(file_path))
        df_logged = pd.read_csv(file_path)
        # Check that the DataFrame includes the added columns
        self.assertIn("Domain", df_logged.columns)
        self.assertIn("ErrorCode", df_logged.columns)
        self.assertIn("Reason", df_logged.columns)

if __name__ == '__main__':
    unittest.main()
