from datetime import date,timedelta
class BirthdayRemainder:
    def __init__(self):
        self.birthday_dates=[]
        
    def collect_birthday_data(self):
        print(f"BirthdayRemainder...!")
        print(f"Fill out the for the upcoming 7 days!...")
        try:
            getting_no=int(input("Enter how many birthdays are in the upcoming 7 days.."))
            
            for i in range(1,getting_no+1,1):
                self.getting_day=int(input(f"Enter bithday day(DD):"))
                self.getting_month=int(input(f"Enter bithday month(MM:"))
                self.getting_year=int(input(f"Enter bithday year(YYYY):"))
                self.getting_name=input(f"Enter name of the Birthday Guy!...:")
                self.dt=date(self.getting_year,self.getting_month,self.getting_day)
                self.dt_list=[ self.dt,  self.getting_name]
                self.birthday_dates.append(self.dt_list)
        except (TypeError,ValueError):
            print("Enter  a valid input!")
            exit()
    
    def find_upcoming_birthday(self):
        current_date=date.today()
        upcoming_event=None
        if  current_date> self.dt:
            print("Too late This person's birthday already finished")
        else:
            for attemp in range(1,8):
                up_coming=current_date+timedelta(days=attemp)
                            
                for birthday in  self.birthday_dates:
                    if up_coming in birthday:
                            if birthday<self.birthday_dates[0]:
                                upcoming_event=birthday
        if  upcoming_event is not None:
            print(f"upcoming birthday event!.. {upcoming_event[0]} {upcoming_event[1]} birthday... Dont forget to wish!..")
        else:
            print("No remanider... in this week")
                        
obj=BirthdayRemainder()
obj.collect_birthday_data()
obj.find_upcoming_birthday()
getting_choice=input("Do you want to continue on this birthday remainder..![yes\no]")
if getting_choice.casefold()=="yes":
    obj=BirthdayRemainder()
    obj.collect_birthday_data()
    obj.find_upcoming_birthday()
elif getting_choice.casefold()=="no":
    print("birthday remainder is going to exit....!")
    exit()
else:
    print("Enter a  valid input")
    exit()
            
