import requests
from readability import Document
from boilerpy3 import extractors
import re

extractor = extractors.ArticleExtractor()


def validate_url(url):
    """Checks for validity of the url"""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


def parse_article_from_url(url):
    """Parses the article in the url
    and returns the title and text
    """
    response = requests.get(url)
    doc = Document(response.text)
    article_html = doc.summary()
    content = extractor.get_content(article_html)
    title = doc.title()
    return title, content
