import pandas as pd
import os

from_date = "2018-09-01"
to_date = "2018-09-07"
event_name_Purchase = "af_purchase"
app_id = ""
token = ""

print("Loading CSV...")

path = os.getcwd()

def getPurchaseWithin7Days():

	inappData = pd.read_csv(path+"/PurchaseWithin7Days.csv")

	print("CSV Loading Complete...")

	inappData["install_datetime"] = pd.to_datetime(inappData["Install Time"])
	inappData["event_datetime"] = pd.to_datetime(inappData["Event Time"])

	# inappData["install_datetime_totalseconds"] =   inappData["install_datetime"].dt.total_seconds()
	# inappData["event_datetime_totalseconds"] = inappData["event_datetime"].dt.total_seconds()

	inappData["install_datetime_totalseconds"] = pd.to_datetime(inappData['install_datetime'], unit='s')
	inappData["event_datetime_totalseconds"] = pd.to_datetime(inappData['event_datetime'], unit='s')


	print("Starting Organization....")

	print("Only Get Your Wanted Event....")
	inappData.rename(columns={'Event Name': 'event_name'}, inplace=True)

	print("Find Event Within 7 Days....")
	inappData['install_to_event_time_inseconds'] = inappData['event_datetime'] - inappData['install_datetime']
	inappData['install_to_event_time_inseconds'] = inappData['install_to_event_time_inseconds'].astype(str)
	inappData['days_during_test'] = inappData['install_to_event_time_inseconds'].str.extract('(\d+)').astype(int)


	inappData = inappData.drop(inappData[inappData.days_during_test > 6].index)

	#Remove Non Events
	inappData = inappData[inappData.event_name == event_name_Purchase]

	inappData = inappData.drop_duplicates(subset='AppsFlyer ID', keep="first")

	print("Sort by Media source....")
	finalTable = inappData.sort_values(by=['Media Source'])

	print("Printing CSV...")

	

	finalTable.to_csv(path+"/PurchaseWithin7Days.csv")

getPurchaseWithin7Days()
