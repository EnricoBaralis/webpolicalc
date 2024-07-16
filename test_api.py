import unittest
from api import app


class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # Test for add operation
    def test_add(self):
        response = self.client.get("/add?a=10&b=20")
        self.assertEqual(response.json["result"], 30)
        print("add ok")

    def test_add_non_number(self):
        response = self.client.get("/add?a=10&b=abc")
        self.assertEqual(response.status_code, 400)
        print("add non-number ok")

    def test_add_no_params(self):
        response = self.client.get("/add")
        self.assertEqual(response.json["result"], 0)
        print("add no params ok")

    def test_add_one_param(self):
        response = self.client.get("/add?a=10")
        self.assertEqual(response.json["result"], 10)
        print("add one param ok")


    def test_subtract(self):
        response = self.client.get("/subtract?a=20&b=10")
        self.assertEqual(response.json["result"], 10)
        print("subtract ok")

    def test_subtract_non_number(self):
        response = self.client.get("/subtract?a=20&b=abc")
        self.assertEqual(response.status_code, 400)
        print("subtract non-number ok")

    def test_subtract_no_params(self):
        response = self.client.get("/subtract")
        self.assertEqual(response.json["result"], 0)
        print("subtract no params ok")

    def test_subtract_one_param(self):
        response = self.client.get("/subtract?a=10")
        self.assertEqual(response.json["result"], -10)
        print("subtract one param ok")


    def test_multiply(self):
        response = self.client.get("/multiply?a=10&b=20")
        self.assertEqual(response.json["result"], 200)
        print("multiply ok")

    def test_multiply_non_number(self):
        response = self.client.get("/multiply?a=10&b=abc")
        self.assertEqual(response.status_code, 400)
        print("multiply non-number ok")

    def test_multiply_no_params(self):
        response = self.client.get("/multiply")
        self.assertEqual(response.json["result"], 0)
        print("multiply no params ok")

    def test_multiply_one_param(self):
        response = self.client.get("/multiply?a=10")
        self.assertEqual(response.json["result"], 0)
        print("multiply one param ok")

    # Test for divide operation
    def test_divide(self):
        response = self.client.get("/divide?a=20&b=10")
        self.assertEqual(response.json["result"], 2)
        print("divide ok")

    def test_divide_non_number(self):
        response = self.client.get("/divide?a=20&b=abc")
        self.assertEqual(response.status_code, 400)
        print("divide non-number ok")

    def test_divide_no_params(self):
        response = self.client.get("/divide")
        self.assertEqual(response.json["result"], "Error: Division by zero")
        print("divide no params ok")

    def test_divide_one_param(self):
        response = self.client.get("/divide?a=10")
        self.assertEqual(response.json["result"], "Error: Division by zero")
        print("divide one param ok")

# Test for power operation
    def test_power(self):
        response = self.client.get("/power?base=2&exp=3")
        self.assertEqual(response.json["result"], 8)
        print("power ok")

    def test_power_non_number(self):
        response = self.client.get("/power?base=2&exp=abc")
        self.assertEqual(response.status_code, 400)
        print("power non-number ok")

    def test_power_no_params(self):
        response = self.client.get("/power")
        self.assertEqual(response.json["result"], 1)
        print("power no params ok")

    def test_power_one_param(self):
        response = self.client.get("/power?base=2")
        self.assertEqual(response.json["result"], 1)
        print("power one param ok")

# Test for square_root operation
    def test_square_root(self):
        response = self.client.get("/square-root?num=9")
        self.assertEqual(response.json["result"], 3)
        print("square root ok")

    def test_square_root_non_number(self):
        response = self.client.get("/square-root?num=abc")
        self.assertEqual(response.status_code, 400)
        print("square root non-number ok")

    def test_square_root_negative(self):
        response = self.client.get("/square-root?num=-1")
        self.assertEqual(response.status_code, 400)
        print("square root negative ok")

# Test for modulus operation
    def test_modulus(self):
        response = self.client.get("/modulus?a=10&b=3")
        self.assertEqual(response.json["result"], 1)
        print("modulus ok")

    def test_modulus_non_number(self):
        response = self.client.get("/modulus?a=10&b=abc")
        self.assertEqual(response.status_code, 400)
        print("modulus non-number ok")

    def test_modulus_no_params(self):
        response = self.client.get("/modulus")
        self.assertEqual(response.json["result"], "Error: Division by zero")
        print("modulus no params ok")

    def test_modulus_one_param(self):
        response = self.client.get("/modulus?a=10")
        self.assertEqual(response.json["result"], "Error: Division by zero")
        print("modulus one param ok")


    def test_divide_by_zero(self):
        response = self.client.get("/divide?a=20&b=0")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json["error"], "division by zero")
        print("divide by zero ok")


if __name__ == "__main__":
    unittest.main()
