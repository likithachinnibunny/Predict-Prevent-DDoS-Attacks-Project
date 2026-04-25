import unittest
from model import train_model

class TestDDoSSystem(unittest.TestCase):

    def test_attack_prediction(self):
        model = train_model([], [])
        result = model([400, 100])
        self.assertEqual(result, 1)

    def test_normal_traffic(self):
        model = train_model([], [])
        result = model([100, 20])
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
