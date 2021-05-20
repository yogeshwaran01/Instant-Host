import json

from .fixtures import client


sample_json_test_1 = """
{
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}
"""

sample_json_test_2 = """
{
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}
"""


def test_api(client):
    response_1 = client.post(
        "/api/host", json={"source": sample_json_test_1, "mimetype": "application/json"}
    )
    url = response_1.get_json()["hosted_at"]
    private_key = response_1.get_json()["private_key"]
    response_2 = client.get(url)
    assert response_1.headers["Content-Type"] == "application/json"
    assert response_1.status_code == 200
    assert response_2.headers["Content-Type"] == "application/json"
    assert response_2.status_code == 200
    data_rendered = response_2.get_json()
    assert data_rendered == json.loads(sample_json_test_1)
    response_3 = client.post(
        "/api/edit", json={"source": sample_json_test_2, "key": private_key}
    )
    assert response_3.headers["Content-Type"] == "application/json"
    assert response_3.status_code == 200
    assert b"updated_at" in response_3.data
    response_4 = client.get(url)
    assert response_4.headers["Content-Type"] == "application/json"
    assert response_4.status_code == 200
    data_rendered = response_4.get_json()
    assert data_rendered == json.loads(sample_json_test_2)
    response_5 = client.post(
        "/api/delete", json={"key": private_key}
    )
    assert response_5.status_code == 200
    assert response_5.get_json() == {"message": f"Source of '{private_key}' Removed Successfully"}
