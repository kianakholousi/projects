# Logic Circuit calculator
This project provides a class called `Binary_conversion` that contains methods for converting decimal numbers to binary and vice versa. It also includes a class called `Calculator` that inherits from `Binary_conversion` and implements various arithmetic operations on binary numbers. The user enters decimal numbers, and the resulting output numbers are displayed in a seven-segment format (excluding base conversion operations). The user can select operations from the menu.

Operations:
1. Addition using full adder logic
2. Subtraction using adder-subtractor logic
3. Multiplication using binary multiplier logic
4. AND-OR-XOR using operators that implement these gates.
5. The conversion operation to the user's desired basis


## `Binary_conversion` Class

### `decimalToBinary(decimal)`

This method takes a decimal number as input and converts it to binary. It uses a recursive approach to divide the decimal number by 2 and append the remainder to a string. The process continues until the decimal number becomes zero. The final binary result is returned as a string.

### `binaryToDecimal(binary)`

This method takes a binary number as input and converts it to decimal. It iterates through each bit of the binary number, starting from the least significant bit, and calculates the decimal value by multiplying each bit with the corresponding power of 2. The decimal result is returned as an integer.

## `Calculator` Class

The `Calculator` class extends the `Binary_conversion` class and provides additional methods for performing arithmetic operations using binary numbers.

### `readyforcomputation(a, b)`

This method prepares the input numbers for computation by converting them to binary using the `decimalToBinary` method from the `Binary_conversion` class. It also equalizes the length of the binary numbers by adding leading zeros to the shorter number.

### `add(a, b, c="0")`

This method performs binary addition using a full adder logic. It takes two binary numbers `a` and `b` as input, along with an optional carry `c`. It iterates through each bit of the binary numbers, starting from the most significant bit, and calculates the sum and carry using XOR and AND logic gates. The result is returned as a binary string.

### `subtract(a, b)`

This method performs binary subtraction using a full adder-subtractor logic. It takes two binary numbers `a` and `b` as input. If the numbers have different signs, it performs addition by taking the two's complement of the negative number. If the numbers have the same sign, it performs subtraction by taking the two's complement of the second number and adding it to the first number. The result is returned as a binary string.

### `multiply(a, b)`

This method performs binary multiplication using a combination of full adders and AND logic gates. It takes two binary numbers `a` and `b` as input. It iterates through each bit of the second binary number, starting from the least significant bit, and performs partial multiplications with the first binary number using AND logic gates. The partial products are then added together using full adders. The result is returned as a binary string.

### `AND(a, b)`

This method performs bitwise AND operation on two binary numbers `a` and `b`. It iterates through each bit of the binary numbers and performs the AND operation. The result is returned as a binary string.

### `OR(a, b)`

This method performs bitwise OR operation on two binary numbers `a` and `b`. It iterates through each bit of the binary numbers and performs the OR operation. The result is returned as a binary string.

### `XOR(a, b)`

This method performs bitwise XOR operation on two binary numbers `a` and `b`. It iterates through each bit of the binary numbers and performs the XOR operation. The result is returned as a binary string.

