from fastapi import APIRouter, status

from database import SessionDep
from schemas.books import BookAddSchema, BookSchema
from repository.book import BookRepository


router = APIRouter(prefix='/books', tags=['Книги'])


@router.get('/', response_model=list[BookSchema])
async def get_books(session: SessionDep):
    """Получить и вернуть список всех книг."""
    books = await BookRepository.find_all(session)
    return books


@router.get('/{book_id}', response_model=BookSchema)
async def get_book(book_id: int, session: SessionDep):
    """Получить и вернуть книгу по ее id."""
    book = await BookRepository.find_one(book_id, session)
    return book


@router.post(
    '/', response_model=BookSchema, status_code=status.HTTP_201_CREATED
)
async def create_book(book: BookAddSchema, session: SessionDep):
    """Создать и вернуть новую книгу."""
    book_model = await BookRepository.add_one(book, session)
    return book_model


@router.put('/{book_id}', response_model=BookSchema)
async def reload_book(book_id: int, data: BookAddSchema, session: SessionDep):
    """Полностью обновить и вернуть книгу."""
    book = await BookRepository.reload_one(book_id, data, session)
    return book


@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int, session: SessionDep):
    """Удалить книгу."""
    await BookRepository.delete_one(book_id, session)
