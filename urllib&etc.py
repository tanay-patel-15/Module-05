import urllib.request
import requests
import ssl

def byURL():
  wiki="https://en.wikipedia.org/wiki/Python_(programming_language)"
  ssl_context = ssl._create_unverified_context()
  webhandler = urllib.request.urlopen(wiki, context=ssl_context)

  contents = webhandler.read()

  print(contents)



def byRequest():
  wiki="https://en.wikipedia.org/wiki/Python_(programming_language)"
  response = requests.get(wiki)
  print(response.text)

if __name__ == "__main__":
  byURL()
  ##byRequest()