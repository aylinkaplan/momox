import requests
from flask import Flask, request

import xmltodict

app = Flask(__name__)


@app.route('/')
def index_view():
    return "Welcome!"


@app.route('/orders', methods=["GET", "POST"])
def orders():
    data = request.data
    if not data:
        return "Not available data"
    employee_dict = xmltodict.parse(request.data)
    employee_list = employee_dict["Employees"]["Employee"]
    json_body = {"orders": []}
    # menu_response = requests.get('http://nourish.me/api/v1/menu')
    # read response and find dish_id based on dish name.
    for employee in employee_list:
        if employee["IsAttending"] == 'true':
            order_list = employee["Order"].split(',')
            dish_list = []
            for order in order_list:
                order = order.split('x')
                dish_name = order[1]
                amount = order[0]
                dishes = {
                    "dish_name": dish_name,  # menu.json file and the others were not reachable sources so dish_id's implementation was not made.
                    "amount": amount
                }
                dish_list.append(dishes)

            customer = {
                "full_name": employee['Name'],
                "address": {
                    "street": employee["Address"]["Street"],
                    "city": employee["Address"]["City"],
                    "postal_code": employee["Address"]["PostalCode"]
                }
            }
            customer_order = {"customer": customer, "dishes": dish_list}
            json_body["orders"].append(customer_order)
            # requests.post("http://nourish.me/api/v1/bulk/order", json=json_body)
            return json_body


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
