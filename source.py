#!/usr/bin/env

import argparse

from googleapiclient.discovery import build


def auth(key):
    return build('youtube', 'v3', developerKey=key)


def getPewdiepieChannel(youtube):
    request = youtube.channels().list(
        part='statistics',
        forUsername='pewdiepie'
    )

    return request.execute()


def main():
    parser = argparse.ArgumentParser(description='Start script with api key.')
    parser.add_argument('key',
                        help='The api key of the youtube application')
    args = parser.parse_args()

    youtube = auth(args.key)
    pewdiepie = getPewdiepieChannel(youtube)

    print(pewdiepie)



if __name__ == "__main__":
    main()