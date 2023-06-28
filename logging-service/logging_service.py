import flask
import hazelcast

app = flask.Flask(__name__)
app.config["DEBUG"] = True

hz = hazelcast.HazelcastClient( 
        cluster_members=[
        "172.25.0.9:5701",
        "172.25.0.10:5701",
        "172.25.0.11:5701"
    ])
map = hz.get_map("MAP").blocking()

@app.route('/logging', methods=['GET', 'POST'])
def logging_serv():
    if flask.request.method == 'GET':
        return forward_get()
    else:
        return forward_post()

def forward_post():
    data=flask.request.json
    print('Logging received POST request from client: ', data)
    try:
        map.set(data["uuid"], data["msg"])
        print("Saved to hazelcast map")
        return "OK"
    except Exception as ex:
        raise ex
        print('Message cannot be saved to hazelcast map')
        return 500      

def forward_get():
    data=flask.request.json
    print('Logging received GET request from client: ', data)
    try:
        print('Return messages: ',  map.values())
        return ','.join(map.get_all(map.key_set()).values())
    except Exception as ex:
        raise ex
        return 400


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8011)