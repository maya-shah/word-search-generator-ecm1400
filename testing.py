from refdef import create_word_search
from refdef import check_answer
from user_interface import cli_formatter
import unittest


class TestFunctions(unittest.TestCase):

    """

    This module was used to test the functions.

    """

    # def test_create_word_search(self):
    #    result = create_word_search(10, "words.txt")
    #    assert len(result) == 10
    # self.assertEqual(result, 10)

    def test_check_answer(self):
        ws = [["C", "A", "T"], ["M", "N", "B"], ["L", "T", "B"]]
        assert check_answer("cat", ws) == True
        assert check_answer("ANT", ws) == True
        assert check_answer("TBB", ws) == False
        assert check_answer("BAT", ws) == False


if __name__ == '__main__':
    unittest.main()
