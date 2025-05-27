import data

config = data.Config("GrebLogger")

redirect_url = config.get("redirect_url") or "https://google.com/"
discord_webhook = config.get("webhook")
