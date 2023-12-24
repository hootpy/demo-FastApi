from fastapi import APIRouter

from app.common.utils.version import get_project_version

router = APIRouter()


@router.get("/health")
async def health_check() -> dict[str, str]:
    """
    The endpoint to check the health of the application

    :return: Version of the application
    """
    version = get_project_version()
    return {"version": version}
