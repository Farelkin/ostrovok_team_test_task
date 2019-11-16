#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import shutil
import re
import click

url_magazine = 'https://www.smashingmagazine.com{}'


def give_user_image(users_date, users_size):
    """
    The function by dates finds links to articles with wallpapers
    :param users_date: users date input
    :param users_size: users size input
    :return: link for download image
    """

    i = 1
    while True:
        if i == 1:
            r = requests.get(url_magazine.format('/category/wallpapers/'),
                             verify=False)
            if r.status_code == 404:
                break
        else:
            r = requests.get(url_magazine
                             .format(f'/category/wallpapers/page/{i}'),
                             verify=False)
            if r.status_code == 404:
                break
        i += 1

        soup = BeautifulSoup(r.text, 'html.parser')

        # -------------------- find first block --------------------
        div_featured = soup.find('div',
                                 class_='tilted-featured-article__content')

        # -------------- find date in the first block --------------
        date_featured = div_featured.find('time').attrs['datetime']
        date_featured = datetime.strptime(date_featured[:7], '%Y-%m') \
            .date().strftime('%Y-%m')

        if users_date == date_featured:
            link_featured = div_featured \
                .find('h2', class_='tilted-featured-article__title') \
                .a['href']

            find_size_and_download_img(link_featured, users_size)

        # ------------ find date and links from articles ------------
        articles = soup.find_all('article', class_='article--post')

        for tag in articles:
            date_from_articles = datetime \
                .strptime(tag.find('time')
                             .attrs['datetime'][:7], '%Y-%m')\
                .date().strftime('%Y-%m')

            if users_date in date_from_articles:
                links_from_articles = tag\
                                        .find('h1', class_='article--post__title')\
                                        .find('a')\
                                        .attrs['href']

                find_size_and_download_img(links_from_articles, users_size)


def find_size_and_download_img(link, users_size):
    """
    The function find links for download image
    :param link:
    :param users_size: users size input
    :return: download image
    """

    r = requests.get(url_magazine.format(f'{link}'), verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')

    tag_a = soup.find_all('a')
    download_links = []
    for link_from_tag_a in tag_a:
        if users_size in link_from_tag_a:
            download_links.append(link_from_tag_a.attrs['href'])

    # ------------ download images -------------------
    for img_link in download_links:
        response = requests.get(img_link, stream=True)
        img_link_split = img_link.split('/')[-1]

        with open(img_link_split, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response


@click.command()
def main():
    while True:
        info = input('Enter q to exit or enter run to run program\n')
        if info == 'q':
            break
        elif info == 'run':
            date = input('Enter date in form MM-YYYY: ')

            try:
                date = datetime.strptime(date, '%m-%Y').date()\
                                                       .strftime('%Y-%m')
            except Exception:
                print('Wrong format. Try again')
                continue

            try:
                size = input('Enter image size, for example 640x480: ')
                regular_ex = re.search(r'[\d{3}x\d{3}|\d{4}x\d{4}]', size)
                print(regular_ex)
                if regular_ex is None:
                    raise Exception
            except Exception:
                print('Wrong format. Try again')
                continue

            give_user_image(date, size)
        else:
            print('Wrong enter')
            continue


if __name__ == '__main__':
    main()
