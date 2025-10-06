from beanie import Document

# defines how users data will be structured in the database
class user(Document):
    name: str
    email: str
    email_verified: bool = False
    created_at: str
    updated_at: str