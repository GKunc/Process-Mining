import json
from flask import Flask, make_response
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner


app = Flask(__name__)


@app.route('/test')
def test():  # put application's code here
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.set_data("Working test!")
    return response


@app.route('/pm4py')
def pm4py():
    log = xes_importer.apply('A2-disco.xes')

    tree = inductive_miner.apply_tree(log)
    print(tree.children.__str__())
    data = json.dumps(tree.children.__str__())

    print(data)
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    response.headers.add("Content-type", "application/json")
    response.set_data(data)
    return response


if __name__ == '__main__':
    app.run()
