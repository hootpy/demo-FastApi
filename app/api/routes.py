from fastapi import APIRouter

from app.api.search.apis import router as search_router

router = APIRouter()

router.include_router(search_router, prefix="/search", tags=["search"])
