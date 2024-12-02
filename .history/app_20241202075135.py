from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Mã bí mật cho session

# Dữ liệu sản phẩm mẫu
products = [
    {'id': 1, 'name': 'Đầm Dạ Hội', 'description': 'Đầm phong cách tôi giản, form dáng theo phong cách Châu Âu.', 'price': 150000, 'image': 'dress.jpg'},
    {'id': 2, 'name': 'Aó Thun Unisex', 'description': 'Aó thun cao cấp với chất liệu cotton mềm mịn thoải mái.', 'price': 85000, 'image': 'tshirt.jpg'},
    {'id': 3, 'name': 'Quần Jeans', 'description': 'Quần Jeans cao cấp co giản 4 chiều cực đẹp.', 'price': 100000, 'image': 'jeans.jpg'}
]

@app.route('/')
def home():
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session

# Sample product data
products = [
    {'id': 1, 'name': 'Đầm Dạ Hội', 'description': 'Đầm phong cách tôi giản, form dáng theo phong cách Châu Âu.', 'price': 150000, 'image': 'dress.jpg'},
    {'id': 2, 'name': 'Aó Thun Unisex', 'description': 'Aó thun cao cấp với chất liệu cotton mềm mịn thoải mái.', 'price': 85000, 'image': 'tshirt.jpg'},
    {'id': 3, 'name': 'Quần Jeans', 'description': 'Quần Jeans cao cấp co giản 4 chiều cực đẹp.', 'price': 100000, 'image': 'jeans.jpg'}
]

@app.route('/')
def home():
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart
    return redirect(url_for('home'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    # Remove the product from the cart
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

