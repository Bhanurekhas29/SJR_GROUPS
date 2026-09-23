"""
Copies the git-committed media_seed/ into MEDIA_ROOT the first time the app
boots against a fresh (empty) persistent volume, so uploaded content shows
up immediately without wiping out anything an admin later uploads.
"""
import os
import shutil
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED_DIR = os.path.join(BASE_DIR, 'media_seed')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')


def main():
    if not os.path.isdir(SEED_DIR):
        return
    os.makedirs(MEDIA_DIR, exist_ok=True)
    if any(os.scandir(MEDIA_DIR)):
        print('seed_media: media/ already has content, skipping seed.')
        return
    shutil.copytree(SEED_DIR, MEDIA_DIR, dirs_exist_ok=True)
    print('seed_media: copied media_seed/ into media/.')


if __name__ == '__main__':
    sys.exit(main())
