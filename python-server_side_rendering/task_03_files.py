#!/usr/bin/python3
"""
This the route of app.
"""
from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        items = json.load(file).get('items')
        return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    product = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')
    
    if source == 'json':
        try:
            with open('products.json', 'r') as file:
                products = json.load(file)
        except FileNotFoundError:
            return render_template('product_display.html', error='Not file found')
    
    elif source == 'csv':
        try:
            with open('products.csv', 'r', newline='') as f:
                read = csv.DictReader(f)
                products = list(read)
        except FileNotFoundError:
            return render_template('product_display.html', error='Not file found')
    
    else:
        return render_template('product_display.html', error='Wrong source')
    
    if product:
        products = [p for p in products if str(p.get('id')) == product]
        if not products:
            return render_template('product_display.html', error='Product not found')
    
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
