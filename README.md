# DRF Test

## How to Install
Build services and launch containers 
```bash
docker-compose up --build -d
```
Create superuser
```bash
docker exec -it drf-test-task-backend-1 python manage.py createsuperuser
```
Then login admin http://0.0.0.0:8000/admin (api accepts only authorized users)

Test drf url located at http://0.0.0.0:8000/api/entities/

Content example to post:
```json
{
    "value": 11,
    "properties": [{"key":"foo", "value":"bar"}, {"key":"foo1", "value":"bar2"}]
}
```
## Docs: 
- http://0.0.0.0:8000/api/redoc/
- http://0.0.0.0:8000/api/schema/
- http://0.0.0.0:8000/api/docs/
    