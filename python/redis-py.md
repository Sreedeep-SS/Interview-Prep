# Redis (redis-py)
```python
import redis
r = redis.Redis(host='redis', port=6379, db=0)
r.set('k', 'v', ex=60)
r.hset('user:1', 'name', 'Sree')
```