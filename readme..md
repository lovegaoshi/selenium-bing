sudo docker build -t bing-rewards .
sudo docker run --rm -it -p 4444:4444 -p 5900:5900 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:dev

http://localhost:7900/?autoconnect=1&resize=scale&password=secret