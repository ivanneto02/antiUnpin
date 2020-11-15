import datetime
import pytz
import os

timezone = pytz.timezone("US/Pacific")
now = datetime.datetime.now(timezone)

months = {
	1 : "January",
	2 : "February",
	3 : "March",
	4 : "April",
	5 : "May",
	6 : "June",
	7 : "July",
	8 : "August",
	9 : "September",
	10 : "October",
	11 : "November",
	12 : "December"
}

curr_year = now.year
curr_month = months[now.month]
curr_day = now.day

def createLog(user_id, name, message):
	curr_date = f'{curr_year}-{now.month}-{curr_day}'
	curr_time = now.strftime("%H:%M:%S")

	try: 
		root_path = os.getcwd()
		rel_path = f"/logs/{curr_year}/{curr_month}"
		os.makedirs(root_path + rel_path)

	except FileExistsError:
		pass

	log_file = open(f'{root_path + rel_path}/{curr_day}.txt', 'a+')
	log_file.write(f'({curr_date}) - {curr_time} - USERID: {user_id} - NAME: {name} - MESSAGE: \"{message}\"\n')
	log_file.close()
