import requests
import matplotlib.pyplot as plt

links = [
		'',
		'',
		'https://www.myfooddiary.com/foods/524089/haagen-dazs-vanilla-ice-cream',
		'https://www.myfooddiary.com/foods/273303/ben-and-jerrys-ice-cream-vanilla',
		'https://www.myfooddiary.com/foods/4737307/breyers-ice-cream-all-natural-natural-vanilla',
		'https://www.myfooddiary.com/foods/6616606/blue-bell-homemade-vanilla-ice-cream',
		'https://www.myfooddiary.com/foods/7190510/halo-top-ice-cream-vanilla-bean',
		'https://www.myfooddiary.com/foods/7426483/baskin-robbins-vanilla-ice-cream',
		'https://www.myfooddiary.com/foods/7211411/talenti-tahitian-vanilla-bean-gelato',
		'https://www.myfooddiary.com/foods/7286859/kroger-deluxe-ice-cream-vividly-vanilla',
		'https://www.myfooddiary.com/foods/7259132/lactaid-vanilla-ice-cream',
		'https://www.myfooddiary.com/foods/3092704/schwans-vanilla-bean-ice-cream'
		]
name = ['Dreyer\'s', 'Blue Bunny', 'Haagen Dazs', 'Ben and Jerry\'s','Breyer\'s', 'Blue Bell', 'Halo Top', 'Baskin Robbins', 'Talenti', 'Kroger', 'Lactaid', 'Schwans']
size = ['59', '69']
cost = [0.0829, 0.179, 0.285, 0.24, 0.0729, 0.1075, 0.249, 0.212, 0.214, 0.0931, 0.140, 0.107]
for num in range(2,len(links)):
	website_url = requests.get(links[num]).text
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(website_url,'lxml')
	for hit in soup.findAll(attrs={'class' : 'badge'}):
	    size.append(hit.text[10:13])

overrun = [round(float(value.replace('g','')) / 1.2,2) for value in size]

temp = zip(name,overrun,cost)
sort = sorted(temp, key=lambda x: x[2])

name, overrun, cost = zip(*sort)

 
colors = ['#2E86C1', '#3498DB', '#5DADE2', '#85C1E9', '#AED6F1', '#D6EAF8', '#F2D7D5', '#E6B0AA', '#D98880', '#CD6155', '#C0392B', '#A93226']
def paint():
	fig, ax = plt.subplots()
	for i in range(len(cost)):
		ax.scatter(name[i], overrun[i], color=colors[i])
	fig.suptitle('Ice Cream brands by value (percent overrun/ounce)', fontsize=20)
	plt.ylabel('Overrun (%)')
	plt.xlabel('Ice Cream brand (Vanilla)')
	plt.rcParams['font.family'] = 'sans-serif'
	labels = ax.get_xticklabels()
	plt.setp(labels, rotation=45, horizontalalignment='right')
	plt.show()

paint()
