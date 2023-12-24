from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.depends.get_session import get_session
from app.common.depends.throttle import Throttle
from app.crud.employee import EmployeeCrud

router = APIRouter(
    tags=["search"],
)


@router.get("/", dependencies=[Depends(Throttle(2, 30))])
async def search(
    page: int = 1,
    limit: int = 20,
    show: list[str] = Query(..., title="Filters", description="Fields to returns"),
    locations: list[str] = Query(None, title="Locations", description="Locations to search"),
    departments: list[str] = Query(None, title="Departments", description="Departments to search"),
    positions: list[str] = Query(None, title="Positions", description="Positions to search"),
    db: AsyncSession = Depends(get_session),
):
    filters = {}
    if locations:
        filters["location"] = locations.split(",")
    if departments:
        filters["department"] = departments.split(",")
    if positions:
        filters["position"] = positions.split(",")
    query = await EmployeeCrud.get_employees(db, page, limit, filters)
    return [row for row in query.scalars()]


@router.get("/org-setting")
async def get_org_setting():
    """Get organization setting
    return settings for fields to show in search result
    """
    return {"show": ["location", "department", "position"]}
