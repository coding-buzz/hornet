import uuid

from pygments.lexers._mapping import LEXERS
from repoze.lru import lru_cache


def upload_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(uuid.uuid4(), filename)


@lru_cache(maxsize=1)
def get_available_lexers():
    return sorted(map(lambda v: (v[2][0], v[2][0]), LEXERS.values()))


@lru_cache(maxsize=32)
def get_page_range(active_page, pages_count):
    first_page = max(1, active_page - 2)
    last_page = min(first_page + 5, pages_count + 1)
    if last_page - first_page < 5:
        diff = 5 - (last_page - first_page)
        first_page = max(1, first_page - diff)
    return range(first_page, last_page)
