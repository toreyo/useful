from bs4 import BeautifulSoup
from requests import get
import csv

cl_sb_scrape_csv = open('cl_sb_scrape_csv.csv', 'w', encoding="utf-8")
csv_writer = csv.writer(cl_sb_scrape_csv)
csv_writer.writerow(['title', 'date_posted', 'price', 'location', 'link'])


response = get('https://honolulu.craigslist.org/search/oah/sga?hasPic=1&query=Surfboards&srchType=A')

html_soup = BeautifulSoup(response.text, 'lxml')

title = []
date_posted = []
price = []
location = []
link = []

posts = html_soup.find_all('li', class_='result-row')

for post in posts:
    if post.find('span', class_='result-hood') is not None:
        # title
        title_link = post.find('a', class_='result-title hdrlnk')
        title_text = title_link.text
        title.append(title_text)
        print(title_text)

        # date_posted
        date_posted_info = post.find('time', class_='result-date')['datetime']
        date_posted.append(date_posted_info)
        print(date_posted_info)

        # price
        post_price = post.find('span', class_='result-price').text
        # post_price_strip = int(post_price.strip().replace("$", ""))
        # price.append(post_price_strip)
        print(post_price)

        # location
        post_location = post.find('span', class_='result-hood').text
        location.append(post_location)
        print(post_location)

        # link
        post_link = title_link['href']
        link.append(post_link)
        print(post_link)

        print()
        csv_writer.writerow([title_text, date_posted_info, post_price, post_location, post_link])
cl_sb_scrape_csv.close()
