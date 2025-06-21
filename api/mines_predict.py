import json
from stake_logic import generate_mines_layout

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Method not allowed"})
        }

    try:
        body = request.json()
        mines = body.get("mines", 3)
        tiles = generate_mines_layout(mines)
        return {
            "statusCode": 200,
            "body": json.dumps({"tiles": tiles})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
