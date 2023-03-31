import os
import sys


def main(bad_hash, good_hash):
    os.system(f'git bisect start {bad_hash} {good_hash}')
    os.system('git bisect run python manage.py test')
    os.system('git bisect reset')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
