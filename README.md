# Picture Roulette MMS

<a href="https://heroku.com/deploy?template=https://github.com/makaimc/mms-picture-roulette/"><img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy on Heroku"></a>

Picture Roulette is a drinking game that uses the Twilio and Flickr APIs. 
Flickr's tags are only as accurate as the humans who use apply them to photos. 
This program was originally designed to query a tag for a relevant picture. 
What we didn't expect is that Flickr users' use of tags would be so diverse 
and often nonsensical. Hence, the MMS Picture Roulette drinking game was born!

## How to play

Text a one-word query to your Twilio number from any texting device. Wait 30 seconds, and receive your photo. Does the photo match your query? Other players drink. Is the photo totally random? You drink. 

### Requirements

* Twilio API credentials
* Flickr API credentials 
* Heroku Account - free tier

### Setup

* Click "Deploy to Heroku" button
* Input your Twilio API credentials in the boxes provided 
* Launch the app. If it works, it should look like the photo below:

<img src="http://otakujournalist.com/wp-content/uploads/2014/09/itworked.png" />

* Now, copy the Heroku app URL and go to your Twilio account
* On the Numbers page, click on the Twilio number you want to use. Make the URL the Messaging Request URL and save. Start texting. 

<img src="http://otakujournalist.com/wp-content/uploads/2014/09/request_url.png" />


