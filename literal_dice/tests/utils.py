import functools
from random import Random
from unittest.mock import patch


def patch_shuffle(func):
    @functools.wraps(func)
    def _patcher(self, *args, **kwargs):
        patcher = patch('literal_dice.literal_dice.random')
        self.addCleanup(patcher.stop)
        random = patcher.start()
        random.shuffle.side_effect = Random(123).shuffle

        func(self, *args, **kwargs)
    return _patcher
