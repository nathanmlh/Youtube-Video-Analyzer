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

    if args.function == 'getUploads':
        recent_video_ids = info_getter.getRecentVideoIds()
        last_video_id = recent_video_ids[0]
        description = info_getter.getVideoDescription(last_video_id)
        print(description)

if __name__ == "__main__":
    main()


