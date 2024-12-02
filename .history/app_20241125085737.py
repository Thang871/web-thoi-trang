from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cấu hình secret key cho Flask session

# Các sản phẩm mẫu
products = {
    'dress': {'name': 'Đầm Dạ Hội', 'price': 150000, 'image': 'images/dress.jpg'},
    'tshirt': {'name': 'Áo Thun Unisex', 'price': 85000, 'image': 'images/tshirt.jpg'},
    'jeans': {'name': 'Quần Jeans', 'price': 100000, 'image': 'images/jeans.jpg'}
}

@app.route('/')
def home():
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}
    if product_id in session['cart']:
        session['cart'][product_id] += 1
    else:
        session['cart'][product_id] = 1
    session.modified = True
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    for product_id, quantity in session.get('cart', {}).items():
        product = products.get(product_id)
        if product:
            cart_items.append({
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'total': product['price'] * quantity
            })
            total += product['price'] * quantity
    return render_template('cart.html', cart_items=cart_items, total=total)

if __name__ == '__main__':
    app.run(debug=True)
