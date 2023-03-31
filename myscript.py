import os


def main():
    bad_hash = input('Enter bad commit hash : ')
    good_hash = input('Enter good commit hash : ')
    os.system(f'git bisect start {bad_hash} {good_hash}')
    os.system('git bisect run python manage.py test')
    os.system('git bisect reset')


if __name__ == "__main__":
    main()
