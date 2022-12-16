from sqlalchemy.orm import joinedload, selectinload

from core.crud import CRUDPaginated
from models.publishers import Author

author_crud = CRUDPaginated(
    model=Author,
    get_options=[joinedload(Author.user)],
    get_multi_options=[joinedload(Author.user)],
)
