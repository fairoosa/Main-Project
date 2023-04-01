from bs4 import BeautifulSoup
import requests


def scraper(url, html_tag, class_name):

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
    url = "https://www.bbc.com/news/world-us-canada-65131913"
    html_tag = 'div'
    class_name = "ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0"
    scraper(url, html_tag, class_name) 

    