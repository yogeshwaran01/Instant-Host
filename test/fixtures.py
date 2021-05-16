import tempfile

import pytest

from app import app, database


@pytest.fixture
def client():
    file = tempfile.mkdtemp()
    _, app.config["SQLALCHEMY_DATABASE_URI"] = file[0], "sqlite:///" + file[1] + ".db"
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            database.init_app(app)
            database.create_all()
            database.session.commit()

        yield client
