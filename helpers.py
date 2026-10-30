import uuid
import secrets
import faker

fake = faker.Faker()

def get_fake_user_data():
    return {
        "email": f"test-{uuid.uuid4().hex}@example.org",
        "password": secrets.token_urlsafe(24),
        "name": fake.name()
    }