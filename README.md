# ethdash
Ethereum Dashboard CLI


To spin up a brand new ethereum node and ethdash server, make sure you have a fast drive with lots (~80GB+) of empty space and a good internet connection, then run:

`docker-compose up -d`

If you already have a running parity (or geth)** node:
`export WEB3_PROVIDER_URI=<json-rpc addess>` (e.g. http://localhost:8545) for http or ws connections

or

`export EXISTING_PARITY_BASE_PATH=<ipc directory>` for ipc connection (parity only). This is the path where jsonrpc.ipc is, by default ~/.local/share/io.parity.ethereum

Then you only need to run the server:
`docker-compose up -d ethdash`

To see some live ethereum blockchain stats:
`docker-compose logs --tail=10 -f ethdash`