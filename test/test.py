import unittest
from unittest.mock import patch
from io import StringIO
from alertg.app import main


class TestApiKey(unittest.TestCase):
    def test_empty_opsgenie_api_key(self):
        with patch(
            "sys.argv",
            [
                "app.py",
                "--opsgenie-api-key",
                "",
                "--etherscan-api-key",
                "VALID_ETHERSCAN_API_KEY",
            ],
        ), patch("sys.stderr", new=StringIO()) as stderr:
            with self.assertRaises(SystemExit):
                main()
            self.assertEqual(
                stderr.getvalue().strip(),
                "usage: app.py [-h] --opsgenie-api-key OPSGENIE_API_KEY --etherscan-api-key ETHERSCAN_API_KEY\napp.py: error: the following arguments are required: --opsgenie-api-key",
            )

    def test_empty_etherscan_api_key(self):
        with patch(
            "sys.argv",
            [
                "app.py",
                "--opsgenie-api-key",
                "VALID_OPSGENIE_API_KEY",
                "--etherscan-api-key",
                "",
            ],
        ), patch("sys.stderr", new=StringIO()) as stderr:
            with self.assertRaises(SystemExit):
                main()
            self.assertEqual(
                stderr.getvalue().strip(),
                "usage: app.py [-h] --opsgenie-api-key OPSGENIE_API_KEY --etherscan-api-key ETHERSCAN_API_KEY\napp.py: error: the following arguments are required: --etherscan-api-key",
            )


if __name__ == "__main__":
    unittest.main()
