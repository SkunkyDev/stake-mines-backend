import json
from stake_logic import generate_mines_layout

def handler(event, context):
    try:
        body = json.loads(event["body"])
        mines = int(body.get("mines", 3))
        tiles = generate_mines_layout(mines)
        return {
            "statusCode": 200,
            "body": json.dumps({"tiles": tiles}),
            "headers": {"Content-Type": "application/json"}
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }
