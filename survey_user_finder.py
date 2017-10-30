"""
selects users from subreddit using an unique set and returns [n] random ones
"""
from typing import Set, List, Tuple

import praw


class Finder(object):
    """finds users"""

    def __init__(self: Finder, reddit: praw.Reddit, subreddit: str, sample: int = 100,
                 days_back: int = 30) -> None:
        self.reddit: praw.Reddit = reddit
        self.subreddit: praw.models.Subreddit = self.reddit.subreddit(subreddit)
        self.sample = sample
        self.days_back = days_back

    def find_users(self: Finder) -> Set[praw.models.Redditor]:
        """finds users"""
        redditors: Set[praw.models.Redditor] = set()
        times: Tuple[int, int] = self.get_times()
        for submission in self.subreddit.submissions(times[0], times[1]):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                redditors.add(comment.author)

        return redditors

    def get_times(self: Finder) -> Tuple[int, int]:
        """returns timestamps"""
        import datetime
        now: datetime.datetime = datetime.datetime.now(datetime.timezone.utc)
        month_ago: datetime.datetime = now + datetime.timedelta(-self.days_back)
        return (int(now.timestamp()), int(month_ago.timestamp()))

    def choose_users(self: Finder, reds: Set[praw.models.Redditor]) -> List[praw.models.Redditor]:
        """returns [n] amount of users"""
        import random
        return random.choices(list(reds), k=self.sample)
