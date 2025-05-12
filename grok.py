import pyngrok
import time
import asyncio
import shared



def start_ngrok(port:int = 5000):
    # Establish connectivity
    listener = ngrok.forward(port, authtoken=shared.ngrok_token, region="eu", bind_tls=True)

    # Output ngrok url to console
    print(f"Ingress established at {listener.url()}")

    # Keep the listener alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Closing listener")
        listener.close()