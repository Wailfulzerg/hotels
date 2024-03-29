from fastapi import APIRouter

router = APIRouter(tags=["Healthcheck"], include_in_schema=False)


@router.get("/health")
async def healthcheck():
    return "Healthcheck\n"


ROUTERS = (router,)
