# Import packages
print("importing lib")
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
#from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os
def check_csv_exists(file_name):
    return os.path.isfile(file_name)


def amazon(url):
    headers = {
        'authority': 'www.amazon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
   
    # Replace "dp" with "product-reviews"
    url = url.replace("/dp/", "/product-reviews/")

    # Remove all characters after the 3rd "/"
    url_parts = url.split("/")
    Title = url_parts[3]
    csv_file_name = Title+'.csv'
    if check_csv_exists(csv_file_name):
        df = pd.read_csv(csv_file_name)
        return df,Title
    url_parts = url_parts[:6]

    modified_url = "/".join(url_parts)
    reviews_url=modified_url
    productUrl=modified_url
    print(reviews_url)

    #storing product name for flipkart
    path = "p_name.txt"
    with open(path, 'w') as file:
        file.write("")
        Title=Title.replace(" ","+")
        file.write(Title)

    # Define Page No

    # Extra Data as Html object from amazon Review page
    reviewlist = []
    def extractReviews(reviewUrl):
        print(reviewUrl)
        headers = {
        'authority': 'www.amazon.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
        resp = requests.get(reviewUrl, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        reviews = soup.findAll('div', {'data-hook':"review"})
        # print(reviews)
        for item in reviews:
            with open('outputs/file.html', 'w', encoding='utf-8') as f:
                f.write(str(item))
            
            review = {
                'Title': item.find('a', {'data-hook':"review-title"}).text.strip(),
                'Stars': item.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
                'Description': item.find('span', {'data-hook': 'review-body'}).text.strip() ,
            }
            reviewlist.append(review)  

    
    
    for i in range(1,4):
        print(f"Running for page {i}")
        try: 
            reviewUrl = productUrl.replace("dp", "product-reviews") + "?pageNumber=" + str(i)
            extractReviews(reviewUrl)
        except Exception as e:
            print(e)
            
    
    df = pd.DataFrame(reviewlist)
    print(df)
    return df,Title




