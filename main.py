import requests
from pprint import pprint


class SuperHero():
  def __init__(self, name):
    self.name = name
    self.intelligence = self.__get_intelligence__(name)

  def __get_intelligence__(self, name):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    heroes = response.json()
    for hero in heroes:
      if hero['name'] == name:
        return hero['powerstats']['intelligence']

  def __lt__(self, other):
    return self.intelligence < other.intelligence

  def __str__(self):
    return f'{self.name} (intelligence: {self.intelligence})'


if __name__ == '__main__':
  Hulk = SuperHero('Hulk')
  print(f'Добавлен {Hulk}')
  Captain_America = SuperHero('Captain America')
  print(f'Добавлен {Captain_America}')
  Thanos = SuperHero('Thanos')
  print(f'Добавлен {Thanos}')

  max_intelligence_hero = max(Hulk, Captain_America, Thanos)
  print()
  print(f'Самый умный - {max_intelligence_hero}')