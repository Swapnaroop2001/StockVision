from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)

@app.route('/api/welcome', methods=['GET'])
def welcome():
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/api/stock/<string:ticker>', methods=['GET'])
def get_stock(ticker):
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.info
        return jsonify(stock_info)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stock/<string:ticker>/history', methods=['GET'])
def get_stock_history(ticker):
    period = request.args.get('period', '1mo')
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)
        return hist.to_json()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stock/<string:ticker>/actions', methods=['GET'])
def get_stock_actions(ticker):
    try:
        stock = yf.Ticker(ticker)
        actions = {
            "dividends": stock.dividends.to_json(),
            "splits": stock.splits.to_json(),
            "capital_gains": stock.capital_gains.to_json()
        }
        return jsonify(actions)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/stock/<string:ticker>/financials', methods=['GET'])
def get_stock_financials(ticker):
    try:
        stock = yf.Ticker(ticker)
        financials = {
            "income_statement": stock.income_stmt.to_json(),
            "quarterly_income_statement": stock.quarterly_income_stmt.to_json(),
            "balance_sheet": stock.balance_sheet.to_json(),
            "quarterly_balance_sheet": stock.quarterly_balance_sheet.to_json(),
            "cashflow": stock.cashflow.to_json(),
            "quarterly_cashflow": stock.quarterly_cashflow.to_json()
        }
        return jsonify(financials)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
