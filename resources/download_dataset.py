#!/usr/bin/env python
"""
Usage:
    download_dataset.py DESTINATION_DIR --set SET_NAME

Options:
    -h --help   Show this screen.
    -s --set    Chose set to download (function/class/inline/all)
"""

import os
from subprocess import call
from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser(description="merge dataset")
    parser.add_argument(
        "--des",
        # "DESTINATION_DIR",
        type=str,
        help="Destination dir",
        default="download_2",
    )
    parser.add_argument(
        "--set",
        "-s",
        default="function",
        type=str,
        help="Chose set to download (function/class/inline/all)",
    )
    return parser.parse_args()


def main():
    args = get_args()

    print(args.des)
    destination_dir = os.path.abspath(args.des)
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    os.chdir(destination_dir)
    if args.set == "all":
        set_name = ["function", "class", "inline"]
    else:
        set_name = [args.set]

    for language in (
        # "javascript",
        "java",
        # "ruby",
        # "php",
        # "go",
        # "cpp",
        "python",
        # "c_sharp",
        # "c",
        # "rust",
    ):
        for _name in set_name:
            call(
                [
                    "wget",
                    "https://ai4code.blob.core.windows.net/thevault/v1/{}/{}.zip".format(
                        _name, language
                    ),
                    "-P",
                    destination_dir,
                    "-O",
                    "{}.zip".format(language),
                ]
            )
            call(["unzip", f"{language}.zip", "-d", f"{language}"])
            # call(['rm', '{}.zip'.format(language)])


if __name__ == "__main__":
    main()
