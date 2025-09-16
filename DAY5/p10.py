from flask import Flask,jsonify,request

products = [{'pid':101,'pname':'pA','pcost':1000},
            {'pid':102,'pname':'pB','pcost':2000},
            {'pid':103,'pname':'pC','pcost':3000}
           ] # dataset (or) database 

app = Flask(__name__)

@app.route("/products",methods=['GET'])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>",methods=['GET'])
def get_product(product_id):
    product = next((var for var in products if var['pid'] == product_id),None)
    return jsonify(product) if product else ('Product not found',404)

@app.route("/products",methods=["POST"])
def add_new_product():
    new_product = request.get_json()
    products.append(new_product)
    return jsonify(new_product),201

@app.route("/product/<int:product_id>",methods=['PUT'])
def update_product(product_id):
    product = next((var for var in products if var['pid'] == product_id),None)
    if product:
        data = request.get_json()
        product.update(data)
        return jsonify(data)
    else:
        return "Product ID not found",404

if __name__ == '__main__':
    app.run(debug=True)