import requests,json

msg ={"frames":[{"text":"dont try this at home","icon":"61"},{"goalData":{"start":0,"current":1500,"end":2000,"unit":"£"},"icon":"34"},{"index":2,"chartData":[10,20,30,40,50,60,70]}]}
#msg ={
#    "frames": [
#		{
#		"text": "more_tests",
#		"icon": "61"
#		},
#		{
#           	"goalData":
#			{
#               	"start": 0,
#              	"current": 1500,
#                	"end": 2000,
#                	"unit": "£"
#            		},
#            	"icon": "34"
#		},
#		{
#	        "index": 2,
#           	"chartData": [10,20,30,40,50,60,70]
#		}
#	      ]
#	}

j = json.dumps(msg,indent=4)
u ='https://json.extendsclass.com/bin/1754378fb961'
h = {
	'Content-Type':'application/json',
	'Security-key': "P@ntherx1"
	}
r = requests.put(url = u, data=json.dumps(msg), headers= h)

print('r:',r)
print('r.reason:',r.reason)
print('r.status_code:',r.status_code)
print('r.headers:',r.headers)
print(j)