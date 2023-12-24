import redis

from app.setup.redis_client import pool


def get_redis():
    return redis.Redis(connection_pool=pool)
