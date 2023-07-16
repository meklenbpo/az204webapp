# MultiInstance WebApp

In order to gain some practical knowledge on Azure App Service, I want to set up a web application that will somehow provide an insight into app performance (i.e. measure CPU load, server response time or similar) then run it in different environments and compare the performance metrics.

## Develop App Requirements
The app will be a simple server with one endpoint that executes any expensive calculation and returns a singe (even dummy) value to the client.

## Develop "High"-Load Simulation
To test for high load we can setup a local client that will ping the server repetitively and measure the request turn-around time / requests per seconds. 
If required we can run it in parallel processes.

## Implement and test the App locally
- I have set up FastAPI / UvCorn server
- Server has just one endpoint and when hit with a request it executes an expensive computation:
	- compute a list of 10000 UUIDs and return the last one
- A local client is pinging the server and return last value and also computes RPS.

## Deploy the App to Azure (Different Tiers)
At this point the app doesn't work in Azure. I deployed it using Github Actions (as suggested in Azure Portal) while tutorial suggested Azure CLI or local git or zip file. Will need to try all of those methods to gain familiarity.

## Run the load tests and compare performance