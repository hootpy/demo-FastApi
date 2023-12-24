import time

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import Response

from app.common.depends.get_redis_session import get_redis


class Throttle:
    def __init__(self, max_requests: int, period: int):
        self.max_requests = max_requests
        self.period = period
        self.redis = get_redis()

    async def __call__(self, request: Request, response: Response):
        ip = request.client.host
        key = f"throttle:{ip}"

        data = self.redis.get(key)
        if data:
            last_request, count = data.split(",")
            last_request = float(last_request)
            count = int(count)
        else:
            last_request = 0
            count = 0

        now = time.time()
        if now - last_request > self.period:
            count = 0

        count += 1
        self.redis.set(key, f"{now},{count}")
        self.redis.expire(key, self.period)

        if count > self.max_requests:
            raise HTTPException(status_code=429, detail="Too many requests. Please try again later.")
