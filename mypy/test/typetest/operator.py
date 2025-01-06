from operator import attrgetter, itemgetter
from typing import assert_type


def check_attrgetter():
    assert_type(attrgetter("name"), attrgetter[object])


def check_itemgetter():
    assert_type(itemgetter("name"), itemgetter[object])
