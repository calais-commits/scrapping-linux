import requests
from bs4 import BeautifulSoup
import pandas as pd

#Website
web = "https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2"
result = requests.get(web)  #Obtaining HTML page
content = result.text #Extracting text content from response "web"

#Arrays where the products, prices and ratings about the items in the page will we stored
products = []
prices = []
ratings = []

#Object "soup" able to analize HTML docs
soup = BeautifulSoup(content, features="html.parser") 

#This page have "a" elements, which inside have the information that we want to list (name, price and rating)
for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
  #We want to obtain the div element that contains the class attribute with the value that indicates the information we want to extract
  name=a.find('div', attrs={'class':'_4rR01T'})
  price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
  rating=a.find('div', attrs={'class':'_3LWZlK'})
  
  #The text content extracted from each variable "name, price, rating" will be stored in their respective arrays
  products.append(name.text)
  prices.append(price.text)
  ratings.append(rating.text)

#Now, create a data frame with the data of the arrays
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})

#Export the data frame to a .csv doc
df.to_csv('products.csv', index=False, encoding='utf-8') 