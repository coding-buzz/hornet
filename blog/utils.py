import uuid


def upload_directory_path(instance, filename):
    return 'uploads/{0}/{1}'.format(uuid.uuid4(), filename)
