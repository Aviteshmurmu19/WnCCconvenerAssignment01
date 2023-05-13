from bs4 import BeautifulSoup as bs                                     #1 Importing BeautifulSoup4
import requests as req                                                  #2 Importing requests library
from csv import writer                                                  #3 Importing csv to create/store all the data fetched
import pandas as pd
import time

def fetch_itc():
        html_text = req.get('https://itc.gymkhana.iitb.ac.in/wncc/soc/').text
        #print(html_text)

        soup = bs(html_text, 'lxml')

        #print(soup.prettify())
        store = soup.find_all('div', class_='col-lg-4 col-6 mb-4 shuffle-item')
        #print(store)
        for courses in store:
                course = courses.find('p', class_ = "lead text-center font-weight-bold text-dark").text
                links = 'https://itc.gymkhana.iitb.ac.in'+courses.find('div', class_ = "rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white").a['href']
                tags = courses['data-groups'].replace("[","").replace("]","").replace('"','').replace(",",", ")
                typ = tags.split(",")[0]
                year = tags.replace(", ",",").split(",")[1]

                #Debug
                if links == 'https://itc.gymkhana.iitb.ac.in/wncc/soc/projects/2023/project285.html':
                        continue
                #Debug

                #print(course)
                #print(links)
                print(f"Course Name                     : {course}")
                print(f"Links to Course                 : {links}")
                print(f"Type                            : {typ}")
                print(f"Year                            : {year}")
                print(f"Tags                            : {tags}")

                t = time.localtime()
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

                save = [course,links,tags,typ,year,current_time]
                #print (course, type(course))
                #print (save, type(save))

                with open('data.csv', 'a') as data:
                        writer_object = writer(data)
                        writer_object.writerow(save)
                        data.close()

                print('\n')
        print('Saved to data.csv !')

if __name__ == "__main__":

        print("Should I Retrieve the List of Courses Offered During the Season of Code by the Web and Coding Club at IIT Bombay? [y/n]")
        reply = input('> ')
        if reply == 'yes' or reply == 'Yes' or reply == 'y' or reply == 'Y' or reply == 'ok' or reply == 'Ok' or reply == 'OK' or reply == 'YEs' or reply == 'YES' or reply == 'please' or reply == 'Please' or reply == '1':
                print("Should I Retrieve that Again and Again ? [in minutes. 0 for once only.]")
                timee=int(input('> '))
                while True:
                        print('Fetching Content...\n')
                        time.sleep(1)

                        fetch_itc()

                        print(f"Data stored at data.csv !!!\n")

                        if timee != 0:
                                time_wait = timee                                                               #in minutes
                                print(f'Waiting {time_wait} minutes...')
                                for i in range(time_wait*60):
                                        print(f"Wait {time_wait*60-i} seconds")
                                        time.sleep(1)
                        else:
                                print("Closing in 20 seconds.")
                                time.sleep(20)
                                break
