import http.client

# IMDSv2 Address
IMDS_ADDRESS = "169.254.169.254"

# Header for requesting token
AWS_REQ_TOKEN_HEADER = {
    "X-aws-ec2-metadata-token-ttl-seconds": 21600,
}

# To keep myself sane and not repeating this
def req(method, address, path, headers):
    conn = http.client.HTTPConnection(address)
    conn.request(method, path, headers=headers)
    res = conn.getresponse()
    body = res.read()
    return body

# Get token, otherwise IMDS will spit 401 Unauthorized
# For more details, see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
def getToken():
    return req("PUT", IMDS_ADDRESS, "/latest/api/token", AWS_REQ_TOKEN_HEADER)

# Header for subsequent requests
def assembleReqHeader():
    return {
        "X-aws-ec2-metadata-token": getToken()
    }

# Request instance ID from IMDS
def getInstanceID():
    return req("GET", IMDS_ADDRESS, "/latest/meta-data/instance-id", assembleReqHeader())

# Request instance local hostname from IMDS
def getInstanceLocalHostname():
    return req("GET", IMDS_ADDRESS, "/latest/meta-data/local-hostname", assembleReqHeader())

# Request instance local address from IMDS
def getInstanceLocalAddress():
    return req("GET", IMDS_ADDRESS, "/latest/meta-data/local-ipv4", assembleReqHeader())

# Request instance availability zone
def getInstanceAvailabilityZone():
    return req("GET", IMDS_ADDRESS, "/latest/meta-data/placement/availability-zone")