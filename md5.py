"""
The implementation of the MD5 algorithm is based on the original RFC at
https://www.ietf.org/rfc/rfc1321.txt.
"""

import struct
from argparse import ArgumentParser
from enum import Enum

from bitarray import bitarray


class MD5Buffer(Enum):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476


class MD5(object):
    _string = None
    _buffers = {
        MD5Buffer.A: None,
        MD5Buffer.B: None,
        MD5Buffer.C: None,
        MD5Buffer.D: None,
    }

    @classmethod
    def hash(cls, string):
        cls._string = string

        preprocessed_bit_array = cls._step_2(cls._step_1())
        cls._step_3()
        return preprocessed_bit_array

    @classmethod
    def _step_1(cls):
        # Convert the string to a bit array.
        bit_array = bitarray()
        bit_array.frombytes(cls._string.encode("utf-8"))

        # Pad the string with a 1 bit and as many 0 bits required such that
        # the length of the bit array becomes congruent to 448 modulo 512.
        # Note that padding is always performed, even if the string's bit
        # length is already conguent to 448 modulo 512, which leads to a
        # new 512-bit message block.
        bit_array.append(1)
        while bit_array.length() % 512 != 448:
            bit_array.append(0)

        return bit_array

    @classmethod
    def _step_2(cls, step_1_result):
        # Extend the result from step 1 with a 64-bit little endian
        # representation of the original message length (modulo 2^64).
        length = (len(cls._string) * 8) % pow(2, 64)
        length_bit_array = bitarray()
        length_bit_array.frombytes(struct.pack("<Q", length))

        result = step_1_result.copy()
        result.extend(length_bit_array)
        return result

    @classmethod
    def _step_3(cls):
        # Initialize the buffers to their default values.
        for buffer_type in cls._buffers.keys():
            cls._buffers[buffer_type] = buffer_type.value


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
    md5_hash = MD5.hash(arguments.string)

    print([int(byte) for byte in md5_hash.tobytes()])


if __name__ == "__main__":
    main()
