from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Employee


class EmployeeCrud:
    @classmethod
    async def get_employees(cls, db: AsyncSession, page: int, limit: int, filters: dict[str, list[str]]):
        offset = (page - 1) * limit
        conditions = []
        for key, value in filters.items():
            attr = getattr(Employee, key, None)
            if attr:
                conditions.append(attr.in_(value))

        return await db.execute(select(Employee).filter(*conditions).offset(offset).limit(limit))
