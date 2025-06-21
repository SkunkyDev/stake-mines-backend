from stake_logic import generate_mines_layout

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 405,
            "body": "Method Not Allowed"
        }

    try:
        data = request.json()
        mines = data.get("mines", 3)
        tiles = generate_mines_layout(mines)
        return {
            "statusCode": 200,
            "body": {"tiles": tiles}
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
