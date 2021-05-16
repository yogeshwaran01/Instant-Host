from datetime import datetime

from app import database as db

from utils.generators import generate_pri_key, generate_pub_key
from utils.processing import Text


class SourceCode(db.Model):
    __tablename__ = "sourcecodes"

    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.String(150))
    private_key = db.Column(db.String(150))
    mimetype = db.Column(db.String(50))
    src = db.Column(db.LargeBinary)
    key = db.Column(db.LargeBinary)
    time = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"SourceCode({self.public_key})"


class DATABASE:
    @staticmethod
    def all_public_key():
        return [i.public_key for i in SourceCode.query.all()]

    @staticmethod
    def all_sources_code():
        return [i.src for i in SourceCode.query.all()]

    @staticmethod
    def all_private_key():
        return [i.private_key for i in SourceCode.query.all()]

    @staticmethod
    def get_source_from_public_key(public_key: str, key):
        data = SourceCode.query.filter_by(public_key=public_key).first()
        source = data.src
        # if media:
        #     return Media.decompress_and_decode(source, key)
        return Text.decompress_and_decode(source, key)

    @staticmethod
    def get_source_from_private_key(private_key: str, key):
        data = SourceCode.query.filter_by(private_key=private_key).first()
        source = data.src
        # if media:
        #     return Media.decompress_and_decode(source, key)
        return Text.decompress_and_decode(source, key)

    @staticmethod
    def get_pub_key_from_source(src):
        data = SourceCode.query.filter_by(src=src).first()
        return data.public_key

    @staticmethod
    def get_key_from_pub_key(key):
        data = SourceCode.query.filter_by(public_key=key).first()
        return data.key

    @staticmethod
    def get_mimetype_from_pub_key(key):
        data = SourceCode.query.filter_by(public_key=key).first()
        return data.mimetype

    @staticmethod
    def store_data(data, mimetype):
        # if media:
        #     processor = Media.encode_and_compress(data)
        # else:
        processor = Text.encode_and_compress(data)
        encoded_data = processor.get("token")
        key = processor.get("key")
        if encoded_data in DATABASE.all_sources_code():
            return DATABASE.get_pub_key_from_source(encoded_data)

        pub_key = generate_pub_key(DATABASE.all_public_key())
        pri_key = generate_pri_key(pub_key)
        src_code = SourceCode(
            src=encoded_data,
            public_key=pub_key,
            private_key=pri_key,
            key=key,
            mimetype=mimetype,
        )
        db.session.add(src_code)
        db.session.commit()

        return {
            "public_key": pub_key,
            "private_key": pri_key,
            "key": key,
            "time": src_code.time,
            "mimetype": src_code.mimetype,
        }

    @staticmethod
    def change_source_by_private_key(pri_key, new_source):
        srccode = SourceCode().query.filter_by(private_key=pri_key).first()
        processor = Text.encode_and_compress(new_source)
        srccode.src = processor.get("token")
        srccode.key = processor.get("key")
        srccode.time = datetime.utcnow()
        db.session.commit()

        return {
            "public_key": srccode.public_key,
            "private_key": srccode.private_key,
            "key": srccode.key,
            "time": srccode.time,
            "mimetype": srccode.mimetype,
        }
