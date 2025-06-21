# api/mines_predict.py

from stake_logic import generate_mines_layout

def handler(request):
    try:
        if request.method != "POST":
            return {
                "statusCode": 405,
                "body": "Method Not Allowed"
            }

        data = request.get_json()
        mines = data.get("mines", 3)
        tiles = generate_mines_layout(mines)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": { "tiles": tiles }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
