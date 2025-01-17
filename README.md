windows 11
$env:STAGE="dev"
docker-compose -p Jed-Blog up --build

linux
STAGE=prod docker-compose up --build
