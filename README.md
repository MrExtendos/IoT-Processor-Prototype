# IoT Processor Prototype – Task 1

This project implements the data system of a simple 32-bit processor architecture.

The processor:
• Accepts a decimal signed integer input
• Converts it to a 32-bit two’s complement representation
• Detects overflow
• Applies saturation (clamping)
• Outputs the value in DEC, BIN, or HEX format

## How to Run

In a terminal:

python3 datasystems.py <integer> <DEC|BIN|HEX>

Example:

python3 datasystems.py -45 HEX

## Run Tests

python3 -m unittest -v
