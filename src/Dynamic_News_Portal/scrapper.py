from bs4 import BeautifulSoup
import requests


def scrap(url, html_tag, class_name):

    response = requests.get(url)
    print("response: ", response)

    html_content = response.content
    print("html content: ", html_content)

    soup = BeautifulSoup(html_content, "html.parser") 
    print("SOUP: ", soup)

    title = soup.find(html_tag, class_ = class_name).text
    print('Title:', title)

    return title


if __name__ == '__main__':
    print("Started")
    url = 'https://www.manoramaonline.com/environment/environment-news/2023/03/09/unusual-the-mysterious-rain-of-worms-scares-china.html'
    html_tag = 'h1'
    class_name = "story-headline"
    scrap(url, html_tag, class_name) 

    