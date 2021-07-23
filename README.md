```shell
curl 'http://127.0.0.1:8000/api/v1/rates/'


curl --request POST 'http://127.0.0.1:8000/api/v1/rates/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "currency": 1,
    "source": 2,
    "buy": "30",
    "sale": "31"
}'


curl --request GET 'http://127.0.0.1:8000/api/v1/rates/4/'

curl --request DELETE 'http://127.0.0.1:8000/api/v1/rates/4/'

curl --request PUT 'http://127.0.0.1:8000/api/v1/rates/4/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "currency": 1,
    "source": 2,
    "buy": "130",
    "sale": "31"
}'

curl --request PATCH 'http://127.0.0.1:8000/api/v1/rates/4/' \
--data-raw '{
    "source": 1
}'

```