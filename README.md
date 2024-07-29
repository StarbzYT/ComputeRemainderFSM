# Policy Reporter - Technical Assignment

## Overview

I created this README to document my solution to this assignment, explain my thought processes, and also tell you how to run/test my code. As requested, this project implements a Finite State Machine (FSM) API to compute the remainder when a binary string, representing an unsigned binary integer, is divided by three. This approach leverages the FSM to transition through states based on input bits and compute the final remainder. 

## Design

The FSM is designed with three states (`S0`, `S1`, `S2`) corresponding to the possible remainders when a binary number is divided by three. The transitions between these states are defined based on the input bits (`0` or `1`):

- `S0` transitions to `S0` on input `0` and to `S1` on input `1`.
- `S1` transitions to `S2` on input `0` and to `S0` on input `1`.
- `S2` transitions to `S1` on input `0` and to `S2` on input `1`.

The final state after processing all input bits determines the remainder.

## Code Layout

```plaintext
ComputeRemainder/
├── README.md               # Project overview and instructions (what you are reading right now!)
├── mod_three_fsm/
│   ├── __init__.py         # Package initialization
│   ├── fsm.py              # FSM class implementation
│   ├── main.py             # An example program of how a developer might use the API
└── tests/
    ├── __init__.py         # Test package initialization
    ├── test_fsm.py         # Unit tests for the FSM
```

## Object Oriented Design: Mod3FSM Class
I thought of many ways to structure my class. But, in the end, I decided on creating multiple private methods as class helpers to compute the remainder.

### Object Initialization
```python
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
```
I thought it would be best to implement as many SOLID object-oriented principles as I could. For example, I thought about abstraction. If developers would use my API, I do not want them to worry about configuring FSM states, alphabets, transitions, etc.

### Private Methods
```python
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
```

The reason these methods start with '\_' is because this is a convention for Python classes. Methods beginning with an '_' tell developers that this should not be called outside of the class implementation. To increase robustness, I added error checks to enhance type safety.

## What I learned
- Last time I heard about a FSM was in my discrete math class. It was nice to apply theory to code.
- I put more focus on making my code production ready! This meant I needed to learn about Python exception handling.
- I improved my ability to write comprehensive unit tests.
- "There are no solutions. Only tradeoffs." I spent some hours thinking about OOD to ensure my API was easy to use for developers.

## Potential Improvements
- In my _remainder method, I could have initialized the "remainders" dictionary as a class attribute. This way, if another developer were to decide that we needed more states (i.e also want to divide by 4), they wouldn't need to change a bunch of methods. Code reusability!
- I could have made more public methods which give developers more flexibility to compute remainders on there own, instead of doing it for them in one method. However, my focus for this assignment was to make my API as easy to use as possible.
- There are probably more SOLID OOP principles I could have included in my could like dependency inversion, single responsibility, open/closed principle, etc. I am new to learning these, and I hope to get better at identifying when it is best to include them in my code.

## How to Run the Code

To run the example program and tests on **macOS**, follow these steps:

### Running the Example Program

1. **Navigate to the `mod_three_fsm` directory**:
    ```bash
    cd mod_three_fsm
    ```

2. **Run the example program**:
    ```bash
    python3 main.py
    ```

### Running the Tests

1. **Navigate to the root directory of the project (`ComputeRemainder/`)**:
    ```bash
    cd ..
    ```

2. **Run the tests**:
    ```bash
    python3 -m unittest discover -s tests
    ```

This will execute all the unit tests in `tests/test_fsm.py` to ensure the FSM is working correctly.
