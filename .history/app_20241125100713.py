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
    return render_template('index.html', products=products)

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Tìm sản phẩm trong danh sách products
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        # Lấy danh sách giỏ hàng từ session (nếu có) hoặc khởi tạo giỏ hàng mới
        cart_items = session.get('cart_items', [])
        cart_items.append(product)  # Thêm sản phẩm vào giỏ hàng
        session['cart_items'] = cart_items  # Lưu giỏ hàng vào session
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart_items', [])
    total_price = sum(item['price'] for item in cart_items)  # Tính tổng giá trị giỏ hàng
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)