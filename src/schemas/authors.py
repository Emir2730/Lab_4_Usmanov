from typing import List

from pydantic import BaseModel

from schemas.contracts import ContractBare
from schemas.core import ListModel
from schemas.users import UserBare


class AuthorUpdate(BaseModel):
    passport: str
    address: str
    phone: str


class AuthorCreate(AuthorUpdate):
    user_id: int


class AuthorBare(AuthorCreate):
    id: int

    class Config(AuthorCreate.Config):
        orm_mode = True


class AuthorFull(AuthorBare):
    contract: ContractBare
    user: UserBare


class AuthorList(ListModel):
    data: List[AuthorBare]
