import requests
from send_email import send_email


api_key = 'b6e52d6f13074a6886fc5ca349cfd97f'
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-06-09&" 
       "sortBy=publishedAt&apiKey=b6e52d6f13074a6886fc5ca349cfd97f&"
       "language=en")
page = requests.get(url)
page_in_json = page.json()

contents = ''
for article in page_in_json['articles'][:20]:
       if article['description'] is not None:
              contents = (contents + article['title'] +
                          '\n' + article['description'] + '\n'
                          + article['url']+ 2*'\n')

contents = contents.encode('utf-8').strip()
send_email(contents)