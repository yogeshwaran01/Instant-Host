from .processing import Text
from .generators import generate_pri_key, generate_pub_key


def test_processing():
    sample_text = "Hello Word"
    encoded_text = Text.encode_and_compress(sample_text)
    assert bytes(sample_text, "utf-8") == Text.decompress_and_decode(
        encoded_text.get("token"), encoded_text.get("key")
    )


def test_generators():
    selection_list = [
        1,
        2,
        3,
        5,
    ]
    pub = generate_pub_key(selection_list)
    pri = generate_pri_key(pub)
    assert pub not in selection_list
    assert pub in pri
