from bs4 import BeautifulSoup
import requests


def scrap(url, html_tag, class_name):

    response = requests.get(url)
    # print("response: ", response)

    html_content = response.content
    # print("html content: ", html_content)

    soup = BeautifulSoup(html_content, "html.parser") 
    # print("SOUP: ", soup)
    print("SOUP", soup.text)

    title = soup.find(html_tag, class_ = class_name).text
    # print('Title:', title)

    return title


if __name__ == '__main__':
    print("Started")
    url = "https://www.businesstoday.in/markets/market-commentary/story/sensex-climbs-600-pts-nifty-tops-17250-ril-shares-gain-ahead-of-board-meet-on-biz-demerger-375493-2023-03-31"
    html_tag = 'div'
    class_name = "story-with-main-sec"
    scrap(url, html_tag, class_name) 

    