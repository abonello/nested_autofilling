import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

depts = [
    {   
        "ref": "radiology",
        "name": "Radiology",
        "services": [
            "X-Rays",
            "Gamma-Rays",
            "Photograpy"
        ]
    },
    {   
        "ref": "another",
        "name": "Another department",
        "services": [
            "Plaster",
            "Straighten bent bones",
            "lengthening bones"
        ]
    },
    {
        "ref": "dentistry",
        "name": "Dentistry",
        "services": [
            "Pull out teeth",
            "cementing teeth",
            "straigthening teeth",
            "whitening"
        ]
    }
]

@app.route("/")
def home():
    return render_template("index.html", depts=depts)

@app.route("/services", methods=["POST"])
def services():

    # data = [
    #         "Plaster",
    #         "Straighten bent bones",
    #         "lengthening bones"
    #     ]
    # return jsonify({"data": data})
    data = request.form['ref']
    # print(data)

    for dept in depts:
        # print(dept['ref'])
        if dept['ref'] == data:
            services = dept['services']
            # print(services)

    if services:

        #  get services

        return jsonify({"data": services})
    return jsonify({"error" : "an error occured"})
    # return "Pass"


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True) # Is it because of the different server?