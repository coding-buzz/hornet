import uuid

from pygments.lexers._mapping import LEXERS
from repoze.lru import lru_cache


def upload_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(uuid.uuid4(), filename)


@lru_cache(maxsize=1)
def get_available_lexers():
    return sorted(map(lambda v: (v[2][0], v[2][0]), LEXERS.values()))
