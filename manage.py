from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import sys
import pandas as pd
import re

class scripy:
    def dotsquare(self,urls):
        titles=[]
        descriptions=[]

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")
        data = soup.find('div', class_='hot-vacancy').find_all('a')
        apply_link="https://careers.dotsquares.com/apply/"
        
        for a in data:
           
            links = a.get('href')

            html_content = requests.get(links).text 
            soup = BeautifulSoup(html_content,"html.parser")
            title = soup.find('div', id='job-description').find('h2').text
            description = soup.find('div', class_='job-description-left').text
            titles.append(title)
            descriptions.append(description)
            # apply_link.append(apply_link)
            dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions,
                    'APPLYLINK':apply_link,
                    'FETCHTIME':current_time,
                }
            df = pd.DataFrame(dataset)
            df.to_csv('dotsquare.csv', index=False, encoding='utf-8')    

    def a3Logics(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        descriptions=[]
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")
        data = soup.find('section', class_='career-opt').find_all('a')
        for a in data:
           
            links = a.get('href')

            html_content = requests.get(links).text 
            soup = BeautifulSoup(html_content,"html.parser")
            title = soup.find('section', class_='career-inner-content').find('h1').text
            description = soup.find('div', class_='career-info').text
            titles.append(title)
            descriptions.append(description)
            dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions,
                    'APPLYLINK': links,
                    'FETCHTIME':current_time,
                }
            df = pd.DataFrame(dataset)
            df.to_csv('a3Logics.csv', index=False, encoding='utf-8')   
            

    def anvaclouds(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        descriptions=[]
        apply_link= "https://www.anavcloudsoftwares.com/apply-at-anavcloud/"
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")

        title1 = soup.find_all('div',class_="position_Description")
        for title in title1:
            h3 = title.find('h3')
            print(h3.text)
            p_tags = title.find('p')  
            print(p_tags.text)
            
            for h3 in h3:
                titles.append(h3.text)  
            
            for p in p_tags:  
                descriptions.append(p_tags.text)  
       
        print(f"Titles Length: {len(titles)}")
        print(f"Descriptions Length: {len(descriptions)}")

        dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions,
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('anvaclouds.csv', index=False, encoding='utf-8')   

    def archiveinfotech(self, urls):
            titles = []
            descriptions = []

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            html_content = requests.get(urls).text
            soup = BeautifulSoup(html_content, "html.parser")

            # Find all titles
            title_elements = soup.find_all('h2', class_='vc_custom_heading')
            for h2 in title_elements:
                title_text = h2.text.strip()  # Clean up the text
                titles.append(title_text)  # Append title to the list
                print(h2)

            # Find all descriptions
            description_elements = soup.find_all('div', class_='wpb_raw_code')
            for div in description_elements:
                description_text = div.text.strip()  # Clean up the text
                descriptions.append(description_text)  # Append description to the list
                print(div)

            # Print lengths after both loops
            print(f"Titles Length: {len(titles)}")
            print(f"Descriptions Length: {len(descriptions)}")

            # # Use min length to ensure matching pairs
    

            min_length = min(len(titles), len(descriptions))

            dataset = {
                'TITLE': titles[:min_length],
                'DESCRIPTION': descriptions[:min_length],
                'FETCHTIME': [current_time] * min_length,
            }
            df = pd.DataFrame(dataset)

            # # Save to CSV
            df.to_csv('archiveinfotech.csv', index=False, encoding='utf-8')
  
    def brixcode(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        descriptions=[]
        apply_link= "https://brixcodetechnologies.com/apply_form"
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")



        title = soup.find('section', class_="about-offer")
        h5=title.find_all('h5')
        p=title.find_all('p')
        for h5 in h5:
            titles.append(h5.text)
        for p in p:
            descriptions.append(p.text)

        dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions,
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('brixcode.csv', index=False, encoding='utf-8')   

    def ijsinfotech(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        descriptions=[]
        apply_link= "https://ijsinfotech.com/career/#rs_apply"
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")

        title = soup.find_all('h3', class_="title")
        description = soup.find_all('p', class_="number-txt")
        for t in title[2:]:
            titles.append(t.text)
        
        #  print(t.text)
        for p in description[2:]:
            # print(p.text)
            descriptions.append(p.text)
        print(f"Titles Length: {len(titles)}")
        print(f"Descriptions Length: {len(descriptions)}")


        dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions,
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('ijsinfotech.csv', index=False, encoding='utf-8')   

    def iskylar(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        apply_link= "https://iskylar.com/hiring/"
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")

        data = soup.find_all('h1', class_="elementor-heading-title")
        for a in data:
            a=a.find('a')
            links = a.get('href')

            html_content = requests.get(links).text 
            soup = BeautifulSoup(html_content,"html.parser")


            title = soup.find('h1', class_='elementor-heading-title').text
            titles.append(title)
            
            # print(f"Titles Length: {len(titles)}")
            # print(f"Descriptions Length: {len(descriptions)}")
            dataset = {
                    'TITLE' : titles,
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('iskylar.csv', index=False, encoding='utf-8') 

    def KadamTech(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        descriptions=[]
        apply_link= "https://www.kadamtech.com/career/"
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")  
        title = soup.find_all('p', class_="job-opening")
        for p in title:
            titles.append(p.text)
        description = soup.find_all('div', class_="well")
        for p in description:
            descriptions.append(p.text)
        dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions,
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('LadamTech.csv', index=False, encoding='utf-8') 
    
    def Digitalwhoper(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        descriptions=[]
        apply_link= "https://www.digitalwhopper.com/apply"
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")  

        title = soup.find('div', class_="position").find_all('h3')
        for title in title:
            titles.append(title.text)
         
        dataset = {
                    'TITLE' : titles,
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('Digitalwhoper.csv', index=False, encoding='utf-8') 

    def kpis(self,urls):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        titles=[]
        descriptions=[]
        d=[]
        des=[]
        apply_link= "https://www.kpis.in/career"
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content,"html.parser")  
        title = soup.find_all('h5', class_="h5")
        for title in title[:9]:
            titles.append(title.text)
            print(title.text)

        description=soup.find_all('p', class_="fs-6")

        for i in range(0,18,2):  # Step by 2

            if i < len(description):
                pair = description[i].text
                if i + 1 < len(description):  # Check if the next index is valid
                    pair += ' ' + description[i + 1].text  # Concatenate the two texts
                    descriptions.append(pair)
        dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions[:len(titles)],
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('Kpis.csv', index=False, encoding='utf-8') 

    # def new(self,urls):
    #     phone_number_matches=[]
    #     html_content = requests.get(urls).text 
    #     soup = BeautifulSoup(html_content,"html.parser")
    #     data=soup.get_text(separator=' ', strip=True)
        
    #     email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
    #     phone_number_pattern = re.compile('\+?1?[-. ]?(\(?\d{3}\)?)?[-. ]?(\d{3})[-. ]?(\d{4})([ -.]?(\d{1,4}))?')
    #     email_matches = re.findall(email_pattern,data)
    #     phone_number=re.findall(phone_number_pattern,data)

    #     print(email_matches)
    #     print(phone_number)
    def new(self, urls):
        phone_number_matches = []
        html_content = requests.get(urls).text 
        soup = BeautifulSoup(html_content, "html.parser")
        data = soup.get_text(separator=' ', strip=True)
        
        # email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
        # phone_number_pattern = re.compile(r'\+?1?[-. ]?(\(?\d{3}\)?)?[-. ]?(\d{3})[-. ]?(\d{4})([ -.]?(\d{1,4}))?|(\d{3})[-. ]?(\d{3})[-. ]?(\d{4})|(\d{10,15})')
        # email_matches = re.findall(email_pattern, data)
        # phone_number_matches = re.findall(phone_number_pattern, data)
        # print(email_matches)
        
        # # Print phone numbers without spaces
        # for match in phone_number_matches:
        #     print(''.join(filter(str.isdigit, match)))

        # pattern = r'(?:https?://)?(?:www\.)?([^/]+)'
        # match = re.search(pattern, urls)
        # if match:
        #     # Split the domain by '.' and take the first part as the company name
        #     domain = match.group(1)
        #     company_name = domain.split('.')[0]  # Take the first segment
        #     print(company_name)
        

        # location = soup.find('footer').find_all('p')
        # text=location.text
        # for p in location:
        #     print(location)
        location = soup.find('footer').find_all('p')
        for p in location:
            print(p.get_text(strip=True))  
        # print(location.text)         
        
        # Print the text of each paragraph
        # for p in location:
        #     print(p.get_text(strip=True))  



       
    
    
            



           
p1=scripy()
url1="https://careers.dotsquares.com/"
# url2="https://www.a3logics.com/careers/"
# url3="https://www.anavcloudsoftwares.com/careers/"  

# url5="https://archiveinfotech.com/careers/"
# url6="https://brixcodetechnologies.com/career"
# url7="https://ijsinfotech.com/career/"
url8="https://iskylar.com/career/"    
# url9="https://www.kadamtech.com/career/"  
# url10="https://www.digitalwhopper.com/career"  
# url11="https://www.kpis.in/career"
# # p1.dotsquare(url1)
# p1.a3Logics(url2)
# p1.anvaclouds(url3)
# p1.archiveinfotech(url5)
# p1.brixcode(url6)
# # p1.ijsinfotech(url7)
# p1.iskylar(url8)
# p1.KadamTech(url9)
# p1.Digitalwhoper(url10)
# p1.kpis(url11)

url12="https://deorwine.com/"
url13="https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TDI3MDTNLUsxYLRSNagwtjRLSba0TDMwSgMDK4MKc0MD46SU1BTT1MRUMwvTNC-BgqLEkozEXIXi_LSS8sSiVADw_RZr&q=pratham+software&oq=pratham&gs_lcrp=EgZjaHJvbWUqDQgBEC4YrwEYxwEYgAQyBggAEEUYOzINCAEQLhivARjHARiABDIQCAIQLhjHARixAxjRAxiABDIMCAMQABhDGIAEGIoFMgYIBBBFGEAyDAgFEAAYQxiABBiKBTIHCAYQABiABDIHCAcQABiABNIBCDMzMTlqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8"

p1.new(url1)






