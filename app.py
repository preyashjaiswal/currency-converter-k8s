from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)
API_URL = "https://open.er-api.com/v6/latest"

@app.route('/')
def home():
    return render_template_string(open('templates/index.html').read())

@app.route('/api/rates')
def rates():
    base = request.args.get('base', 'USD').upper()
    try:
        res = requests.get(f"{API_URL}/{base}", timeout=10)
        data = res.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/convert')
def convert():
    from_curr = request.args.get('from', 'USD').upper()
    to_curr = request.args.get('to', 'EUR').upper()
    amount = float(request.args.get('amount', 1))
    try:
        res = requests.get(f"{API_URL}/{from_curr}", timeout=10)
        data = res.json()
        rates = data.get('rates', {})
        rate = rates.get(to_curr)
        if not rate:
            return jsonify({"error": f"{to_curr} not available"}), 400
        result = amount * rate
        return jsonify({
            "from": from_curr,
            "to": to_curr,
            "amount": amount,
            "rate": rate,
            "result": result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

