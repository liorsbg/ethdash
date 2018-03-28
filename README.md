# EthDash

### TLDR

```sh
docker-compose build ethdash
WEB3_PROVIDER_URI=http://ethdash.pw:58545 docker-compose up ethdash
```

#### Run a new node

To spin up a brand new ethereum node and ethdash server, make sure you have a fast drive with lots (~80GB+) of empty space and a good internet connection, then run:

`docker-compose up -d`

#### Connect to a running parity node

for http or ws connections (e.g. http://localhost:8545) :

`export WEB3_PROVIDER_URI=<json-rpc addess>` 

for ipc connection:

`export EXISTING_PARITY_BASE_PATH=<ipc directory>` 

the default is  ~/.local/share/io.parity.ethereum

Then you only need to run the server:

`docker-compose up -d ethdash`



Then, to see some live ethereum blockchain stats:

`docker-compose logs --tail=10 -f ethdash`
