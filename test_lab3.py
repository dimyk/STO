import unittest
from unittest.mock import patch, mock_open
import lab1_uip

class TestServiceFunctions(unittest.TestCase):

    def test_load_data_empty_file(self):
        with patch('os.path.exists', return_value=False):
            self.assertEqual(lab1_uip.load_data(), {})

    def test_save_and_load_data(self):
        test_data = {'VIN123': [{'service': 'Oil change', 'date': '2023-01-01', 'mileage': '12000'}]}
        m = mock_open()
        with patch('builtins.open', m), patch('json.dump'), patch('json.load', return_value=test_data):
            lab1_uip.save_data(test_data)
            result = lab1_uip.load_data()
            self.assertEqual(result, test_data)

    @patch('builtins.input', side_effect=["VIN123", "Oil change", "2023-01-01", "12000"])
    def test_add_service(self, mock_inputs):
        data = {}
        with patch('builtins.print'):
            lab1_uip.add_service(data)
        self.assertIn("VIN123", data)
        self.assertEqual(len(data["VIN123"]), 1)
        self.assertEqual(data["VIN123"][0]['service'], "Oil change")

    @patch('builtins.input', side_effect=["VIN999"])
    def test_show_history_not_found(self, mock_input):
        data = {"VIN123": []}
        with patch('builtins.print') as mock_print:
            lab1_uip.show_history(data)
            mock_print.assert_called_with("Історії не знайдено.")

    def test_show_last_service(self):
        data = {
            "VIN123": [
                {"service": "Oil", "date": "2023-01-01", "mileage": "10000"},
                {"service": "Brake", "date": "2023-06-01", "mileage": "15000"},
            ]
        }
        with patch('builtins.print') as mock_print:
            lab1_uip.show_last_service(data)
            mock_print.assert_called_with("VIN123: 2023-06-01 | Brake @ 15000 км")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
