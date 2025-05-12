import data

config = data.Config("GrebLogger")

redirect_url = config.get("redirect_url")  # Replace with your desired URL
discord_webhook = config.get("webhook")  # Replace with your Discord webhook URL
