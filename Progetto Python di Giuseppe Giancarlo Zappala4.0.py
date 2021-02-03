import requests
import json
import itertools






Counter=0
bestvolume=[]
Best=[]
Worst=[]
pricenowsum=0
profitloss=0
Best10=[]
Worst10=[]
Current_price=0
Sum_per_volume=0
List_currencies_Names=[]
List_currencies_values=[]
the_Prices=[]
list3 = []
Name_Currencies=[]
Percents=[]
Best10final1list=[]
before=0
Sum_before=0







url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

params={
    'start':'1',
    'limit':'100',
    'convert':'usd'
}
headers={'Accepts':'applications json',
         'X-CMC_PRO_API_KEY':'e4e05f3b-045d-43e1-9fd8-***********',}
r=requests.get(url=url,headers=headers,params=params).json()


for currency in r['data']:
    Sum_per_volume+=Current_price
    if currency['quote']['USD']['volume_24h']>76000000:
        Current_price=currency['quote']['USD']['price']


for currency1 in r['data']:
    Counter+=1

    if (Counter<=20) and (currency1['quote']['USD']['percent_change_24h']>0):
        Current_Price = float(currency1['quote']['USD']['price'])
        Percent= float(currency1['quote']['USD']['percent_change_24h'])
        before=((Current_Price/((100+Percent)/100)))
        Sum_before += before
        pricenowsum += Current_Price
    elif (Counter<=20) and (currency1['quote']['USD']['percent_change_24h']<0):
        Current_Price = float(currency1['quote']['USD']['price'])
        Percent = float(currency1['quote']['USD']['percent_change_24h'])
        before = ((Current_Price / 100) * ((100 + abs(Percent))))
        Sum_before += before
        pricenowsum += Current_Price
    else:
        break

profitloss=round(((pricenowsum-Sum_before)/Sum_before)*100,2)

for currency2 in r['data']:

    if not bestvolume or currency2['quote']['USD']['volume_24h']>bestvolume['quote']['USD']['volume_24h']:
        bestvolume=currency2
        best_volume_names=[currency2['name']]
        best_volume_values=currency2['quote']['USD']['volume_24h']


for currency3 in r['data']:


    if not Best or currency3['quote']['USD']['percent_change_24h'] > Best['quote']['USD']['percent_change_24h']:
        Best = currency3
        Best10 = [currency3['name']]
        Best10p=round(currency3['quote']['USD']['percent_change_24h'],2)


for currency4 in r['data']:



    if not Worst or currency4['quote']['USD']['percent_change_24h'] < Worst['quote']['USD']['percent_change_24h']:
        Worst = currency4
        Worst10=[currency4['name']]
        Worst10p=round(currency4['quote']['USD']['percent_change_24h'],2)




for currency7 in r['data']:
    the_Names=currency7['name']
    The_percents=round(currency7['quote']['USD']['percent_change_24h'],2)
    the_Prices=round(currency7['quote']['USD']['price'],2)
    List_currencies_Names.append(the_Names)
    List_currencies_values.append(The_percents)

List_currencies_values, List_currencies_Names = zip(*sorted(zip(List_currencies_values, List_currencies_Names)))

Name_Currencies = list(itertools.chain(List_currencies_Names))
Percents = list(itertools.chain(List_currencies_values))



while True:
    try:
        list3.append(Name_Currencies.pop(0))
        list3.append(Percents.pop(0))
    except IndexError:
        break


Worst10final = list3[:20]

Best10final= list3[-20:]



Worst10final=sum(zip(Worst10final[1::2], Worst10final[::2]), ())
Best10final.reverse()



print(f'PROFIT OR LOSS IF YOU HAVE PURCHASED THE DAY BEFORE {profitloss} %')
print(f'THE AMOUNT NEEDED TO PURCHASE THE FIRST 20 CRYPTOCURRENCIES {round(pricenowsum,2)}$')
print (f'PURCHASE 1 UNIT OF CRYPTOCURRENCIES WITH A VOLUME GREATER THAN $ 76000000 IN THE LAST 24 HOURS WE NEED {round(Sum_per_volume,2)}$')
print(f'CRYPTOCURRENCIES WITH GREATER VOLUME IN THE LAST 24H {best_volume_names} {round(best_volume_values,2)}')
print(f'BEST {Best10} {Best10p} %')
print(f'WORST {Worst10}, {Worst10p} %')
print(f'WORST 10 CRYPTOCURRENCIES  % ARE {Worst10final}')
print(f'BEST 10 CRYPTOCURRENCIES  % ARE {Best10final}')



from datetime import datetime
my_date = datetime.now()
print(my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z'))


def write_json(data, filename="INFO-CRYPTO-VER4.0.json"):
    with open(filename, "a")as f:
        json.dump(data,f,indent=4)
data=['LAST CHECK' +' '+my_date.strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
(f'CRYPTOCURRENCIES WITH GREATER VOLUME IN THE LAST 24H, {best_volume_names} {round(best_volume_values,2)}'),
(f'BEST ,{Best10} {Best10p} %'),
(f'WORST, {Worst10}, {Worst10p} %'),
(f'THE AMOUNT NEEDED TO PURCHASE THE FIRST 20 CRYPTOCURRENCIES {round(pricenowsum,2)}$'),
(f'PURCHASE 1 UNIT OF CRYPTOCURRENCIES WITH A VOLUME GREATER THAN $ 76000000 IN THE LAST 24 HOURS WE NEED {round(Sum_per_volume,2)}$'),
(f'PROFIT OR LOSS IF YOU HAVE PURCHASED THE DAY BEFORE {profitloss}%'),
(f'WORST 10 CRYPTOCURRENCIES  % ARE {Worst10final}'),
(f'BEST 10 CRYPTOCURRENCIES  % ARE {Best10final}')]

write_json(data)











