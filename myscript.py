import os


def main():
    bad_hash = 'c1a4be04b972b6c17db242fc37752ad517c29402'
    good_hash = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'
    os.system(f'git bisect start {bad_hash} {good_hash}')
    os.system('git bisect run python manage.py test')
    os.system('git bisect reset')


if __name__ == "__main__":
    main()
