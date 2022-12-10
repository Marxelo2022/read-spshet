from flask import Flask, jsonify
from openpyxl import load_workbook
import pandas as pd

app = Flask(__name__)


@app.route("/api/users/count", methods=["GET"])

def count_users():
    wb = load_workbook("users_academlo.xlsx")
    ws = wb.active

    df = pd.DataFrame(ws.values)
    count = df.count()
    count = count.to_dict()
    
    return jsonify({"count": count})



if __name__ == '__main__':
    app.run(port=9000, debug=True)
