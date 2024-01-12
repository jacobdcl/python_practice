from datetime import datetime
import time

# set today's date to a variable
todays_date = datetime.today()
mm_dd_yy = todays_date
# organize each form/piece of info
date_info = {'month_name':todays_date.strftime('%B'), 'month_abrv':todays_date.strftime('%b'), 'mm':todays_date.strftime('%m'), 'dd':todays_date.strftime('%d'), 'yy':todays_date.strftime('%y'), 'yyyy':todays_date.strftime('%Y'), '24hr':todays_date.strftime('%H'), 'hr':todays_date.strftime('%I'), 'hr_ampm':(todays_date.strftime('%I')+todays_date.strftime('%p')), 'min':todays_date.strftime('%M'), 'sec':todays_date.strftime('%S'), 'week_num':todays_date.strftime('%U'), 'weekday':todays_date.strftime('%A'), 'weekday_abrv':todays_date.strftime('%a'), 'weekday_num':todays_date.strftime('%w')}
# print each iteration of date_info dictionary
for info in date_info:
    print(info,date_info[info])
    
# month_name dd, yyyy
month_dd_yyyy = todays_date.strftime("%B %d, %Y")
# mm/dd/yy
mm_dd_yy = todays_date.strftime("%m/%d/%y")
# abbreviated_month-dd-yyyy	
abrv_dd_yyyy = todays_date.strftime("%b-%d-%Y")
# hour
current_time = todays_date.strftime('%h')

