#!/usr/bin/env

# This class be able to receive a youtuber name and produce information for this youtube

from googleapiclient.discovery import build

class YoutuberInformationGetter:
    def __init__(self, key, name):
        self.api_key = key
        self.youtuber_name = name
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.youtuber_channel = self.youtube.channels().list(
            part='contentDetails',
            forUsername=self.youtuber_name
        ).execute()

    def getKey(self):
        """
        Gets the key passed in previously
        :return: The api key
        """
        return self.api_key

    def getName(self):
        """
        Gets the name of the youtuber
        :return: The name of the youtuber
        """
        return self.youtuber_name

    def getDetails(self):
        return self.youtuber_channel

    def getComments(self, video_id):
        """
        This function will get comments from the video_id
        :param video_id: The video id to get the comments from
        :return: A list of comments?
        """
        print("Getting comments for: ", video_id)