import pandas as pd
web_xys={"Days":[1,2,3,4,5],"Visitor":[123,258,369,789,456],"Bounce_rate":[12,36,12,32,14]}
#dataFrame of this tabuler data

'''Days  Visitor  Bounce_rate
0     1      123           12
1     2      258           36
2     3      369           12
3     4      789           32
4     5      456           14'''

df=pd.DataFrame(web_xys)
#first 2 rpws data
print(df.head(2))
#last 2 rows data
print(df.tail(2))
