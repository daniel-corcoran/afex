Each program can only be 64 'commands' long. Each command can be represented as a long double. 

In an afex program, every value is a pointer. This means that an afex program can change any aspect of itself. 

process(array) # Array is the entire bytecode, process is the live interpreter. 

COMMANDS: 

0. Copy [a] [b] (Overwrites the value at index B with the value at index A)

1. Arithmatic (operator) (value_a) (value_b)\

    0. +

    1. -
    2. *
    3. quot
    4. pow
2. Comparator
3. goto_index
4. Print register 0

5: stop terminate
