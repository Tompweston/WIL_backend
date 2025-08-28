from beanie import Document

# defines how users data will be structured in the database
class User(Document):
    email: str
    name: str
    #password_hash: str