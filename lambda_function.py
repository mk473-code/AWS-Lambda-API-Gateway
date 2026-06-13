import json

def lambda_handler(event, context):
    # Get 'name' from query string or body, default to 'World'
    name = "World"

    if event.get("queryStringParameters") and event["queryStringParameters"].get("name"):
        name = event["queryStringParameters"]["name"]
    elif event.get("body"):
        body = json.loads(event["body"])
        name = body.get("name", "World")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": f"Hello {name}, welcome to AWS Lambda!"})
    }
