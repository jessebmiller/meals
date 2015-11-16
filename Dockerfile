from alpine

run apk update && apk add python py-pip
run pip install Flask

run mkdir /app

add app /app

cmd python app