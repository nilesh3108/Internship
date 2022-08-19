#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install selenium')


# In[11]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[12]:


driver=webdriver.Chrome(r"C:\Users\sony\Downloads\chromedriver.exe")


# In[18]:


driver=webdriver.Chrome(r"chromedriver.exe")


# In[78]:


#question 1
driver.get("https://www.naukri.com/")
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Analyst')
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div[1]/input")
location.send_keys('Bangalore')
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()
job_title=[]
job_location=[]
company_name=[]
experience_required=[]

title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,"//li[@class='fleft grey-text br2 placeHolderLi location']")    
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]//span') 
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)
    
    


# In[82]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))
df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name':company_name,'Exp_required':experience_required})
df


# In[88]:


#question 2
driver.get("https://www.naukri.com/")
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/div/div/div[5]/div/div/div[1]/input")
location.send_keys('Bangalore')
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()
job_title=[]
job_location=[]
company_name=[]

title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,"//li[@class='fleft grey-text br2 placeHolderLi location']")    
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    


# In[86]:


print(len(job_title),len(job_location),len(company_name))
df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name':company_name})
df


# In[113]:


#question 3
driver.get("https://www.naukri.com/")
designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')
search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()
job_title=[]
job_location=[]
company_name=[]
experience_required=[]

title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,"//li[@class='fleft grey-text br2 placeHolderLi location']")    
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]//span') 
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[115]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))
df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name':company_name,'Exp_required':experience_required})
df


# In[174]:


#question 4
driver.get("https://www.flipkart.com/")
brand=driver.find_element(By.CLASS_NAME,"_3704LK")
brand.send_keys('sunglasses')
search=driver.find_element(By.CLASS_NAME,"_34RNph")
search.click()
brand_name=[]
product_description=[]
product_price=[]


# In[175]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[0:100]:
    brand=i.text
    brand_name.append(brand)
    
product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
for i in product_tags[0:100]:
    product=i.text
    product_description.append(product)
    
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')    
for i in price_tags[0:100]:
    price=i.text
    product_price.append(price)


# In[176]:


print(len(brand_name),len(product_description),len(product_price))
df=pd.DataFrame({'brand_name':brand_name,'product_description':product_description,'product_price':product_price})
df


# In[177]:


#question 5
driver.get("https://www.flipkart.com/")


# In[216]:


product_rating=[]
review_summary=[]
full_review=[]


# In[227]:


rating_tags=driver.find_elements(By.XPATH,'//div[@class="_3LWZlK"]')
for i in rating_tags[0:100]:
    rating=i.text
    product_rating.append(rating)
    
summary_tags=driver.find_elements(By.XPATH,"//span[@class='_2_R_DZ']")    
for i in summary_tags[0:100]:
    summary=i.text
    review_summary.append(summary)
    
review_tags=driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]') 
for i in review_tags[0:100]:
    review=i.text
    full_review.append(review)
    


# In[229]:


print(len(product_rating),len(review_summary),len(full_review))


# In[230]:


df=pd.DataFrame({'product_rating':product_rating,'review_summary':review_summary})
df


# In[231]:


#question 6
driver.get("https://www.flipkart.com/")


# In[252]:


brand_name=[]
product_description=[]
selling_price=[]


# In[255]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[0:100]:
    brand=i.text
    brand_name.append(brand)
    
product_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa _2-ICcC"]')
for i in product_tags[0:100]:
    product=i.text
    product_description.append(product)
    
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')    
for i in price_tags[0:100]:
    price=i.text
    selling_price.append(price)


# In[256]:


print(len(brand_name),len(product_description),len(selling_price))


# In[257]:


df=pd.DataFrame({'brand_name':brand_name,'product_description':product_description,'selling_price':selling_price})
df


# In[375]:


#Question 7
driver.get("https://www.myntra.com/shoes")


# In[ ]:


shoe_brand=[]
shoe_description=[]
shoe_price=[]


# In[264]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_tags[0:100]:
    brand=i.text
    shoe_brand.append(brand)
    
shoe_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa _2-ICcC"]')
for i in shoe_tags[0:100]:
    shoe=i.text
    show_description.append(shoe)
    
price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')    
for i in price_tags[0:100]:
    price=i.text
    shoe_price.append(price)


# In[265]:


print(len(shoe_brand),len(shoe_description),len(shoe_price))


# In[266]:


#question 8
driver.get("https://www.amazon.in/")


# In[292]:


laptop_title=[]
laptop_rating=[]
laptop_price=[]


# In[293]:


title_tags=driver.find_elements(By.XPATH,'//span[@class="a-size-medium a-color-base a-text-normal"]')
for i in title_tags[0:10]:
    title=i.text
    laptop_title.append(title)
    
rating_tags=driver.find_elements(By.XPATH,' //span[@class="a-size-base s-underline-text"]')
for i in rating_tags[0:10]:
    rating=i.text
    laptop_rating.append(rating)
    
price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')    
for i in price_tags[0:10]:
    price=i.text
    laptop_price.append(price)


# In[294]:


print(len(laptop_title),len(laptop_rating),len(laptop_price))


# In[296]:


df=pd.DataFrame({'laptop_title':laptop_title,'laptop_rating':laptop_rating,'laptop_price':laptop_price})
df


# In[297]:


#question 9
driver.get("https://www.ambitionbox.com/")


# In[299]:


job_title=[]
job_location=[]
company_name=[]


# In[301]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title noclick"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,"//div[@class='entity loc']")    
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="company-info"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[304]:


print(len(job_title),len(job_location),len(company_name))
df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name':company_name})
df


# In[308]:


#question 10
driver.get("https://www.ambitionbox.com/")


# In[369]:


company_name=[]
experience_required=[]
average_salary=[]
minimum_salary=[]
maximum_salary=[]
total_salary=[]


# In[370]:


company_tags=driver.find_elements(By.XPATH,'//div[@class="company-info"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//div[@class="sbold-list-header"]') 
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)
    
average_tags=driver.find_elements(By.XPATH,'//p[@class="averageCtc"]')
for i in average_tags[0:10]:
    average=i.text
    average_salary.append(average)
    
maximum_tags=driver.find_elements(By.XPATH,'//div[@class="value body-medium"]') 
for i in maximum_tags[0:10]:
    maximum=i.text
    maximum_salary.append(maximum)
    
minimum_tags=driver.find_elements(By.XPATH,'//div[@class="salary-values"]') 
for i in minimum_tags[0:10]:
    minimum=i.text
    minimum_salary.append(minimum)
    
total_tags=driver.find_elements(By.XPATH,'//span[@class="datapoints"]')    
for i in total_tags[0:10]:
    total=i.text
    total_salary.append(total)


# In[371]:


print(len(company_name),len(experience_required),len(average_salary),len(maximum_salary),len(minimum_salary),len(total_salary))


# In[373]:


df=pd.DataFrame({'company_name':company_name,'experience_required':experience_required,'average_salary':average_salary,'maximum_salary':maximum_salary,'minimum_salary':minimum_salary,'total_salary':total_salary})
df


# In[ ]:




