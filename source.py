#!/usr/bin/env

import argparse
import YoutuberInformationGetter


def main():
    parser = argparse.ArgumentParser(description='Start script with api key.')
    parser.add_argument('key',
                        help='The api key of the youtube application')
    parser.add_argument('youtuber',
                        help='The name of the youtuber you want')
    parser.add_argument('function',
                        help='The function we want to run')
    args = parser.parse_args()

    info_getter = YoutuberInformationGetter.YoutuberInformationGetter(args.key, args.youtuber)

    print(info_getter.getKey())
    print(info_getter.getName())
    print(args.function)

    print(info_getter.getDetails())
    info_getter.getComments(1)

if __name__ == "__main__":
    main()


