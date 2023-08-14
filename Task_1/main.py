import json
from pprint import pprint
import random


class select_city(object):
    def __init__(self, file):
        self.file = file

    def all_sum(self):
        with open(self.file, encoding='utf-8') as f:
            total_sum = 0
            data = json.load(f)
            for x in data:
                pp = x["population"]
                total_sum = total_sum + pp
            og_dict = {}  # создаем новый словарь в виде город:вероятность
            for x in data:
                pp = x["population"]
                city = x["name"]
                pb = pp/total_sum
                og_dict.update({city: pb})

            chosen = []
            val = 0
            r = random.random()

            for n in sorted(og_dict, key=og_dict.get, reverse=True):
                prb = og_dict[n]
                if r <= prb:
                    print(n)
                    break
                else:
                    r = r-prb

        return chosen


def main():
    ee = select_city('/Users/ekks-job/Downloads/j.json')
    ee.all_sum()


if __name__ == '__main__':
    main()
