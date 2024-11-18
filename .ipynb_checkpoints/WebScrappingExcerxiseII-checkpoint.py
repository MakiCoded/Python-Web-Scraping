import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

webpage = requests.get(url)

parsed_webpage = BeautifulSoup(webpage.content, "html.parser")

python_job = parsed_webpage.find_all("div", class_="column is-half")


all_titles =[]
all_names =[]
all_locations =[]
all_dates = []


for jobs in python_job:
    title = jobs.find("h2", class_ ="title is-5").text\
    ##append all titles
    all_titles.append(title)
    
    name = jobs.find("h3", class_ = "subtitle is-6 company").text
    ##append all names
    all_names.append(name)
    
    location = jobs.find("p", class_="location").text
    ## append all locations
    all_locations.append(location)
    
    timeDate = jobs.find("p", class_ ="is-small has-text-grey").text
    #append all dates to
    all_dates.append(timeDate)
    print(title, name, location, timeDate )

    job_dict = {"Job_title": all_titles, "All_Name": all_names, "All_location": all_locations, "All_Dates": all_dates}
    

df = pd.DataFrame(job_dict)

df.to_csv("joblisting.csv", index=False)
print("Done Converting......")