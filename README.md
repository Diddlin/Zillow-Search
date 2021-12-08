# Zillow-Search

This Application is intended to utilized new postings on zillow with specific search criteria via their API and then Text a message to a target phone number via Twilio.


Intention - Developed for personal use but could be applied to notify a target userbase of individuals (such as a broker notifying their clients of a new posting based off their search criteria) in an automated way.

Python script scrapes Zillow (ZillowScrape.py) with input of Zipcode as the initial search criteria and builds a current state list of houses on market in that area "BigList" this is the baseline of the search. Every time the script runs it will search for new houses not on this list as the target to be a newly posted house and this will be moved forward as the result to push via Twilio in the form of a link to the posting. 

Once this house has been sent it will be added to the master file "Biglist" and not be sent again, updating the baseline.

Twilio is taking the result of this output and simply sending it to a target phone number.


This is all being hosted and ran via Herkoku currently 3 times a day (every 8 hours) thru Cronjob.py
