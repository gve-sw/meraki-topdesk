# Meraki and TopDesk Cloud Integration
This is the Meraki TopDesk Cloud Integration source code. Using Meraki Webhooks and Flask, we have developed a connector to initiate incident requests in TopDesk Cloud.

![alt text](img/highlevel.png)

## Contacts:

* Josh Ingeniero (jingenie@cisco.com)
* Monica Acosta (moacosta@cisco.com)

## Solution Components
* Python
* Flask
* Meraki Dashboard API
* Meraki MR Access Points

## Installation:

#### Clone the repo
```
$ git clone https://wwwin-github.cisco.com/gve/meraki-topdesk.git
```

#### Install dependencies
```
$ pip3 install -r requirements.txt
```

## Setup:
#### Meraki details :
You can deploy this prototype in a lab environment or on your own Meraki dashboard online [here](https://account.meraki.com/secure/login/dashboard_login).
You need to have a TopDesk App Password and your TopDesk Deployment URL (replace localhost). You may check [here](https://developers.topdesk.com/tutorial.html#show-collapse-usage-createAppPassword) for more info. 
Fill in the details of your Meraki deployment and TopDesk Cloud in the [DETAILS.py](DETAILS.py) file
```python
MERAKI_API_KEY = 'Your API Key'
MERAKI_ORGANIZATION_ID = 'Your Organization ID'

TOPDESK_USERNAME = 'Your Username'
TOPDESK_PASSWORD = 'Your App Password'
TOPDESK_URL = 'http://localhost/tas/api/incidents'

```

## Usage:

Launch the Alert Handler Server. Make sure that you have your venv activated.
```
$ flask run --host=0.0.0.0 --port=5000
```

You must now expose your Server through an https connection. You may use [ngrok](https://ngrok.com/) for this.
```
$ ngrok http 5000
```

You may also use AWS Lambda and Zappa to host the server. You may refer to [zappa_settings](zappa_settings.json)
for a sample config.

Setup your Meraki Dashboard settings using this [guide](https://developer.cisco.com/meraki/webhooks/#!introduction/overview)
and use the https endpoint provided by ngrok. TopDesk should now be creating incidents for every alert webhook received.

You may customise the message provided by changing [TopDeskHelper.py](./TopDeskHelper.py).

####Uplink Loss and Latency
You may access the Uplink Loss and Latency Monitoring at IP/stats (for example: http://127.0.0.1:5000/stats)


#### Sample Alert
![alt text](img/sample.png)


## License
Provided under Cisco Sample Code License, for details see [LICENSE](./LICENSE.txt)

## Code of Conduct
Our code of conduct is available [here](./CODE_OF_CONDUCT.md)

## Contributing
See our contributing guidelines [here](./CONTRIBUTING.md)