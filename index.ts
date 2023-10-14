

const underdogApiEndpoint = "https://devnet.underdogprotocol.com";

const config = {
    headers: { Authorization: `Bearer 580ece025159d3.cc3470ddf5b44f71b65d735b08368e5d` }
};

const projectId = 2


const nftData = { 
  "name": "Tweet", 
  "symbol": "ALPHA", 
  "image": "https://shdw-drive.genesysgo.net/2bJMeJk5a3Nu9xJvFBitvzUxRC9ZLCx7NhNeP8FRbPZ6/1708213929246154785.png",
  "receiver": {
    "identifier": "7VKZueH6v6xqnR5Z8LzsKE6BQuP9SUoHcJaALUwtY2QB"
  }
};

const createNftResponse = await axios.post(
  `${underdogApiEndpoint}/v2/projects/${projectId}/nfts`, 
  nftData,
  config,
);