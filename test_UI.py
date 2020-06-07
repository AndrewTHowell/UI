from unittest import TestCase
from unittest.mock import patch

import UI


class TestGetNum(TestCase):
    userInputs = {
        "negative": "-100",
        "zero": "0",
        "positive": "100",
        "nonDigit": "twenty",
        "empty": ""
    }

    def test_with_digit(self):
        userInput = [TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num")
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)

    def test_with_empty_string(self):
        userInput = [TestGetNum.userInputs["empty"], TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num")
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)

    def test_with_non_digit(self):
        userInput = [TestGetNum.userInputs["nonDigit"], TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num")
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)

    def test_on_minimum(self):
        minimum = -10
        minimumString = str(minimum)

        userInput = [TestGetNum.userInputs["negative"], minimumString]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", minimum=minimum)
        self.assertEqual(minimum, userNum)

    def test_below_minimum(self):
        userInput = [TestGetNum.userInputs["negative"], TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", minimum=-10)
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)

    def test_on_maximum(self):
        maximum = 10
        maximumString = str(maximum)

        userInput = [TestGetNum.userInputs["positive"], maximumString]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", maximum=maximum)
        self.assertEqual(maximum, userNum)

    def test_below_maximum(self):
        userInput = [TestGetNum.userInputs["positive"], TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", maximum=10)
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)

    def test_on_minimum_with_maximum(self):
        minimum = -10
        minimumString = str(minimum)

        userInput = [TestGetNum.userInputs["negative"], minimumString]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", minimum=minimum, maximum=10)
        self.assertEqual(minimum, userNum)

    def test_below_minimum_with_maximum(self):
        userInput = [TestGetNum.userInputs["negative"], TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", minimum=-10, maximum=10)
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)

    def test_on_maximum_with_minimum(self):
        maximum = 10
        maximumString = str(maximum)

        userInput = [TestGetNum.userInputs["positive"], maximumString]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", maximum=maximum, minimum=-10)
        self.assertEqual(maximum, userNum)

    def test_below_maximum_with_minimum(self):
        userInput = [TestGetNum.userInputs["positive"], TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", maximum=10, minimum=-10)
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)

    def test_with_wrong_order_min_max(self):
        userInput = [TestGetNum.userInputs["negative"], TestGetNum.userInputs["positive"], TestGetNum.userInputs["zero"]]
        with patch("builtins.input", side_effect=userInput):
            userNum = UI.getNum("Enter num", minimum=10, maximum=-10)
        self.assertEqual(int(TestGetNum.userInputs["zero"]), userNum)
