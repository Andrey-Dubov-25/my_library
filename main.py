from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import engine, Model
from models.books import BooksModel
from routers.book import router as books_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Старт и остановка приложения."""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
        print('База данных готова к работе')
        yield
        print('Выключение сервера')


app = FastAPI(lifespan=lifespan)
app.include_router(books_router)
