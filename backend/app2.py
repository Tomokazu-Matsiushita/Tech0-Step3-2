# from flask import Flask
# app2 = Flask(__name__)

# @app2.route("/store")
# def get_stores():
#     return{"stores": stores}

# stores = [
#     {
#         "name": "Store1",
#         "items": [
#             {
#                 "name": "Chair"
#                 "price": 15.99
#             },
#         ]
#     },
# ]
from flask import Flask
app2 = Flask(__name__)

@app2.route("/store")
def get_stores():
    return {"stores": stores}

stores = [
    {
        "name": "Store1",
        "items": [
            {
                "name": "Chair",  # Add a comma here
                "price": 25.99
            },
        ]
    },
]
