import snowflake.connector as sf

def lambda_handler(event, context):
    print(event)
    execute_the_query=event['queryStringParameters']['query']
    print("Query to be executed : ",execute_the_query)
    user=os.environ['username']
    print("Username : ",user)
    password=os.environ['password']
    print("Password : ",password)
    account="nx50928.ap-southeast-1.aws";
    database="GOLDSTONE"
    warehouse="COMPUTE_WH"
    schema="PUBLIC"
    role="ACCOUNTADMIN"
    conn=sf.connect(user=user,password=password,account=account)
    print("Connection successfully created")