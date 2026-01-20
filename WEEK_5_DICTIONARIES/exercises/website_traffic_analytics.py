#website taffic analytics
#As a data analyst, your job is to analyse the website traffic data for an ecommerce site
# because the marketing team needs to understand which pages users visit frequent
#The problem
#You have a log of page visit from 50 users
# You need to count how many times a page was visited
#The most and least popular pages
#Percentage of traffic each page receives
#Identify pages with low traffic that need promotion


print("\n" + "="* 50)
print("""
      WEBSITE TRAFFIC ANALYTICS

      AUTHOR :TEMITOPE OLUGBAMILA
      DECSRIPTION: 
      """)
print("="* 50)
print("="* 50)

import random
from pprint import pprint

pages = ["products", "product profile", "about", "home", "checkout", "cart", "contact"]
users = 50

visited_pages = []

for i in range (users):
    rounds= random.randint(3,20)
    for take in range(rounds):
      index = random.randint(0, 6)
      visited_pages.append(pages[index])
     
print(visited_pages)

#step 1-count page visits
#concept:use dictionary to count frequency-a fundamental data science task

page_counts = {}


for page in visited_pages:
   if page in page_counts:
      page_counts[page]=page_counts[page] + 1
   else:
      page_counts[page] = 1  

pprint(page_counts)   


#Step 2-Find most visited & least visited pages
#concept : extraxt insights from the frequency rate
all_visits = page_counts.values()
max_visit = max(all_visits)
min_visit = min(all_visits)

print("\nMost popular pages:")
for (key, value) in page_counts.items():
   #in this context, the key is the page name, while the value is the visit frquency- i.e how many 
   if value == max_visit:
      print(f"  -{key}: {value} visits")


print("\nLeast popular pages:")
for(key,value) in page_counts.items():
   if value == min_visit:
      print(f"  -{key}: {value} visits")


#step 3: Clculate traffic percentage
#concept:convert page visit count to percentages for better insight

total_visits = sum(page_counts.values())
print(f"\nTotal_visits: {total_visits}")
print("\nTraffic Distribution:")

page_percentages = {}

for (key, value) in page_counts.items():
   #in this context, the key is the page name, while the value is the visit frquency- i.e how many

   percentage = (value/total_visits) * 100
   page_percentages[key] = f"{percentage:.1f}" 
   print(f"  -{key}: {value} visits {page_percentages[key]}%")  
 
pprint(page_percentages) 

#step 4: Identify pages needing promotion
#concept: Use conditional logic with dictionary data to generate insight

low_traffic_threshold = 13 #percentage
low_traffic_pages = {}

print("\nPages needing promotion(< 13% of traffic):")

for (key, value) in page_percentages.items():
   percentage_value = float(value)

   if percentage_value <= low_traffic_threshold:
      low_traffic_pages[page] = percentage_value

if len(low_traffic_pages) == 0:
   print(" All pages have adequate tarffic")
else:
   pprint(low_traffic_pages)         







  
    