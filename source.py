#!/usr/bin/env

import argparse

from googleapiclient.discovery import build


def auth(key):
    return build('youtube', 'v3', developerKey=key)


def getPewdiepieChannel(youtube):
    """
    This function returns pewdiepie's channel from youtube
    Takes in a build object that should be youtube
    """
    request = youtube.channels().list(
        part='contentDetails',
        forUsername='pewdiepie'
    )

    return request.execute()


def getPlaylist(youtube, id):
    """
    Gets playlist from id
    :param youtube: The youtube instance we are using
    :param id: The id of the playlist we want to get
    :return: playlist item
    """
    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=id,
    )

    return request.execute()


def getVideoNames(youtube, list_of_video_names):
    request = youtube.videos().list(
        part='statistics',
        id=list_of_video_names
    )

    return request.execute()


def main():
    parser = argparse.ArgumentParser(description='Start script with api key.')
    parser.add_argument('key',
                        help='The api key of the youtube application')
    args = parser.parse_args()

    youtube = auth(args.key)
    pewdiepie = getPewdiepieChannel(youtube)

    videos_id = pewdiepie['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print("The video id for pewdiepie's videos: ", videos_id)

    print()
    print('Now the videos')
    playlist = getPlaylist(youtube, videos_id)

    print()
    for item in playlist['items']:
        print(item)
    video_ids = [video['contentDetails']['videoId'] for video in playlist['items']]

    print(video_ids)

    print(getVideoNames(youtube, video_ids))


if __name__ == "__main__":
    main()