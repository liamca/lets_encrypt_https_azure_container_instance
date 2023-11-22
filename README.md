# How to Create an HTTPS Certificate for Azure Container Instance using Let's Encrypt

certbot certonly --manual -d <DOMAIN_NAME>.westus2.azurecontainer.io


http://<DOMAIN_NAME>.westus2.azurecontainer.io/save_challenge/<CHALLENGE_RESPONSE_STRING>


http://<DOMAIN_NAME>.westus2.azurecontainer.io/.well-known/acme-challenge/test
