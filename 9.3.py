import requests
from pprint import pprint
import os


if __name__ == '__main__':

  url = 'https://ru.stackoverflow.com/search'
  params = '?tab=newest&pagesize=50&q=created%3a2d%20is%3aquestion%20duplicate%3a0%20%5bpython%5d'
  r = requests.get(url + params)

  question_list = []

  temp_file = 'test.txt'

  with open(temp_file, 'wb') as f:
    f.write(r.text.encode('cp1251'))

  with open(temp_file, 'r', encoding='cp1251') as input_file:
    for line in input_file.readlines():
      if line[0:3] == 'В: ':
        question_list.append(line[:-12].rstrip())

  os.remove(temp_file)

  pprint(question_list)
