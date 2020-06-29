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
        self.uploadsId = self.youtuber_channel.get('items')[0]['contentDetails']['relatedPlaylists']['uploads']

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

    def getUploadsId(self):
        """
        Gets the uploads id for the youtube
        :return: The uploads id
        """
        return self.uploadsId

    def getRecentVideoIds(self):
        """
        Returns a list of recent video ids
        :return: A list of video ids
        """
        response = self.youtube.playlistItems().list(
            part='contentDetails',
            playlistId=self.getUploadsId()
        ).execute()
        videos = response['items']

        video_ids = []
        for video in videos:
            video_ids.append(video['contentDetails']['videoId'])
        return video_ids

    def getVideoTitles(self, videoIds):
        """
        Returns a list of video titles base on the list of video ids
        :param videoIds: The video ids we want to get titles for
        :return: A list of titles
        """
        responses = self.youtube.videos().list(
            part='snippet',
            id=videoIds
        ).execute()
        items = responses['items']
        titles = [item['snippet']['title'] for item in items]
        return titles

    def getVideoTitle(self, videoId):
        """
        Returns a video titles base on a video ids
        :param videoId: The video id we want to get title for
        :return: The title for the video
        """
        response = self.youtube.videos().list(
            part='snippet',
            id=[videoId]
        ).execute()
        return response['items'][0]['snippet']['title']

    def getCommentsForVideoId(self, videoId):
        """
        Returns a list of comments related to a specified video
        :param videoId: The video id
        :return: A list of comments
        """
        response = self.youtube.commentThreads().list(
            part='snippet',
            videoId=videoId
        ).execute()

        video_comments = []
        for thread in response['items']:
            video_comments.append(thread['snippet']['topLevelComment']['snippet']['textDisplay'])
        return video_comments

    def getVideoCommentsObject(self, videoId):
        """
        Returns a dictionary resource for a videos comments
        :param videoId: The videos id we want to get
        :return: A dictionary resource for comments
        """
        # Format of object specified below:
        # {
        #   'id': string,
        #   'title': string,
        #   'comments': [string]
        # }
        return {'id': videoId, 'title': self.getVideoTitle(videoId),
                'comments': self.getCommentsForVideoId(videoId)}
