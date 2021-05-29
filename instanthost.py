# -*- coding: utf-8 -*-
"""
    instanthost
    ~~~~~~~~~~

    A cli tool to host any non-binary files

    :license: MIT License
"""

__package__ = "instagramy"
__version__ = "1.1"
__description__ = "A cli tool to host any non-binary files"
__url__ = "https://github.com/yogeshwaran01/Instant-Host"
__author__ = "YOGESHWARAN R <yogeshin247@gmail.com>"
__license__ = "MIT License"
__copyright__ = "Copyright 2021 Yogeshwaran R"

import argparse
import json
import mimetypes
import urllib.parse
import urllib.request

host_api = "http://instant-host.herokuapp.com/api/host"
edit_api = "http://instant-host.herokuapp.com/api/edit"
delete_api = "http://instant-host.herokuapp.com/api/delete"
short_api = "https://tinyurl.com/api-create.php"


def short(big_url: str):
    """
    Function short the big urls to tiny by Tiny Api
    """

    req = urllib.request.Request(short_api)
    data = urllib.parse.urlencode({"url": big_url}).encode("utf-8")
    res = urllib.request.urlopen(req, data)
    return res.read().decode()


def post(url: str, json_data: dict):
    """
    Post data to API and return the response data
    """

    req = urllib.request.Request(url)
    req.add_header("Content-Type", "application/json; charset=utf-8")
    data = json.dumps(json_data).encode("utf-8")
    response = urllib.request.urlopen(req, data)
    return json.loads(response.read().decode())


def main():
    parser = argparse.ArgumentParser(
        description="Host page or any non-binary file from your Terminal"
    )

    parser.add_argument("file")
    parser.add_argument(
        "--edit",
        required=False,
        help="To Edit or Update your file",
        action="store_true",
    )
    parser.add_argument(
        "--key", required=False, help="Your Private Key for edit or update and delete"
    )

    arguments = parser.parse_args()

    if arguments.file == "delete":
        if arguments.key is None:
            print("👎 Please provide the private key 😞")
            exit()
        response = post(delete_api, json_data={"key": arguments.key})
        if "error" in response:
            print("👎 Unable to delete the file 😞")
        else:
            print("✌️  Deleted Successfully ✨")

        exit()

    with open(arguments.file, "r") as file_obj:
        try:
            source = file_obj.read()
        except UnicodeDecodeError:
            print("👎 Binary file are not supported 😞")
            exit()

    if arguments.edit:
        response = post(edit_api, json_data={"source": source, "key": arguments.key})

    else:
        mimetype = mimetypes.guess_type(arguments.file)[0]
        if mimetype:
            response = post(
                host_api, json_data={"source": source, "mimetype": mimetype}
            )
        else:
            print("👎 Unable Detect the Mimetype of the File 😞")
            exit()

    shorted_url = short(response["hosted_at"])
    response.update({"tiny_url": shorted_url})
    print("✌️  Hosted Successfully ✨" + "\n")

    for i, j in response.items():
        print(f"{i}: {j}" + "\n")
