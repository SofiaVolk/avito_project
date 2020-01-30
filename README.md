# avito_project
JSON API for ad site on Flask + flask-SQLAlchemy + PostgreSQL

### Clone repo and run 
```
git clone https://github.com/SofiaVolk/avito_project.git
```
```
cd avito_project
```
```
docker-compose build
```
```
docker-compose up
```

### Test
**1. create ad**
  - correct requests
```
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"name": "myFirst", "price":"56780", "photos":["http://ph1.jpeg"], "description":"blabla"}'\
    http://0.0.0.0:5000/ad
    
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"name": "mySecond", "price":"123123", "photos":["http://p2.jpeg", "http://p33.jpeg"], "description":"blabla"}'\
    http://0.0.0.0:5000/ad
```

  - incorrect data requests *(photos > 3 (or name > 200 symbols or description > 1000 symbols))*
```
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"name": "myFirstd", "price":"56780", "photos":["ph1.jpeg", "ph2.jpeg", "ph3.jpeg", "ph4.jpeg"], "description":"blabla"}'\
 http://0.0.0.0:5000/ad
```

**2. get ad by id**
  - correct request *(id = 2)*
```
curl -X GET  http://0.0.0.0:5000/ad/2
```
   or *(for full info)*
```
curl -X GET  http://0.0.0.0:5000/ad/2?fields=True
```

  - incorrect param requests
```
curl -X GET  http://0.0.0.0:5000/ad/a
```
   or
```
curl -X GET  http://0.0.0.0:5000/ad
```

**3. get list of ads**
  - correct request *(first page, 10 per page)*
```
curl -X GET  http://0.0.0.0:5000/ads
```
  or *(page number = 2)*
```
curl -X GET  http://0.0.0.0:5000/ads/2
```
  or *(sort_by date|price order_by desc|asc)*
```
curl -X GET  http://0.0.0.0:5000/ads?sort_by=price\&order_by=asc
```






