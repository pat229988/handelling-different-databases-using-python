
# # Example snippet for dynamo Db


# imports for  dynamo Db 
import boto3
from boto3.dynamodb.conditions import Key, Attr

# setting up connection
# once setup no need for reconnecting throught the appllication
ACCESS_ID ='Your_Access_Key_Id'
ACCESS_KEY ='Your_Secret_Access_Key'
ddb = boto3.resource('dynamodb', region_name='Region of Aws server',aws_access_key_id=ACCESS_ID,aws_secret_access_key= ACCESS_KEY)
# eg of region - 'ap-south-1'

#reading Database table
Any_variable_for_table = ddb.Table('Table_Name')

#finding a row / rows from the table with single attribute
response = Any_variable_for_table.scan(FilterExpression = Attr('Table column').eq("things to be found"))

#finding a row / rows from the table with multiple attributes
response = Any_variable_for_table.scan(FilterExpression = Attr('Table column1').eq("elm1") & Attr('Table column2').eq("elm2"))

#response will be in the form of multi dimensional list
# to extract a perticular value from the row we can get it from response variable
# EG - response['Items'][pos1]['pos2']
# here pos1 will be an integer determining the index of rows founded match.
# pos2 can be either of the column name.


# # Notes for getting your Access Keys to dynamo Db on AWS


# 1. To create access keys for an IAM user
# 2. Sign in to the AWS Management Console and open the IAM console.
# 3. In the navigation pane, choose Users.
# 4. Choose the name of the user whose access keys you want to create, and then choose the Security credentials tab.
# 5. In the Access keys section, choose Create access key.
# 6. To view the new access key pair, choose Show. You will not have access to the secret access key again after this dialog box closes. Your credentials will look something like this:
# 7. Examples:
#     Access key ID: AKIAIOSFODNN7EXAMPLE
#     Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
# 8. To download the key pair, choose Download .csv file. Store the keys in a secure location. You will not have access to the secret access key again after this dialog box closes.
# 9. Keep the keys confidential in order to protect your AWS account and never email them. Do not share them outside your organization, even if an inquiry appears to come from AWS or Amazon.com. No one who legitimately represents Amazon will ever ask you for your secret key.
# 10. After you download the .csv file, choose Close. When you create an access key, the key pair is active by default, and you can use the pair right away.





# # Example snippet for MySQL Db


#imports for pymysql 
import pymysql as mdb

#Setting up connection
######## imp notes ###################
# if the application has multiple processing and requires data at different location,
# try making the connection at global variables or in a global function.
# it is not required to make reconnected to the database for every query execution,
# but the connection terminates itself if not called after a specific time period.
# so, calling a global function for reconnecting to the database makes it easier.
hst = 'ip or localhost or name and path of the db on web'
P_ID = "port number" # this value must be numeric
usr = "USER_OF_DB"
pss = "USERS_PASS"
db_con = mdb.connect(host = hst, port = P_ID, user = usr, password = pss, database='DATABASE_NAME')
cursor = db_con.cursor()

# writing up the query string for intermediate edits in the striig
# use the .format or the %s in format string
qry="select pass,dept,role from users where email like {}".formate(var)
qry="select pass,dept,role from users where email like '%s'"%(var)
cursor.execute(qry)

# here the query work like the same as on SQL Console
# and there are two methods to fetch the output presented on the console

# use fetchone() method to get the single row output from the connsole
rs=cursor.fetchone()

# use fetchall() method to get the full table output from the connsole
rs=cursor.fetchall()

# output results in a multi dimensional list 
#EG - 
#rs[pos1][pos2]
# to get the element we can use the indexs of the list.
# the pos1 determines the row value.
# the pos2 determines the column value.






