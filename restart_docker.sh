docker stop bealstreasure-app
docker rm bealstreasure-app

docker run --name bealstreasure-app -p 8000:8000 -d bealstreasure