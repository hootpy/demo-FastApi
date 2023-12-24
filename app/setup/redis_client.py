import redis

from app.setup.setting import SETTING


def create_redis():
    return redis.ConnectionPool(host=SETTING.REDIS_HOST, port=SETTING.REDIS_PORT, db=0, decode_responses=True)


pool = create_redis()
