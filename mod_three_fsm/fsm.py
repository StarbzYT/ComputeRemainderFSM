# Finite state machine class with binary string input (API)
class Mod3FSM:
    def __init__(self):
        self.states = ["S0", "S1", "S2"]
        self.current_state = "S0"
        # binary string has either 0 or 1 (these are the valid string characters)
        self.alphabet = ("0", "1")
        self.transition_table = {
            "S0": {"0": "S0", "1": "S1"},
            "S1": {"0": "S2", "1": "S0"},
            "S2": {"0": "S1", "1": "S2"},
        }
    
    # private method to change from one state to another given current state and bit in binary integer
    def _change_state(self, state, bit):
        # validation checks
        if bit not in self.alphabet:
            raise ValueError(f"Bit passed in was not in {self.alphabet}")
        if state not in self.states:
            raise ValueError(f"State passed in was not in {self.states}")
        # proceed with state change if arguments are valid
        next_state = self.transition_table[state][bit]
        self.current_state = next_state
    
    # private method to reset state after we get remainder
    def _reset_state(self):
        self.current_state = self.states[0]

    # private method to get remainder based on final state
    def _remainder(self, final_state):
        remainders = {"S0": 0, "S1": 1, "S2": 2}
        if final_state not in self.states:
            raise ValueError(f"State passed in was not in {self.states}")
        return remainders[final_state]

    # calculate remainder by iterating through input string and changing states
    def get_remainder(self, binary_integer):
        if not isinstance(binary_integer, str):
            raise TypeError("Input must be a string!")
        for bit in binary_integer:
            self._change_state(self.current_state, bit)
        # calculate remainder based on final state
        remainder = self._remainder(self.current_state)
        self._reset_state()
        return remainder
