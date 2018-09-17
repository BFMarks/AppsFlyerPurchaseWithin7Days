# AppsFlyerPurchaseWithin7Days

This script is designed obtain all first-time purchases within 7 days of installs by using [AppsFlyer's Pull API](https://support.appsflyer.com/hc/en-us/articles/207034346-Pull-APIs-Pulling-AppsFlyer-Reports-by-APIs)

To use the script open a terminal in the folder with python code and:

1) Add the python [pandas libary](https://pandas.pydata.org/) via pip

```python
pip install pandas
```

2) Change the date range, add your event name, add your app_id and token:

```python
from_date = "2018-09-01"
to_date = "2018-09-07"
event_name_Purchase = "af_purchase"
app_id = "YOUR_APP_ID"
token = "YOUR_TOKEN"
```

3) Lastly, start the script by typing this command in the terminal:

```python
python GetPurchaseInFirst7Days.py
```

You folder directory will now have every first time purchase within 7 days.


Cheers,



