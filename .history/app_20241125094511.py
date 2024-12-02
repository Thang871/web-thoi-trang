from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Mã bí mật cho session

# Dữ liệu sản phẩm mẫu
products = [
    {'id': 1, 'name': 'Đầm Dạ Hội', 'description': 'Đầm phong cách tôi giản,  form dáng theo phong cách Châu Âu.', 'price': 150000, 'image': 'dress.jpg'},
    {'id': 2, 'name': 'Aó Thun Unisex', 'description': 'Aó thun cao cấp với chất liệu cotton mềm mịn thoải mái.', 'price': 85000, 'image': 'tshirt.jpg'},
    {'id': 3, 'name': 'Quần Jeans', 'description': 'Quần Jeans cao cấp co giản 4 chiều cực đẹp.', 'price': 100000, 'image': 'jeans.jpg'}
]

@app.route('/')
def home():
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Tìm sản phẩm theo ID
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if product:
        # Lấy giỏ hàng từ session, nếu không có thì khởi tạo giỏ hàng mới
        cart = session.get('cart', [])
        cart.append(product)  # Thêm sản phẩm vào giỏ hàng
        session['cart'] = cart  # Cập nhật lại giỏ hàng trong session
    return redirect(url_for('home'))  # Quay lại trang sản phẩm

@app.route('/cart')
def cart():
    # Lấy giỏ hàng từ session
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
