import requests, os, sys, time, random, json, datetime
from stationsCP import getStation
from bs4 import BeautifulSoup

url_bilhetes = "https://venda.cp.pt/bilheteira/comprar/pesquisar"
url_cp = "https://www.cp.pt/passageiros/pt/comprar-bilhetes"
url_bilhetes1 = "https://www.cp.pt/sites/passageiros/pt/consultar-horarios/horarios-resultado"

postData ={ "stationPartidaID" : "94-2006",
            "stationChegadaID" : "94-31039",
            "textBoxPartida"   : "Espinho",
            "textBoxChegada"   : "Aveiro",
            "textBoxDataIda"   : "2020-01-13",
            "textBoxDataVolta" : "",
            "departDate" 	   : "13 Janeiro, 2020",
            "returnDate"       : "",
            "radioButtonClasse": "2",
            "passengers"       : "1",
            "numTicket"        : "1",
            "language"		   : "pt",
            "sessionId"		   : "",
            "corporate"	       : "0"
            }

postData1={ "allServices" : "allServices",
            "depart" 	  : "Espinho",
            "arrival"     : "Aveiro",
            "Date"   	  : "14 Janeiro, 2020",
            "departDate"  : "2020-01-14",
            "turnDate" 	  : "",
			"returnDate"  : ""
            }

postData2={ "depart" 	     : "Espinho",
            "arrival"        : "Aveiro",
            "Date"   	     : "14 Janeiro, 2020",
            "departDate"     : "2020-01-14",
			"timeType"       : "1",
			"time"		     : "",
            "turnDate" 	     : "",
			"returnDate"     : "",
			"returnTimeType" : "1",
			"returnTime"     : ""
            }

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho' , 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

class args_class:
	depart          = None
	arrival         = None
	departDate      = None
	endDate         = None
	isAlfa          = False
	isIntercities   = False  # intercities
	isInternational = False # international
	isRegionals     = False  # regionals
	isUrbans        = False  # urbans


def getPrices(url_cp, url_to_post, send_data):
    # get sessionId from CP
    response = requests.get(url_cp).text
    soup = BeautifulSoup(response, 'lxml')
    candidates = soup.select('input')

    # Update sessionId value
    for x in candidates:
        if(str(x).find('sessionId') != -1):
            send_data['sessionId'] = str(x['value'])

    #request to CP
    response = requests.post(url_to_post, data=send_data)

    print(response)
    print(response.text)
    print(response.url)
    return None

def getPrices1(url_to_post, send_data):
	train_price = []
	train_info  = []
	#request to CP
	response = requests.post(url_to_post, data=send_data).text
	soup = BeautifulSoup(response, 'lxml')
	candidates = soup.select('td')

	waiting_train_price = False

	for x in candidates:
		# Cast Number of Results given by CP search engine
		if(str(x).find('IDA') != -1):
			total_nr_results = [int(s) for s in (x.text).split() if s.isdigit()]

		# Cast travel train description
		#### In case of receiving description without receiving last travel price, 
		#### add a price value of 99999 to the last travel option
		description = x.select('li')
		if(description):
			#init vars
			tmp_str = ''
			promo_val = [99999,99999]
			promo_first_class = 0
			promo_second_class = 0
			if(waiting_train_price == True):
				train_price.append(99999)
			for y in description[:-1]:
				if((y.text).find('Serviço') != -1):
					tmp_str += y.text + '\n'
				elif((y.text).find('Partida') != -1):
					tmp_str += y.text + '\n'
				elif((y.text).find('Chegada') != -1):
					tmp_str += y.text + '\n'
				elif((y.text).find('Duração') != -1):
					tmp_str += y.text + '\n'
				# get promotion prices
				elif((y.text).find('€') != -1):
					promo_str = (y.text).split('€')
					try:
						promo_first_class  = promo_str[1].split('/')
						promo_second_class = promo_str[2].split()
					except:
						promo_second_class = promo_first_class
						promo_first_class = ["99999"]
					try:
						promo_first_class = float((promo_first_class[0].split())[0].replace(',','.'))
						promo_second_class = float((promo_second_class[0].split())[0].replace(',','.'))
					except:
						pass
					promo_val[0] = promo_first_class
					promo_val[1] = promo_second_class
			train_info.append(tmp_str)
			waiting_train_price = True
		# Cast travel train price
		elif((str(x).find('€') != -1) and waiting_train_price):
			value = (x.text).split()
			value = str(value[0]).replace('€','')
			value = value.replace(',','.')
			value_per_class = value.split('/')
			# Since CP have 2 class's , 1º and 2º class, choose the cheapest one
			min_price = 99999
			for val in value_per_class:
				if(float(val) < min_price):
					min_price = float(val)
			# check promo prices
			try:
				for val in promo_val:
					if(val < min_price):
						min_price = val
			except:
				pass
			# Append price info
			train_price.append(min_price)
			waiting_train_price = False

	# If everything ok, print results |GOOD for debug| 
	#for i in range(0,total_nr_results[0]-1):
	#	print(train_info[i] + 'Preço: ' + str(train_price[i])) 
		
	return [train_info, train_price]

def getDate(year, month, day):
	res = ['-','-']
	res[1] = str(day) + ' ' + months[month-1] + ', ' + str(year)
	res[0] = str(year) + '-' + str(month).rjust(2,'0') + '-' + str(day).rjust(2,'0')
	return res

def print_helper():
	print('Usage: python3 ' + sys.argv[0] + ' -sS <startStation> -eS <endStation> \r')
	print('Options: ')
	print('-sD <startDate> (search only after <startDate> value inclusive |ex: -sD 2020-05-29|)')
	print('-eD <endDate>   (search only until <endDate> value inclusive   |ex: -eD 2020-05-30|)')
	print('-al (search for alfa trains)')
	print('-ic (search for intercities trains)')
	print('-in (search for international trains)')
	print('-re (search for regionals trains)')
	print('-ub (search for urbans trains)')
	print('Note: When only <startStation> <endStation> specifyed, <startDate> will be set as the current day, and <endDate> as the maximum allowed by CP (60 days).')
	print('      By default the program will search for all types of trains.')
	exit()

def get_args(_argv_):
	# initialize class
	args = args_class()
	# get args
	for x in range(0,len(_argv_)):
		# startStation
		if(  _argv_[x] == '-sS'):
			args.depart = _argv_[x+1]
		# endStation
		elif(_argv_[x] == '-eS'):
			args.arrival = _argv_[x+1]
		# startDate
		elif(_argv_[x] == '-sD'):
			# validate date 
			splited_date = (_argv_[x+1]).split('-')
			if(len(splited_date) != 3):
				print_helper()
			# everything ok :)
			args.departDate = _argv_[x+1]
		# endDate
		elif(_argv_[x] == '-eD'):
			# validate date 
			splited_date = (_argv_[x+1]).split('-')
			if(len(splited_date) != 3):
				print_helper()
			# everything ok :)
			args.endDate = _argv_[x+1]
		# alpha
		elif(_argv_[x] == '-al'):
			args.isAlfa = True
			postData2['alfa'] = 'true'
		# intercities
		elif(_argv_[x] == '-ic'):
			args.isIntercities = True
			postData2['intercities'] = 'true'
		# international
		elif(_argv_[x] == '-in'):
			args.isInternational = True
			postData2['international'] = 'true'
		# regionals
		elif(_argv_[x] == '-re'):
			args.isRegionals = True
			postData2['regionals'] = 'true'
		# urbans
		elif(_argv_[x] == '-ub'):
			args.isUrbans = True
			postData2['urbans'] = 'true'
		else:
			pass
	# return value
	return args

def main():
	# get args
	args = get_args(sys.argv)

	if((args.depart == None) or (args.arrival == None)):
		print_helper()

	# If no restrictions added - search for all
	if(args.isAlfa == False and args.isIntercities == False and args.isInternational == False and args.isRegionals == False and args.isUrbans == False):
		searchTemplate = postData1
	else:
		searchTemplate = postData2

	startStation = getStation(args.depart)
	endStation   = getStation(args.arrival)

	# try start station 
	if((startStation[0] == '-') or (startStation[1] == '-')):
		print("Invalid startStation!!!")
		exit()

	# fill depart station
	searchTemplate['depart'] = startStation[0]

	# try end station
	if((endStation[0] == '-') or (endStation[1] == '-')):
		print("Invalid endStation!!!")
		exit()

	# fill end station
	searchTemplate['arrival'] = endStation[0]

	if(args.departDate == None):
		date_time_obj = datetime.datetime.now().strftime("%Y-%m-%d").split('-')
	else:
		date_time_obj = (args.departDate).split('-')

	if(args.endDate != None):
		endDate_time_obj = (args.endDate).split('-')
		deltaTime = datetime.date(int(endDate_time_obj[0]),int(endDate_time_obj[1]),int(endDate_time_obj[2]))-datetime.date(int(date_time_obj[0]),int(date_time_obj[1]),int(date_time_obj[2]))
		deltaTime = deltaTime.days
	else:
		# max allowed by CP
		deltaTime = 59

	# Start the searching ...
	lowest_price = []
	travel_info  = []
	travel_day   = []
	
	for incDay in range(0,deltaTime):
		searchDate = datetime.date(int(date_time_obj[0]),int(date_time_obj[1]),int(date_time_obj[2])) + datetime.timedelta(days=incDay)
		coded_date = getDate(searchDate.year,searchDate.month,searchDate.day)

		searchTemplate['Date'] = coded_date[1]
		searchTemplate['departDate'] = coded_date[0]
		
		[train_info, train_price] = getPrices1(url_bilhetes1 , searchTemplate)

		# get cheapest travel options if avaible
		try:
			l_p = min(train_price)
		except:
			continue
		

		# get all occurrences
		for i in range(0,len(train_price)-1):
			# if train_price on index i is equal to lowest price
			if(train_price[i] == l_p):
				lowest_price.append(l_p)
				travel_info.append(train_info[i])
				travel_day.append(searchDate.strftime("%Y-%m-%d"))
	
	# final display all the results
	l_p = min(lowest_price)
	for i in range(0,len(lowest_price)-1):
		# if lowest_price on index i is equal to lowest price
		if(lowest_price[i] == l_p):
			print('\nDia: ' + travel_day[i] + '\n' + travel_info[i] + 'Preço: ' + str(l_p) + '\n') 
	
if __name__ == '__main__':
    main()
