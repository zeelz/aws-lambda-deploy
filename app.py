
import random

def handler (event, context):
    return {
        "statusCode": 200,
        "body": f"Your hello number is {random.randint(2, 200)}"
    }

# print(handler(event=None, context=None))