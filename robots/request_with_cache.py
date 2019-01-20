import requests as req
from cachecontrol import CacheControl

session = req.Session()

cached_session = CacheControl(session)

res = cached_session.get('https://docs.python.org/3/')
print(res.from_cache)

res = cached_session.get('https://docs.python.org/3/')
print(res.from_cache)
