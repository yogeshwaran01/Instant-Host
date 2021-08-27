from urllib.parse import urlparse

from flask import jsonify, make_response, request

from app import app

from .models import DATABASE


@app.route("/")
def index():
    return jsonify({"message": "ok"})


@app.route("/api/host", methods=["POST"])
def get_source():
    if request.json is None:
        return jsonify({"error": "Source is required"})
    source_code = request.json.get("source")
    mimetype = request.json.get("mimetype", "text/html")
    if source_code is None:
        return jsonify({"error": "Source is required"})

    x = DATABASE.store_data(source_code, mimetype)
    host = urlparse(request.host_url)
    host_base = host.scheme + "://" + host.netloc
    return jsonify(
        {
            "public_key": x.get("public_key"),
            "private_key": x.get("private_key"),
            "hosted_at": f'{host_base}/render/{x.get("public_key")}',
            "created_at": x.get("time").strftime("%m/%d/%Y, %H:%M:%S"),
            "mimetype": x.get("mimetype"),
        }
    )


@app.route("/api/edit", methods=["POST"])
def change_source():
    if request.json is None:
        return jsonify({"error": "Source and Key are required"})
    pri_key = request.json.get("key")
    source = request.json.get("source")
    if source and pri_key:
        if pri_key in DATABASE.all_private_key():
            host = urlparse(request.host_url)
            host_base = host.scheme + "://" + host.netloc
            x = DATABASE.change_source_by_private_key(pri_key, source)
            return jsonify(
                {
                    "public_key": x.get("public_key"),
                    "private_key": x.get("private_key"),
                    "hosted_at": f'{host_base}/render/{x.get("public_key")}',
                    "updated_at": x.get("time").strftime("%m/%d/%Y, %H:%M:%S"),
                    "mimetype": x.get("mimetype"),
                }
            )
        return jsonify({"error": "key is Invalid"})
    return jsonify({"error": "source or key is missing"})


@app.route("/render/<pub_key>")
def send_source(pub_key):
    if pub_key in DATABASE.all_public_key():
        key = DATABASE.get_key_from_pub_key(pub_key)
        res = make_response(DATABASE.get_source_from_public_key(pub_key, key))
        res.mimetype = DATABASE.get_mimetype_from_pub_key(pub_key)
        return res

    else:
        return jsonify({"error": "No Key Found"})


@app.route("/api/delete", methods=["POST"])
def del_source():
    if request.json is None:
        return jsonify({'error': "Private key is required to delete the post"})
    pri_key = request.json.get('key')
    if pri_key in DATABASE.all_private_key():
        DATABASE.remove_source_by_private_key(pri_key)
        return jsonify({"message": f"Source of '{pri_key}' Removed Successfully"})
    else:
        return jsonify({"error": "Key is Invalid"})


@app.after_request
def enabale_cors(res):
    header = res.headers
    header['Access-Control-Allow-Origin'] = '*'
    return res
