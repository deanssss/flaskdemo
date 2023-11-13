from flask import Blueprint, request
from model.user import User
from util.json_util import serialize, make_json_rsp

test = Blueprint("test", __name__, url_prefix="/test")


@test.route('/testjson', methods=['POST'])
def testjson():
    data = request.get_json()
    # data = json.loads(data_)
    print("username: " + data['username'] + ", password: " + data['password'])
    user = User.query.first()
    user.username = data['username']
    return make_json_rsp(serialize(user))
