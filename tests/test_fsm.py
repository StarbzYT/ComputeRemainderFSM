import unittest
from mod_three_fsm import Mod3FSM

class TestMod3FSM(unittest.TestCase):

    def setUp(self):
        self.fsm = Mod3FSM()

    # test different binary integers
    def test_valid_remainder_1101(self):
        self.assertEqual(self.fsm.get_remainder('1101'), 1)

    def test_valid_remainder_1110(self):
        self.assertEqual(self.fsm.get_remainder('1110'), 2)

    def test_valid_remainder_1111(self):
        self.assertEqual(self.fsm.get_remainder('1111'), 0)

    def test_valid_remainder_1010(self):
        self.assertEqual(self.fsm.get_remainder('1010'), 1)

    def test_valid_remainder_000(self):
        self.assertEqual(self.fsm.get_remainder('000'), 0)

    def test_valid_remainder_1(self):
        self.assertEqual(self.fsm.get_remainder('1'), 1)

    def test_valid_remainder_10(self):
        self.assertEqual(self.fsm.get_remainder('10'), 2)

    def test_valid_remainder_11(self):
        self.assertEqual(self.fsm.get_remainder('11'), 0)

    def test_valid_remainder_1001001(self):
        self.assertEqual(self.fsm.get_remainder('1001001'), 1)

    def test_valid_remainder_10101(self):
        self.assertEqual(self.fsm.get_remainder('10101'), 0)

    # test empty string and if error messages are thrown correctly
    def test_empty_string(self):
        self.assertEqual(self.fsm.get_remainder(''), 0)

    def test_invalid_character_1102(self):
        with self.assertRaises(ValueError) as context:
            self.fsm.get_remainder('1102')
        self.assertEqual(str(context.exception), "Bit passed in was not in ('0', '1')")

    def test_invalid_character_11a1(self):
        with self.assertRaises(ValueError) as context:
            self.fsm.get_remainder('11a1')
        self.assertEqual(str(context.exception), "Bit passed in was not in ('0', '1')")

    def test_invalid_input_type_int(self):
        with self.assertRaises(TypeError) as context:
            self.fsm.get_remainder(1101)
        self.assertEqual(str(context.exception), "Input must be a string!")

    def test_invalid_input_type_none(self):
        with self.assertRaises(TypeError) as context:
            self.fsm.get_remainder(None)
        self.assertEqual(str(context.exception), "Input must be a string!")
    
    # test private methods' error messages
    def test_change_state_2(self):
        with self.assertRaises(ValueError) as context:
            self.fsm._change_state("S0", "2")
        self.assertEqual(str(context.exception), "Bit passed in was not in ('0', '1')")

    def test_change_state_s4(self):
        with self.assertRaises(ValueError) as context:
            self.fsm._change_state("S3", "1")
        self.assertEqual(str(context.exception), "State passed in was not in ['S0', 'S1', 'S2']")
    
    def test_remainder_lookup_s4(self):
        with self.assertRaises(ValueError) as context:
            self.fsm._remainder("S3")
        self.assertEqual(str(context.exception), "State passed in was not in ['S0', 'S1', 'S2']")
    
    # more edge cases
    def test_edge_case_0(self):
        self.assertEqual(self.fsm.get_remainder('0'), 0)

    def test_edge_case_1(self):
        self.assertEqual(self.fsm.get_remainder('1'), 1)

    def test_edge_case_10(self):
        self.assertEqual(self.fsm.get_remainder('10'), 2)

    def test_edge_case_01(self):
        self.assertEqual(self.fsm.get_remainder('01'), 1)

if __name__ == '__main__':
    unittest.main()
