from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)

# Simulasi fungsi API untuk mendapatkan followers
def add_followers(username, country, count):
    # Logika untuk memproses followers organik
    print(f"Adding {count} followers from {country} to {username}")
    time.sleep(random.randint(1, 3))
    return {"status": "success", "message": f"{count} followers added to {username}"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-followers', methods=['POST'])
def process_followers():
    username = request.form.get('username')
    country = request.form.get('country')
    count = int(request.form.get('count'))
    result = add_followers(username, country, count)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
