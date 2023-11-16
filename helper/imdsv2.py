import http.client

IMDS_ADDRESS = "169.254.169.254"

AWS_REQ_TOKEN_HEADER = {
    "X-aws-ec2-metadata-token-ttl-seconds": 21600,
}

def req(method, address, path, headers):
    conn = http.client.HTTPConnection(address)
    conn.request(method, path, headers=headers)
    res = conn.getresponse()
    body = res.read()
    return body

def getToken():
    return req("PUT", IMDS_ADDRESS, "/latest/api/token", AWS_REQ_TOKEN_HEADER)

def assembleReqHeader():
    return {
        "X-aws-ec2-metadata-token": getToken()
    }

def getInstanceID():
    return req("GET", IMDS_ADDRESS, "/latest/meta-data/instance-id", assembleReqHeader())

def getInstanceHostname():
    return req("GET", IMDS_ADDRESS, "/latest/meta-data/local-hostname", assembleReqHeader())