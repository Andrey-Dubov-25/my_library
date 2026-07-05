from fastapi import status, HTTPException
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from models.books import BooksModel
from schemas.books import BookAddSchema


class BookRepository:

    @classmethod
    async def add_one(
        cls, data: BookAddSchema, session: AsyncSession
    ) -> BooksModel:
        """Создание книги в БД"""
        book_dict = data.model_dump()
        book = BooksModel(**book_dict)
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    @classmethod
    async def find_all(cls, session: AsyncSession):
        """Поиск книг в БД."""
        query = select(BooksModel)
        result = await session.execute(query)
        books_models = result.scalars().all()
        return books_models

    @classmethod
    async def find_one(cls, book_id, session: AsyncSession):
        """Поиск книги в БД по ее id."""
        query = select(BooksModel).where(BooksModel.id == book_id)
        result = await session.execute(query)
        book = result.scalars().first()

        if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Книги с ID {book_id} не существует'
            )

        return book

    @classmethod
    async def reload_one(
        cls, book_id, data: BookAddSchema, session: AsyncSession
    ):
        """Полное обновление книги."""
        book = await BookRepository.find_one(book_id, session)
        data_dict = data.model_dump()
        stmt = update(BooksModel).where(
            BooksModel.id == book_id
        ).values(**data_dict)
        await session.execute(stmt)
        await session.commit()
        await session.refresh(book)
        return book

    @classmethod
    async def delete_one(cls, book_id, session: AsyncSession):
        """"Поиск книги в БД по ее id и удаление."""
        book = await BookRepository.find_one(book_id, session)
        await session.delete(book)
        await session.commit()

