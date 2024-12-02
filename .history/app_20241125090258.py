from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Mã bí mật cho session

# Dữ liệu sản phẩm mẫu
products = [
    {'id': 1, 'name': 'Elegant Dress', 'description': 'A stylish and elegant dress perfect for any occasion.', 'price': 50.00, 'image': 'dress.jpg'},
    {'id': 2, 'name': 'Comfortable T-shirt', 'description': 'Soft and comfortable cotton t-shirt for everyday wear.', 'price': 20.00, 'image': 'tshirt.jpg'},
    {'id': 3, 'name': 'Trendy Jeans', 'description': 'Classic denim jeans that are perfect for any outfit.', 'price': 40.00, 'image': 'jeans.jpg'}
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
