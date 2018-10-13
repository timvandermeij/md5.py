from argparse import ArgumentParser

from md5 import MD5


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

    print(md5_hash)


if __name__ == "__main__":
    main()
