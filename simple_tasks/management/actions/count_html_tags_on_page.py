import requests
import bs4
import logging
from sys import stderr


# import pytest
# import pyperclip
# import openpyxl
# import xlrd as xlrd


class OutputFormatter(logging.Formatter):
    def format(self, record):
        record.source_url = record.args.get("source_url")
        record.site_response_code = record.args.get("site_response_code")
        record.unique_tags_count = record.args.get("unique_tags_count")
        record.tags_count = record.args.get("tags_count")
        record.tags_with_attributes_count = record.args.get("tags_with_attributes_count")
        return super().format(record)


def start_parser_logger():
    logger = logging.getLogger()
    ch = logging.StreamHandler(stderr)
    # formatter = logging.Formatter('%s tags count result: Response: %s Unique tags count: %s Tags count: %s Tags with attributes count: %s')
    # ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    logging.basicConfig(level=logging.INFO, handlers=[ch])
    return logger


def get_page_content(source_url: str):
    logger = start_parser_logger()
    headers = ({'User-Agent':
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    site_response = requests.get(source_url, headers=headers)
    site_response_code = site_response.status_code
    if site_response_code == 200:
        html_soup = bs4.BeautifulSoup(site_response.text, 'html.parser')

        tags_content = [tag for tag in html_soup.find_all()]
        tags_with_attributes = [tag for tag in tags_content if tag.attrs]

        tags_count = len(tags_content)
        unique_tags_count = len(set([tag.name for tag in tags_content]))
        tags_with_attributes_count = len(tags_with_attributes)

        logger.warning('%(source_url)s tags count result:'
                       '\nResponse: %(site_response_code)s'
                       '\nUnique tags count: %(unique_tags_count)s'
                       '\nTags count: %(tags_count)s'
                       '\nTags with attributes count: %(tags_with_attributes_count)s'
                       , {"source_url": source_url,
                          'site_response_code': site_response_code,
                          'unique_tags_count': unique_tags_count,
                          'tags_count': tags_count,
                          'tags_with_attributes_count': tags_with_attributes_count,
                          })