import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Momodou Lamin Sanyang'
    signup_ts: datetime.datetime = None
    friends: list[int] = []

external_data = {
    'id': '123',
    'signup_ts': '2017-06-01 12:22',
    'friends': [1, '2', b'3'],
}
user = User(**external_data)
print(user.json())
print(user.id)

async def khalifa():
    print('khalifa')