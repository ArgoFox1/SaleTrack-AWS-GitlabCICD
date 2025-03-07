from flask import Flask, render_template, request, redirect, url_for
from db import init_db, add_sale, get_daily_sales

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_sale', methods=['POST'])
def add_sale_route():
    product_name = request.form['product_name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    description = request.form['description']
    
    add_sale(product_name, quantity, price, description)
    
    return redirect(url_for('index'))

@app.route('/report')
def report():
    sales, total_revenue = get_daily_sales()
    return render_template('report.html', sales=sales, total_revenue=total_revenue)

if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
