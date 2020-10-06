#!/usr/bin/python3.7
import argparse
import sys
import os


def validate_offset(offset):
    """Validate user-supplied offset"""

    try:
        # Ensure offset is hexadecimal
        off = int(offset, 16)
    except ValueError:
        print("    Error: Offset is not hexadecimal.")
        sys.exit()

    # Ensure offset is within range
    if (off < 2147483648) or (off > 2483027968):
        print("    Error: Offset is not within Dolphin memory range.")
        print("    Error: Value must be between 0x80000000 and 0x94000000")
        sys.exit()


def validate_input(file):
    """Validate user-supplied input file"""

    if not os.path.isfile(file):
        print(f"    Error: {file} does not exist.")
        sys.exit()


def modify_file(file, offset, output):
    """Modify user-supplied input file"""

    # Get the input file
    with open(file, 'r') as inp_file:
        data = inp_file.readlines()

    # Iterate through lines
    for i,line in enumerate(data):
        try:
            # A dirty check for if the line is a function
            first_address = int(line[2:10], 16)
        except ValueError:
            # Skip if not a function line
            pass
        else:
            # Add the offset to the addresses and convert them back to source format
            first_address = first_address + offset
            first_address = '{:08x}'.format(first_address)
            second_address = int(line[19:26], 16) + offset
            second_address = '{:08x}'.format(second_address)

            # Replace original line with edited addresses
            data[i] = line[:2] + first_address + line[10:18] + second_address + line[26:]


    # Write output file
    with open(output, 'w') as out_file:
        out_file.writelines(data)
    out_file.close()


def main(args):
    """Main"""

    # Get input file, default output file to input
    input_file = args.input
    validate_input(input_file)
    output = args.input

    # Get offset
    validate_offset(args.offset)
    offset = int(args.offset,16)

    # Get output file if supplied
    if args.output:
        output = args.output

    modify_file(input_file, offset, output)

    sys.exit()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                               description="Add an offset to a dolphin memory map.")

    parser.add_argument('-i', action="store",
                               dest="input", help="path to input map file",
                               required=True)

    parser.add_argument('-o', action="store",
                               dest="offset",
                               help="memory offset",
                               required=True)

    parser.add_argument('-x', action="store",
                        dest="output",
                        help="path to output file; defaults to input file")

    main(parser.parse_args())
