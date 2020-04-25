import argparse
from utils import parse_article_from_url, validate_url

from person_extractor import PersonExtractor

ap = argparse.ArgumentParser()
ap.add_argument('paths', nargs='*', default=None, help='Paths to local files or urls')
person_extractor = PersonExtractor(lang='en')


def start_interactive_mode():
    while True:
        text = input('>> ')
        people = person_extractor.extract_people(text)
        print(people)
        print()


def work_with_paths(paths):
    for path in paths:
        if validate_url(path):
            title, body = parse_article_from_url(path)
            text = title + '\n' + body
        else:
            with open(path) as f:
                text = f.read()
        people = person_extractor.extract_people(text)
        print(people)


if __name__ == '__main__':
    args = vars(ap.parse_args())
    paths = args['paths']
    if not paths:
        start_interactive_mode()
    else:
        work_with_paths(paths)
