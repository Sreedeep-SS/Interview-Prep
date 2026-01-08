## Implement a Python + Celery + Redis task
### “How do retries work?” → Set retry=True 
### “What broker and result backend do you use?” → Usually Redis or RabbitMQ
Just practice implementing:

- Key → value pair

- Round robin assignment with INCR

- TTLs (Time-to-Live)



```python
from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery

# task
@celery.task
def send_email(to, subject):
    # send...
    return True
```