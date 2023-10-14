import bs58 from 'bs58'
import nacl from 'tweetnacl'
import crypto from 'crypto'

// Assuming that the storage account and keypair are relevant for list-objects as well

const SHDW_DRIVE_ENDPOINT = "https://shadow-storage.genesysgo.net"
const storageAccount = "HU3zrq5EcJFbRTgjhguUpT7A2MJSQbChBc8ChePtn5xy"
keypair = "[252,180,204,63,202,6,22,10,52,198,133,240,244,119,27,86,121,52,232,246,149,101,166,89,62,73,236,6,90,167,105,161,96,103,96,223,85,10,135,116,2,58,184,203,178,19,90,23,153,11,79,64,3,180,72,215,25,117,182,119,165,169,150,108]"

// Construct the message to sign - adjust as necessary based on the requirements for list-objects
const msg = `Shadow Drive Signed Message:\nStorage Account: ${storageAccount}`;

// Encode the message
const encodedMessage = new TextEncoder().encode(msg);

// Sign the message
const signedMessage = nacl.sign.detached(encodedMessage, keypair.secretKey);

// Convert the signed message to a bs58-encoded string
const signature = bs58.encode(signedMessage);

// Construct the request payload
const payload = {
    signer: keypair.publicKey.toString(),
    storage_account: storageAccount.toString(),
    message: signature
};

// Make the request to the list-objects endpoint
const response = await fetch(`${SHDW_DRIVE_ENDPOINT}/list-objects`, {
    method: "POST",
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
});

// Handle the response
if (response.ok) {
    const data = await response.json();
    console.log(data);
} else {
    console.error("Error fetching objects:", await response.text());
}
