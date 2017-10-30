"""
selects users from subreddit using an unique set and returns [n] random ones
"""
import random
from typing import Set, List

import praw

class Finder(object):
    """finds users"""
    def __init__(self: Finder, reddit: praw.Reddit, subreddit: str, num: int = 100) -> None:
        self.reddit: praw.Reddit = reddit
        self.subreddit: praw.models.Subreddit = self.reddit.subreddit(subreddit)
        self.num = num

    def find_users(self: Finder) -> Set[praw.models.Redditor]:
        """finds users"""
        redditors: Set[praw.models.Redditor] = set()
        for submission in self.subreddit.submissions(1506816000, 1509408000):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                redditors.add(comment.author)

        return redditors

    def choose_users(self: Finder, reds: Set[praw.models.Redditor]) -> List[praw.models.Redditor]:
        """returns [n] amount of users"""
        return random.choices(list(reds), k=self.num)
