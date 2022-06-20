from pydantic import BaseModel

class Data(BaseModel):
    fibNumber: int

class Session(BaseModel):
    username: str
    password: str

class CloseSession(Session):
    session_id: str

class SessionStatus(Session):
    bin: str
    x509_auth: str
