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
            p_tags = title.find('p')  
            
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

            title_elements = soup.find_all('h2', class_='vc_custom_heading')
            for h2 in title_elements:
                title_text = h2.text.strip()  
                titles.append(title_text)  

            description_elements = soup.find_all('div', class_='wpb_raw_code')
            for div in description_elements:
                description_text = div.text.strip()  
                descriptions.append(description_text)  

            print(f"Titles Length: {len(titles)}")
            print(f"Descriptions Length: {len(descriptions)}")

            min_length = min(len(titles), len(descriptions))
            dataset = {
                'TITLE': titles[:min_length],
                'DESCRIPTION': descriptions[:min_length],
                'FETCHTIME': [current_time] * min_length,
            }
            df = pd.DataFrame(dataset)
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
        
        for p in description[2:]:
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

        for i in range(0,18,2):  

            if i < len(description):
                pair = description[i].text
                if i + 1 < len(description):  
                    pair += ' ' + description[i + 1].text  
                    descriptions.append(pair)
        dataset = {
                    'TITLE' : titles,
                    'DESCRIPTION' : descriptions[:len(titles)],
                    'APPLYLINK': apply_link,
                    'FETCHTIME':current_time,
                }
        df = pd.DataFrame(dataset)
        df.to_csv('Kpis.csv', index=False, encoding='utf-8') 



    def new(self, url,urls):
        name, email, address, titles, social_links, description, logo, phone =[], [], [], [], [], [], [], []

        html_content1 = requests.get(urls).text 
        soup1 = BeautifulSoup(html_content1,"html.parser")

        div = soup1.find_all('span',class_="BNeawe")
        address_text = ''
        for i in div:
            address_text += i.text + ' '  
            
        address_pattern = re.compile(r'Address\s*(.+?)\s*Hours', re.DOTALL)
        match = address_pattern.search(address_text)
        if match:
            address1 = match.group(1).strip()
            print(address1)


        # Fetch main page content
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Referer': url,
        }

        html_content = requests.get(url, headers=headers).text 
        soup = BeautifulSoup(html_content, "html.parser")
        data1 = soup.get_text(separator=' ', strip=True)

        pattern = r'(?:https?://)?(?:www\.)?([^/]+)'
        match = re.search(pattern, url)
        if match:
            domain = match.group(1)
            company_name = domain.split('.')[0]
            print(company_name) 

        email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
        email_matches = re.findall(email_pattern, data1)
        email = list(dict.fromkeys(email_matches))

        phone_number_pattern = re.compile(r""" 
                                          \b\d{10}\b|\b(?:\+91|091)?\s?\d{10}\b|\b0\d{2}[-.]?\d{8}\b|\b0\d{2}[-.]?\d{3}[-.]?\d{4}\b""", re.VERBOSE)
        phone_number_matches = phone_number_pattern.findall(data1)
        phone_numbers = list(dict.fromkeys(phone_number_matches)) 
        phone_numbers = [''.join(filter(str.isdigit, num)) for num in phone_numbers]
        for phone_number in phone_numbers:
            print("Phone Number:", phone_number)
            phone.append(phone_number)


        a=soup.title
        if a:
            title=a.string
            print(title)
        else:
            title=None
        
        
        description_tag = soup.find('meta', attrs={'name': 'description'})
        if description_tag:
            description_content = description_tag.get('content', '')
            print(description_content)
        else:
            description_content=None
          
        
        # facebook_links = [link['href'] for link in links if re.search(r'facebook\.com', link['href'])]
        # twitter_links= [link['href'] for link in links if re.search(r'twitter\.com',link['href'])]
        # instagram_links= [link['href'] for link in links if re.search(r'instagram\.com',link['href'])
        # youtube_links= [link['href'] for link in links if re.search(r'youtube\.com',link['href'])] 
        # social_links = [facebook_links, twitter_links, instagram_links, linkedin_links, youtube_links]
        # social_links=list(dict.fromkeys(linkedin_links))

        # links = soup.find_all('a', href=True)
        # linkedin_links= set(link['href'] for link in links if re.search(r'linkedin\.com',link['href']))
        # linkedin_link = next(iter(linkedin_links), None)
        # social_links.append(linkedin_links)
        # print(social_links)



        links = soup.find_all('a', href=True)

        facebook_links = [link['href'] for link in links if re.search(r'facebook\.com', link['href'])]
        twitter_links = [link['href'] for link in links if re.search(r'twitter\.com', link['href'])]
        instagram_links = [link['href'] for link in links if re.search(r'instagram\.com', link['href'])]
        youtube_links = [link['href'] for link in links if re.search(r'youtube\.com', link['href'])]
        linkedin_links = [link['href'] for link in links if re.search(r'linkedin\.com', link['href'])]

        # Combine all links into a structured dictionary
        social_links.append(['Facebook', list(dict.fromkeys(facebook_links)) if facebook_links else None])
        social_links.append(['Twitter', list(dict.fromkeys(twitter_links)) if twitter_links else None])
        social_links.append(['Instagram', list(dict.fromkeys(instagram_links)) if instagram_links else None])
        social_links.append(['LinkedIn', list(dict.fromkeys(linkedin_links)) if linkedin_links else None])
        social_links.append(['YouTube', list(dict.fromkeys(youtube_links)) if youtube_links else None])


        # Print the social links
        print(social_links)
                    

        logos = soup.find_all('img')
        pattern = re.compile(r'[/\-]logo', re.IGNORECASE)
        match = next((img for img in logos if pattern.search(img.get('src', ''))), None)
        if match:
            logo_link = match.get('src')
            print("Logo link:", logo_link)
            if logo_link:
                logo.append(logo_link)


        name.append(company_name)
        email.append(email)
        address.append(address1)





        print("Lengths of lists:")
        print("Name:", len(name))
        print("Email:", len(email))
        print("Address:", len(address))
        print("Titles:", len(titles))
        print("Description:", len(description))
        print("Social_links:", len(social_links))
        print("LOGO:", len(logo))
        print("Phone:", len(phone))
            
        min_length = min(len(name),len(email),len(address),len(titles),len(description),len(social_links),len(logo),len(phone))
        
        dataset = {
        'Company_name': name[:min_length],
        'Email': email[:min_length],
        'Phone': phone[:min_length] or [''] * min_length,  # Fill with empty strings if empty
        'Address': address[:min_length],
        'Title': titles[:min_length] or [''] * min_length,  # Fill with empty strings if empty
        'Description': description[:min_length] or [''] * min_length,  # Fill with empty strings if empty
        'Social_links': social_links[:min_length],
        'LOGO': logo[:min_length]
    }

        try:
            df = pd.DataFrame(dataset)
            df.to_csv('Data5.csv', index=False, encoding='utf-8')
            print("Data successfully saved to Data5.csv.")
        except Exception as e:
            print("error:")

           
p1=scripy()
url1="https://www.zonettech.com"
# url2="https://www.google.com/search?q=zordial&sca_esv=97958ac28674b0c2&ei=Wb4HZ9HVNtGNnesPpO_YiQs&gs_ssp=eJzj4tVP1zc0zEgpsrCoskw3YLRSNagwtjRLSbY0SjG1MDdKMrUwtDKoSDZINbSwNE01TEpLNEu0NPdir8ovSslMzAEAKRUSCg&oq=zordial&gs_lp=Egxnd3Mtd2l6LXNlcnAiB3pvcmRpYWwqAggAMhEQLhiABBiRAhjHARiKBRivATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyAhAmMgIQJjIIEAAYgAQYogQyCBAAGIAEGKIEMggQABiABBiiBDIgEC4YgAQYkQIYxwEYigUYrwEYlwUY3AQY3gQY4ATYAQJIgR9QmAtYmAtwAXgBkAEAmAHoAaAB6AGqAQMyLTG4AQHIAQD4AQH4AQKYAgOgAvcWqAIUwgIjEC4YgAQYtAIY5QIYxwEYtwMYigUY6gIYigMYjgUYrwHYAQHCAh0QABiABBi0AhjUAxjlAhi3AxiKBRjqAhiKA9gBAcICFhAAGAMYtAIY5QIY6gIYjAMYjwHYAQLCAhYQLhgDGLQCGOUCGOoCGIwDGI8B2AECmAOdAboGBAgBGAe6BgYIAhABGAqSBwswLjEuMC4xLjgtMaAHtQk&sclient=gws-wiz-serpp1.new(url1,url2)"
url2="https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TC42LDZIryo2YLRSNagwtjRLSU40TEtJSjQwSzI1tjKosEhONEi2TEs0TTIzNDBPNPASqMrPS1UoSU3OUCguTlbISgUAA28Vxg&q=zone+tech+ssc+je&oq=zonettech&gs_lcrp=EgZjaHJvbWUqDwgFEC4YDRivARjHARiABDIGCAAQRRg5MgkIARAAGA0YgAQyCQgCEAAYDRiABDIJCAMQABgNGIAEMgkIBBAAGA0YgAQyDwgFEC4YDRivARjHARiABDIJCAYQABgNGIAEMgkIBxAAGA0YgATSAQg0OTkwajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8"
p1.new(url1,url2)






