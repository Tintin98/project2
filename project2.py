"""
    Program name: project.py
    Author: Soran Dizay-Loftkaer
    Purpose of this code is to find the lowest average temperature for a 5 days trip
    through 5 different cities.
    Last modified: 5/8/19
"""
import requests
import json
from itertools import permutations

API_KEY = "4184978bccfb87d8e4016668779af080"
WS_URL = "https://api.openweathermap.org/data/2.5/forecast"


class City:
    """Stores the values for the cities name and highest temperature values."""
    def __init__(self, name, temperatures):
        self.name = name
        self.temps = temperatures

    def get_temperature(self, day):
        """Returns max temperature for each of the 5 days."""
        return self.temps[day]

    def __str__(self):
        """Returns the name."""
        return self.name, self.temps


class Route:
    """Stores given route for the trip"""
    def __init__(self, listed_cities):
        self.cities = listed_cities


    def temp_avg(self):
        """Method to find average temperature from permutations list"""
        a_temp = 0
        for e in range(len(self.cities)):
            a_temp += self.cities[e].get_tempurature(e)
        a_temp /= len(self.cities)
        return a_temp

    def __str__(self):
        """Returns the listed cities."""
        return self.cities


def api_call(id):
    """API call to find the 40 temp maxes and find the averages for 5 days"""
    query_string = "?id={}&units=imperial&APIKEY={}".format(id, API_KEY)
    request_url = WS_URL + query_string
    # print("Request URL: ", request_url)
    response = requests.get(request_url)
    if response.status_code == 200:
        d = response.json()
        city_name = d["city"]['name']
        lst = d['list']
        tmp_list = []
        for i in range(len(lst) // 8):
            li = [x for x in range(len(lst)) if x // 8 == i]
            tmp_list.append(max([lst[j]["main"]["temp_max"] for j in li]))
        return City(city_name, tmp_list)    # returns the city name and its 5 days max temps to City class.
    else:
        print("There was an error, check connection and try again.")
        return None


if __name__ == "__main__":
    id_list = json.loads(open("cities.json").read())
    cities = []
    for id in id_list:
        cities.append(api_call(id))

    # Best attempt
    avg_temp = 0
    # p = [i for i in permutations(range(5))]
    # print(p)
    temp_listed = []
    for i in range(len(cities)):
        city = cities[i]
        temp_listed.append(city.temps)
        # print(city.temperatures)
        avg_temp += city.get_temperature(i)
    print("Temperatures for each day in list: " + str(temp_listed))
    p = [list(i) for i in permutations(temp_listed)]
    print(p)
    added = []      #   Creating a list to put the added permutation/temp into
    for a in p:
        for c in a:
            added.append(sum(c))
    divided = []    #   Creating a list to pass added into
    for m in added:
        divided.append(m / 5)
    print(min(divided))
""" 
    Past this point are different methods tried to attempt an answer,
    initial reason for not deleting was that they might be helpful to review for other attempts
"""

    # print(avg_temp)
    # avg_temp /= len(cities)
    # print(avg_temp)



    # permut = permutations(range(len(cities)))
    # permut = [list(i) for i in permut]
    # # print(permut)
    #
    #
    # n_lst = []
    # for i in range(len(cities)):
    #     city = cities[i]
    #     n_lst.append(city.temps)
    # print(n_lst)



    # routes = [Route([cities[i] for i in p]) for p in permut]
    # print(routes)



    # avg_temp = 0
    #
    # p = list(permutations(range(5)))
    # print(p)
    # for i in range(len(cities)):
    #     city = cities[i]
    #     print(city.temps)
    #     avg_temp += city.get_temperature(i)
    # print(avg_temp)
    # avg_temp /= len(cities)
    # print(avg_temp)



    # for permut in range(len(cities)):
    #     city = cities[permut]
    #     print(city)
    #     avg_temp += city.get_temperature(permut)
    # avg_temp /= len(cities)
    # print(avg_temp)

    # for p in permut:
    #     for d in p:
    #         city = cities[d]
    #         for i in range(len(cities)):
    #             avg_temp = city.get_temperature(i)
                # avg_temp /= len(cities)

                # print(d)
                # print(avg_temp)
                # print(avg_temp)
            # print(city)



    # for p in permut:
    #     for d in p:
    #         city = cities[d]
    #         avg_temp = city.get_temperature(d)
    #         print(avg_temp)



    # for b in permut:
    #     for p in range(len(cities)):
    #         city = cities[p]
    #         # avg_temp += city.get_temperature(p)
    #         # avg_temp /= len(cities)
    #         # print(avg_temp)
    #         print(city)

    # avg_temp = 0
    # for i in range(len(cities)):
    #     city = ([cities[i] for i in p] for p in permut)
    #     print(city)
    #     avg_temp += city.get_temperature(i)
    # avg_temp /= len(cities)
    # print(avg_temp)

    # avg_temp = 0
    # p = list(permutations(range(5)))
    # print(p)