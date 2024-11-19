import pickle
# we are going to use Flask micro web framework (very lightweight, can add extensions to make it more intense)
# alternative - Django
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_model():
    # unpickle header and tree in tree.p
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile)
    infile.close()
    return header, tree

def tdidt_predict(header, tree, instance):
    info_type = tree[0]
    if info_type == "Leaf":
        return tree[1] # label
    att_index = header.index(tree[1])
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            return tdidt_predict(header, value_list[2], instance)
        
# we need to add some routes!
# a "route" is a function that handles a request
# eg. for the HTML content for a home page
# or for the JSON response for a /predict API endpoint
@app.route("/")
def index():
    # return content and status code
    return "<h1>Welcome to the interview app</h1>", 200

# let's add a route for the /predictb endpoint
@app.route("/predict")
def predict():
    # lets parse the unseen instance values from the query string
    # 
    level = request.args.get("level")
    lang = request.args.get("lang")
    tweets = request.args.get("tweets")
    phd = request.args.get("phd")
    instance = [level, lang, tweets, phd]
    header, tree = load_model()
    pred = tdidt_predict(header, tree, instance)
    if tree is not None:
        return jsonify({"prediction": pred}), 200
    return "Error making a prediction", 400

if __name__ == "__main__":
    # header, tree = load_model()
    # print(header)
    # print(tree)
    # host is IP address when putting it out for production
    app.run(host="0.0.0.0", port=5001, debug=True)
    # TODO: when deploy app to production, set debug to False and check host and port 