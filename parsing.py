from bs4 import BeautifulSoup

with open('sample.html', 'r') as f:
    docs = BeautifulSoup(f, "html.parser")
# print(docs)

nav_left = docs.find_all("ul")[1]

a_tags = nav_left.find_all("a")

uni_list = []

for a_tag in a_tags:
    uni_list.append(a_tag.text)
print(uni_list)




table = docs.find('table')

tr = table.find_all('tr')


autumn = int(tr[2].find_all('td')[1].text.split()[0])
spring = int(tr[2].find_all('td')[2].text.split()[0])


result = autumn + spring


print(f"ჯამი: {result}")

