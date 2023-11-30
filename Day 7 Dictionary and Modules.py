# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:27:03 2023

@author: Web 123
"""

# capital={'yasir':'bro','jam':'br',"aon":'brot','Ak':'Big',}

# capital.get('aon')
# capital['Ali']='small'

# capital.items()
# print(capital)

# for country in capital:
#     print(country)

# for country,bro in capital.items():
#     print(f'The Capital of {country}, is {bro} ')
    
# print(capital.keys())
# print(capital.values()) 


# if 'ak' in capital:
#     print('it Contain Ak')


# capital = {'yasir': 'bro', 'jam': 'br', 'aon': 'brot', 'Ak': 'Big'}

# if 'Ak' in capital:
#     print('It contains Ak')


# l=[1,2,3,4,5,6,7,6,8,4,6]
# print(6 in  l)
 
# letter count in varibales

# u='''
# # "sdfhjfflksfjhjjkjkkj"
# # "sdjjkkjxbnnmzxjh"
# # "sfjhjhjhxcznbmnsfh"
# # "sfdfjhjhsjkfnbxc"
# # "njjhjhsfjhjksf"
# # "jahhjsfajbhssbnsf"
# # "sfajhhjhgghsfbnsf"
# # "sfjjhsjjhsf"
# # "shjhjjsfjsf"
# werklesdkljdg
# dgkjkjjker
# enkkcfkmer
# ermllkkljgf
# erknljkjkle

# '''
# letter_count={}
# for letter in u:
#     letter_count[letter.lower()]=letter_count.get(letter,0)+1
# # letter['m']=1    
# print(letter_count)



# import matplotlib.pyplot as plt


# # x,y = zip(*letter_count.items())
# # plt.bar(x,y)
# # plt.show()

# # a,b = zip(*letter_count.items())

# letter_count_clean={}
# for k,v in letter_count.items():
#     if k.isalpha():
#         letter_count_clean[k]=v
# print(letter_count_clean)

# x,y = zip(*letter_count.items())
# plt.bar(x,y)
# plt.show()

# l1=[1,2,3,4,5]
# l2=['a','b','c','d']
# joind=list(zip(l1,l2))
# # print(joind)

# plt.bar(l1,l2)
# plt.show()


# sher='''In the ever-evolving landscape of technology, data stands as the lifeblood that fuels innovation and drives decision-making across industries. The realm of data technology encompasses a vast array of tools, techniques, and methodologies aimed at collecting, storing, processing, and analyzing data to extract valuable insights. As we navigate the 21st century, the evolution of data technology continues to shape the way businesses operate, scientists conduct research, and individuals interact with the digital world.

# The journey of data technology can be traced back to the early days of computing when punch cards were used to input information. However, the real breakthrough came with the advent of databases in the 1960s, providing a structured and efficient way to organize and retrieve data. The relational database management system (RDBMS), introduced by Edgar F. Codd, marked a pivotal moment, laying the foundation for the structured storage and retrieval of data that still forms the backbone of many systems today.

# Fast forward to the present, and we find ourselves in the era of big data. The sheer volume, velocity, and variety of data generated daily have necessitated new approaches to handling information. Distributed computing frameworks like Apache Hadoop emerged, enabling the processing of massive datasets across clusters of computers. This shift opened the door to more advanced analytics, empowering organizations to uncover patterns and trends that were previously hidden in the vast sea of data.

# Cloud computing has further revolutionized the data technology landscape. With the ability to store and process data in the cloud, organizations can scale their infrastructure dynamically, paying only for the resources they use. This flexibility has democratized access to powerful computing resources, allowing even small businesses and startups to harness the capabilities of big data analytics.

# The rise of artificial intelligence (AI) and machine learning (ML) has added another layer of sophistication to data technology. These technologies leverage algorithms to analyze data, learn patterns, and make predictions or decisions without explicit programming. From recommendation systems to predictive analytics, AI and ML are transforming industries by automating tasks, optimizing processes, and providing valuable insights.'''


# # new_word=sher.split(' ')
# # # print(new_word)

# # for i in range(len(new_word)):
# #     new_word[i]=new_word[i].strip('\n')
# # print(new_word)

# letter_count1={}
# for letter in sher:
#     letter_count1[letter.lower()]=letter_count1.get(letter,0)+1
# # letter['m']=1    
# print(letter_count1)

# tup=(1,2,3,4)
# li=[5,6,7,8]
# st='Dera ghazi Khan'
  
# capitals = {'Paris': {'Paris': 'Spain', 'madrid': 'Paris'}, 'spain': {'madrid': 'Paris'}}

                        

# # for key,value in capitals.items():
# #     print(key,value)

# for key,value in capitals.items():
#     print(f'{value["Paris"]} is the capital of {key}, they speak {value["madrid"]}')

# contries={'france':{'capital':'paris','language':'french'},'spain':{'capital':'united Kigdom','language':'english'}}
# for key,value in contries.items():
#     print(f'{value["capital"]} is the capital of {key},they speak {value["language"]}')

# countriess = [
#     {"United States": {"capital": "Washington", "language": "English"}},
#     {"France": {"capital": "Paris", "language": "French"}},
#     {"Japan": {"capital": "Tokyo", "language": "Japanese"}},
#     {"India": {"capital": "New Delhi", "language": "Hindi"}},
# ]

# for countris in countriess.items():
#     print(f'{value["capital"]} is the capital of {key},the speake {value["language"]}')

# import collections 
# counter = collections.Counter(sher.lower())
# # counter = collections.counter(sher.lower())
# print(counter)

# import collections as Counter

# print(collections.Counter(sher.lower()))


# new_dict= collections.Counter(sher.lower())
# print(new_dict)

# new_dict = {k:v for k,v in new_dict.items() if k.isalpha()}


# new = {k:v for k,v in new_dict.items() if k.isalpha()}

# L = [x**2 for x in range(1,11)]
# print(L)

# M=[]
# for x in range(1,11):
#     M.append(x**2)

# l=[x**2 for x in range(1,5)]

# m=[]
# for x in range(1,6):
#     m.append(x**3)
# print(m)

# Qustion Number 1

# Question 1
# Can you remember how to check if a key exists in a dictionary?
# Using the capitals dictionary below write some code to ask the user to input
# a country, then check to see if that country is in the dictionary and if it is
# print the capital. If not tell the user it's not there.

# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#             'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#             'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#             'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}
            
# user_input = input('Which ountry Would you Like  to Check :>') 
# user_input = user_input.lower()

# while ('united kingdom' not in user_input and not user_input.isalpha()):
#     if user_input == 'united State':
#         break
#     print('You Must  Input String')
#     user_input=input('Which ountry Would you Like  to Check :>') 
#     \
# user_input = user_input.title()

# if user_input in capitals:
#     print(f' the Capitals of {user_input} is {capitals[user_input]}')
# else:
#     print('no data availble')


# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#             'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#             'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#             'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#             }

# user_input = input('Which country would you like to check?:> ')

# user_input = user_input.lower()


# def get_valid_input():
#     while True:
#         user_input = input('Which country would you like to check: ').strip().lower()

#         if user_input == 'united states':
#             break
#         elif user_input.isalpha():
#             return user_input.title()
#         else:
#             print('You must input a valid string.')

# capitals = {'France': 'Paris', 'Spain': 'Madrid', 'United Kingdom': 'London',
#             'India': 'New Delhi', 'United States': 'Washington DC', 'Italy': 'Rome',
#             'Denmark': 'Copenhagen', 'Germany': 'Berlin', 'Greece': 'Athens',
#             'Bulgaria': 'Sofia', 'Ireland': 'Dublin', 'Mexico': 'Mexico City'
#             }

# user_input = get_valid_input()

# if user_input in capitals:
#     print(f'The capital of {user_input} is {capitals[user_input]}')
# else:
#     print('No data available')


# def get_user():
#     while True:
#         user_input = input('Please Enter Cuntry Name  And Capital Was Print :>')
#         if  user_input == 'United States' :
#             break
#         elif user_input.isalpha():
#             return user_input.title()
#         else:
#             print('you must input a valid number')
# capitals = {'France': 'Paris', 'Spain': 'Madrid', 'United Kingdom': 'London',
#             'India': 'New Delhi', 'United States': 'Washington DC', 'Italy': 'Rome',
#             'Denmark': 'Copenhagen', 'Germany': 'Berlin', 'Greece': 'Athens',
#             'Bulgaria': 'Sofia', 'Ireland': 'Dublin', 'Mexico': 'Mexico City'
#             }
# user_input = get_user()
# if user_input in capitals:
#     print(f' The Capital of {user_input} is {capitals[user_input]}')
# else:
#     print('no Data Found')


# Question 2
# Write python code that will create a dictionary containing key, value pairs
# that represent the first 12 values of the Fibonacci sequence 
# i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}   

# n=12
# a,b=0,1
# d=dict()
# for i in range(1,n+1):
#     d[i] = a
#     a,b=b,a+b
# print(d)

# n=12
# a,b = 0,1
# d =dict()
# for i in range(1,n+1):
#     d[i]=a
#     a,b = b,a+b
# print(d)

# Question 3
# Create a dictionary to represent the open, high, low, close share price data 
# for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
# the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]

# companies = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
# key_names = ['Open','High','Low','Close']
# prices = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]

# d_1 = {}

# for i in range(len(key_names)):
#     d_1[companies[i]] = dict(zip(key_names,prices[i]))
        
# print(d_1) 

# companies= ['Python DS', 'PythonSoft', 'Pythazon','Pybook']
# key=['open', 'high', 'low', 'close']
# sets= [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
# d= {}
# for i in range(len(key)):
#     d[companies[i]] = dict(zip(key,sets[i]))
# print(d)

# Question 4
# Go to the python module web page and find a module that you like. Play with it, 
# read the documentation and try to implement it.

# import datetime
# today = datetime.date.today()
# print(f'Today Date  is  {today}')
# holiday=datetime.date(2023,12,3)
# delta = holiday-today
# print(f'Just {delta.days} days will the holiday')

# import datetime
# today = datetime.date.today()
# print(f'Today date Is {today}')
# holiday = datetime.date(2023,12,3)
# delta = holiday - today
# print(f'Just {delta.days} days Will the Holiday')


# import random
# keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# d=dict()
# for letter in keys:
#      d[letter] =random.randint(1,100)
# print(d)

# import matplotlib.pyplot as plt
# x,y = zip (*d.items())
# plt.bar(x,y)

# Question 6
# Create a dictionary containing 4 suits of 13 cards 
# ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

# suits=['Ace','Jack','Queen','King']
# rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

# deck=dict()
# for i in suits:
#     deck[i]=rank
# print(deck)





