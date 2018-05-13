"""
The implementation of the MD5 algorithm is based on the original RFC at
https://www.ietf.org/rfc/rfc1321.txt.
"""

import struct
from argparse import ArgumentParser

from bitarray import bitarray


class MD5(object):
    def hash(self, string):
        return self._step_1(string)

    def _step_1(self, string):
        # Convert the string to a bit array.
        bit_array = bitarray()
        bit_array.frombytes(string.encode("utf-8"))

        # Pad the string with a 1 bit and as many 0 bits required such that
        # the length of the bit array becomes congruent to 448 modulo 512.
        # Note that padding is always performed, even if the string's bit
        # length is already conguent to 448 modulo 512, which leads to a
        # new 512-bit message block.
        bit_array.append(1)
        while bit_array.length() % 512 != 448:
            bit_array.append(0)

        return bit_array


def main():
    argument_parser = ArgumentParser(
        description="Compute the MD5 hash of a given string.",
    )
    argument_parser.add_argument(
        "string",
        type=str,
        help="The string to hash",
    )

    arguments = argument_parser.parse_args()

    md5 = MD5()
    print(md5.hash(arguments.string))


if __name__ == "__main__":
    main()
