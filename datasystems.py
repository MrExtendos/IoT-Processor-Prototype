# Name: Jeremie Saint Amour
# Course: Computer Architecture - IoT Processor Prototype
# Task 1: Data Systems
# Description:
# Implements a 32-bit signed integer system using Two's Complement representation.
# Handles conversion between Decimal, Binary, and Hexadecimal.
# Includes overflow detection and saturation logic.

MIN_INT32 = -2147483648
MAX_INT32 = 2147483647
MASK32 = 0xFFFFFFFF

# ---------------------------
# Parse input
# ---------------------------
def parse_input(value_str):
    return int(value_str.strip())


# ---------------------------
# Overflow Detection + Saturation
# ---------------------------
def apply_saturation(x):
    overflow = 0
    saturated = 0

    if x > MAX_INT32:
        overflow = 1
        saturated = 1
        x = MAX_INT32

    elif x < MIN_INT32:
        overflow = 1
        saturated = 1
        x = MIN_INT32

    return x, overflow, saturated


# ---------------------------
# Decimal -> 32bit Binary (Two's Complement)
# ---------------------------
def decimal_to_binary32(x):
    return format(x & MASK32, '032b')


# ---------------------------
# Binary -> Decimal (Signed)
# ---------------------------
def binary_to_decimal(bin_str):
    value = int(bin_str, 2)
    if value & (1 << 31):  # negative number
        value -= (1 << 32)
    return value


# ---------------------------
# Binary -> Hexadecimal
# ---------------------------
def binary_to_hex(bin_str):
    value = int(bin_str, 2)
    return "0x" + format(value, '08X')


# ---------------------------
# Output Formatter
# ---------------------------
def format_output(x, mode):
    mode = mode.upper()
    bin32 = decimal_to_binary32(x)

    if mode == "DEC":
        return str(binary_to_decimal(bin32))

    elif mode == "BIN":
        return bin32

    elif mode == "HEX":
        return binary_to_hex(bin32)

    else:
        raise ValueError("Mode must be DEC, BIN, or HEX")


# ---------------------------
# Main Processor Function
# ---------------------------
def process(value_str, mode):
    x = parse_input(value_str)
    x, overflow, saturated = apply_saturation(x)
    result = format_output(x, mode)

    return result, overflow, saturated


# ---------------------------
# Command Line Execution
# ---------------------------
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python datasystems.py <decimal_integer> <DEC|BIN|HEX>")
        sys.exit(1)

    value = sys.argv[1]
    mode = sys.argv[2]

    try:
        value_out, overflow, saturated = process(value, mode)

        print("value_out:", value_out)
        print("overflow:", overflow)
        print("saturated:", saturated)

    except Exception as e:
        print("Error:", e)