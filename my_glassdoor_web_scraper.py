# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 23:55:02 2023

@author: Valde

My version of glassdoor web screper. Inspired in anohter version that I cathed up in the internet and modified to my purposes.
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

def get_jobs(keyword, num_jobs, path, slp_time):
    
    #Chrome Driver
    options = webdriver.ChromeOptions()
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    #URL
    #url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP4.htm?pgc=AB4AA4EAWgAAAAAAAAAAAAAAAfe7RToAmwEEAREkCCgHHAkAgorSUgzh6dfDLUYq4Imi2czjuTzyyFNGxexmzQAG8hf30wCuYAhkh7U8JMcQXDnr3z%2BDQR3qsEW1272CiW9kW%2BjHWsl4Gdly2rFUK9xiKBcNORtHGzyO35QFMv1zDl7o9Pt%2FjC%2FiXAzlqEWMXTBAVnnd0lo2%2FVRCcjtJUmStruwxYB4XvOXIfR%2FFlqDX7a1FAAA%3D"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP8.htm?pgc=AB4AB4EA0gAAAAAAAAAAAAAAAfe7RToA%2BAECAUTwAgY6DqDJrdWdaJKDXURvYN4IKlIAFjWils96MAavlEFqm8Z8EZlbv2%2BFqV52O7QXRRYefP3a0tSnLMXsQ91K2tgXLjkw8QdVvR40xUetHZWIgK8LVyWxu6dKV4ABqTPwuB42usazO%2F%2FWJXkcuFnU9u2lXEnsO6KoLVFO%2BrOMcq2EOp4gg00sEPXgSzv2yJExSSZDJnZ%2FRoMgGpPJKoDEdcdT%2BMy17YQUc05ayRrraH8lsfWJM2qJw5D6WI7ZLjruTVF%2Bdw5QLDlooCzDk4rszGW7WMLtTAXrXCVG8YfwU%2FixPTIfDjfaKx%2FQ1jv7zvgdgFquAAA%3D"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP11.htm?pgc=AB4ACoEBLAAAAAAAAAAAAAAAAfe7RToBLAEFAUecAQYODRwKIgYBUko1fep%2FtbnFchM4eMH8%2B9PlQkdyrPdsL5KyGhl%2FiHo4OjgK63%2BYDP134DBwQu0D63Nlb%2FKTTaU%2FxFgx6NjaXcx3lAPV6IRNDI8Wtd9nhO%2FbdiXTK5M5EmeOhC1ToYMdTstFXOF2Owo4KMN6JYzbZjMdCUuGwpPVKfaWTqwBINZQdX1%2BcyKg5ZYFKo68TT2qA79V35%2BQe6Sg1QJXhUnsDZ2RMzDj85WmTGCeMIMga2XIVkNkoUQjHPlWTFK4AWcRKt3IjLgb%2BXBudkmTcgjQvGN%2Ftl%2FDLYYNzeOeTfPXpo68x%2Fj0Nw3JNIuQ5smnHNtQeolxDr1leuRs0QIGym7PnmUbtoyQMBMDbx2RKxB5MJug0%2Ba7nTfAgktJXzWgsgAA"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP14.htm?pgc=AB4ADYEBhgAAAAAAAAAAAAAAAfe8WlQBRwEGAUicAQYOGD4GUgZMBylq6N4lKeGrVwgzqShpXZzpat5dIv9uG4yeYwGvqDIdtc8J3pPfSMO5nHP4wsyxIE2xxsTy3bt7P%2By40aCs4GLz12Oc8EXuI9OAPD37%2BK8RTQGutwk%2Bnpx1VTjLFM4LeKtYUgx4EpUxN%2B6s6zQuQuT8Lrn%2BN689YQ0KmrtTZ%2FQiphkaxr09uxiKZAZtXmU4JH0iuodmE84pAK1a9rDvxn6UNYLN%2Bd9vxTRYTnSHrAhrjrRQ5xGEHwbzTOHsk47NzJQEU%2FBw17603ZoHUao4Ajfd0t%2B9yV%2F4UgML6UM%2BGrU0vplQVrm%2FMsT1UelF%2BVt%2BHIqjgQwWXRNfmuNSQDPcIoe6VIvDB0RUfEz3QourIA62vpscpA1vRTQyqf2yJLaCiMneNByuv8pXVf8DZMMDz9nkfb1jUJECXQAA"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP17.htm?pgc=AB4AEIEB4AAAAAAAAAAAAAAAAfe8wOEBQQEGAUuYAQgSJZIBBxoGDgcGMNnsnibwuipP5hnZ%2BvHfpK8SDvTFjmDqMnhogO1Aad4Jur4CBHEDrhQA0WxnYaSOlnx3rn6W3lF1vCZjx7wNnAkL35M9fq0aMsoH9bmaX7YLWdxMn6Q3sS2L5Luq8G4%2FMYjif%2F6ofXGp%2Fe%2B7OTIyog37jcTIvCX9teSeKvOwqAeki6IqKeCWdrBY9q92X0XAkiTa0Qa%2FjlS0lrFGmYeRSfm5PWzzPMEH3cbJ3w7Y5cpBCzX5759UYXCobrdBlco36zPyU5lWhiMLsWOA6QieLg8D2fQDfhfkMYny37utic2tlt%2B9MDdxBKZjsJ8W%2Bd3pHeaJspjWvVpEuOLMEeK41OC%2BL6J90pNSucFQdfNwc8io1xTh4G1h%2FhDF7XvcDV6kp5Nj7bMfwdXkYqgXBFmZEAAA"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP20.htm?pgc=AB4AE4ECOgAAAAAAAAAAAAAAAfe8wOEBLwEEAUukARUsBxAQMYvhdUnVBD9obF7YX7aBa5xoSLSJ%2FyzXeKJWh4X0g5exiI4VBz3H3FX9IPyYnNqGFqmRYlTZkkx%2F4O1y%2B3LoIdeXjyjg97cihHTAv3e8Wyh0G5EETacIxD7PRKFMAV91mQ5hH%2BgoS5ExzCrZW2M8BduAs9ckbe4%2FUjOdhQ40AlswVZYysP6c5uassJY2dMa%2BYYbY9CLjAONHZuxA9Taz0%2BBZGOtEb7HAwJV8CHSUa6LcRJJu0w18QgwXMLRiYtzWjfn%2BQAtCH82wHhb0yfyfIsZZs3%2FHS38Km6XJNJFpUOSsQCHAds1Uclu%2BahRW6tD1sRcZymEEp0T5JRoODicbpp4KjnL7lpGKsrVLomTLIU%2BpQahxWZpBx0CoDT4t%2BYWeqCA7RQAA"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP23.htm?pgc=AB4AFoEClAAAAAAAAAAAAAAAAfe8wOEBFgEDAUqoAQ44BhSMLQ4vlBqNocFdm3OZFwBKecVEdunEUYo5JmswuuitZer9h0c7fH%2FkD%2F0e721OmwAtv14npKv83OuWWlTkF%2FwXeSHx7hzIIbS22dOOCd3yopFOh%2BCSrFV4Tk%2FA%2BwhW8SzHWd70WYrghPU7dERNx5wmR0c7Etk89e11dw7P5NbSkaIDiBKAdqtOYSSq57uSZw%2FwjyC80P%2Bjwh%2BNanjPB44Cvnjn3TYBcd86KTgGhbdqUdoGhCKm8dGeT3QXCR01MtVSz6aFyxb4EU2OYPbgum2uPcX3f8zQeaHfEwNztvPeW8k%2BTxpB%2F%2Fhd4ohF33yeY8pwyDJJTv3ZHoje43FCkLCnTZpH8N85p%2FshEAbaAAA%3D"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP26.htm?pgc=AB4AGYEC7gAAAAAAAAAAAAAAAfe8wOEA7gEBAUVVTp0uiBB3ysjOCOu9xeUBy3opwFVQJc6jjqeD6tehXy66ErpHogpux%2B8e4KImJKK6SXoE7vTqdr8aI%2BDqU3LGo7LOsFrojvOaFuNU9WLkQfwd1BHSmUgMwRMtXknTVwFnE5JoXi0SKriHkhEuQQ5Au1c1HLKTfK8MIV%2F4UK9p8TWVvBuwgLGNePjA3bCrHDinEzErkEmgo8KIIBTuDyyj6dbPIzLvixnxWDs9NyZKxGBIaeCy7G1s%2BDi3Mg6ifQZylIBLYdcaC10e27hXPg3JZk%2BsjG8FdK7TMWpA3PzO7vmbnWOW4rZia40AAA%3D%3D"
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP29.htm?pgc=AB4AHIEDSAAAAAAAAAAAAAAAAfe8wOEArAECASJICgmZ0HZgUl7miUNbvs7UEPLl8pju9MCMS%2B%2F%2F%2FSghGXsiPxvxjSjKN0DbxagB7CwlPfaQvxI%2FUG1r2LZyoas5568jOr%2FOJ4GuX675zpiF1xSPa0ZC2cHso43T%2FfDygvTlFpo7%2BOWN0rM3xPpeeM3gtfxsrOw17lb4q6Jt9ggoe%2FqPgPcjLp3s8vyJaUFpj4wvS8f8lpwoTSw99pK%2FQIZtF5J1H4kjTG4AAA%3D%3D"
    url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP30.htm?pgc=AB4AHYEDZgAAAAAAAAAAAAAAAfe8wOEAlgEEARY4BhgHFAYJcHyBUa0cLRDZnVeyQdLIGCHNinoBMg3bOTooO5sgonBlzbfzHPCbY4%2FhMXwX7ZzEc9CJ5pE9PIceIGssqbR4t%2FDGi80urVjKrIRm4LmsUtvVvXcvmyYZpFEcGx32r6dK5hHvVfIU4e94UeQEMjtKv%2FS1q6g3GSr2fwkLOeup71ytcFSwthgwA1tSmwAA"
    
    """
    Such diferent URL is because of the 'Error loading' that the side will give if a number of num_jobs is too high and it made many requests to the site being impossible to load all the jobs.
    Because of that if you want to make like 1000 jobs you have to divide this work per 10, basicaly 100 jobs 10 times, but because of the nature of the site you'll need 1100, this 100 more is
    because of the 10 jobs that can be repeated 10 times in order to continue of the last lage that were given to as via currenturl in the final of this code, this URL that were given is the last current
    and you have to but it above to continue catching more jobs until you finish with all 1000 jobs.
    """
    
    driver.get(url)
    
    #Put the jobs first in an list, then will be converted to a dataframe.
    jobs = []

    while len(jobs) < num_jobs:
        
        time.sleep(slp_time) #Change based your internet conection speed.
        
        try:
            newselected = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[1]")
            newselected.click()
        except ElementClickInterceptedException:
            pass
        
        time.sleep(.1)

        try:
            driver.find_element_by_css_selector('[alt="Close"]').click() 
        except NoSuchElementException:
            pass
        
        #Finding the jobs in the list
        job_buttons = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li")

        #Initiate the loop for every each.
        for job_button in job_buttons:
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break
            
            job_button.click()  #You might 
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    
                    driver.implicitly_wait(1)
            
                    company_name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div').text
                    location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    job_title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    job_description = driver.find_element(By.XPATH, '//*[@id="JobDescriptionContainer"]').text                        
        
                    collected_successfully = True    
                    
                except NoSuchElementException:
                                                
                    #print("We have an expetion here: NoSuchElementException")
                        
                    job_description = -1
                    #print(job_description)
                        
                    job_title = -1
                    #print(job_title)
                        
                    location = -1
                    #print(location)
                        
                    company_name = -1
                    #print(company_name)

                    collected_successfully = True    
                        
                except StaleElementReferenceException:
                        
                    #print("We have an expetion here: StaleElementReferenceException")
                        
                    job_description = driver.find_element(By.XPATH, '//*[@id="JobDescriptionContainer"]').text
                    #print(company_name)
                        
                    job_title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    #print(company_name)
                        
                    location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    #print(company_name)
                        
                    company_name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div').text
                    #print(company_name)
                        
                    collected_successfully = True    

            try:
                salary_estimate = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
                
            except NoSuchElementException:
                #print("We have an expetion here: NoSuchElementException")
                salary_estimate = -1 #You need to set a "not found value. It's important."
                #print(salary_estimate)
            except StaleElementReferenceException:
                #print("We have an expetion here: StaleElementReferenceException")
                salary_estimate = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
                #print(salary_estimate)
            
            try: 
                rating = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[28]/div[1]/span').text
                
            except NoSuchElementException:
                #print("We have an expetion here: NoSuchElementException")
                rating = -1 #You need to set a "not found value. It's important."
                #print(rating)
            except StaleElementReferenceException:
                #print("We have an expetion here: StaleElementReferenceException")
                rating = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[28]/div[1]/span').text
                #print(rating)
                
            try:
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]').click()
                
                try:
                    headquarters = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text                        
                except NoSuchElementException:
                    #print("We have an expetion here: NoSuchElementException")
                    headquarters = -1
                    #print(headquarters)
                except StaleElementReferenceException:
                    #print("We have an expetion here: StaleElementReferenceException")
                    headquarters = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    #print(headquarters)
                
                try:
                    size = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[1]').text
                except NoSuchElementException:
                    #print("We have an expetion here: NoSuchElementException")
                    size = -1
                    #print(size)
                except StaleElementReferenceException:
                    #print("We have an expetion here: StaleElementReferenceException")
                    size = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[1]').text
                    #print(size)
                    
                try:
                    founded = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]').text
                except NoSuchElementException:
                    #print("We have an expetion here: NoSuchElementException")
                    founded = -1
                    #print(founded)
                except StaleElementReferenceException:
                    #print("We have an expetion here: StaleElementReferenceException")
                    founded = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]').text
                    #print(founded)
                    
                try:
                    type_of_ownership = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[2]').text                
                except NoSuchElementException:
                    #print("We have an expetion here: NoSuchElementException")
                    type_of_ownership = -1
                    #print(type_of_ownership)
                except StaleElementReferenceException:
                    #print("We have an expetion here: StaleElementReferenceException")
                    type_of_ownership = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[2]').text
                    #print(founded)
                    
                try:
                    industry = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[3]').text
                except NoSuchElementException:
                    #print("We have an expetion here: NoSuchElementException")
                    industry = -1
                    #print(industry)
                except StaleElementReferenceException:
                    #print("We have an expetion here: StaleElementReferenceException")
                    industry = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[3]').text
                    #print(industry)
 
                try:
                    sector = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[4]').text 
                except NoSuchElementException:
                    #print("We have an expetion here: NoSuchElementException")
                    sector = -1
                    #print(sector)
                except StaleElementReferenceException:
                    #print("We have an expetion here: StaleElementReferenceException")
                    sector = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[4]').text
                    #print(sector)
 
                try:
                    revenue = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[5]').text
                except NoSuchElementException:
                    #print("We have an expetion here: NoSuchElementException")
                    revenue = -1
                    #print(revenue)
                except StaleElementReferenceException:
                    #print("We have an expetion here: StaleElementReferenceException")
                    revenue = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[5]').text
                    #print(revenue)
           
            except NoSuchElementException:
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
            except StaleElementReferenceException:
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                
            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Headquarters" : headquarters,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            #add job to jobs
            })
                       
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[2]/div/div[1]/button[7]').click()

        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break
        
    currenturl = driver.current_url
    driver.implicitly_wait(1)
    print("THE CURRENT URL IS: ", currenturl)
    driver.implicitly_wait(1)
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.