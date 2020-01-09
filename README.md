# model-3-delivery-predictor
Predicting Model 3 delivery times, based on dataset from TMC forums


### helper scripts

#### get_doq 
Get number of days into fiscal quarter a given date is

```
[user@localhost:scripts]# python3 get_doq.py
usage: get_doq.py [-h] -d DATE [-f FORMAT]
get_doq.py: error: the following arguments are required: -d/--date
[user@localhost:scripts]# python3 get_doq.py -d '2020-01-03'
2
[user@localhost:scripts]# python3 get_doq.py -d '3 Jan 2020' -f '%d %b %Y'
2
[user@localhost:scripts]#
```

#### factory_dist
Get the distance in miles between city, state and the Tesla factory in Fremont, CA

```
[user@localhost:scripts]# python3 factory_dist.py
usage: factory_dist.py [-h] -s STATE -c CITY
factory_dist.py: error: the following arguments are required: -s/--state, -c/--city
[user@localhost:scripts]# python3 factory_dist.py -s ne -c omaha
1407
[user@localhost:scripts]#
```
