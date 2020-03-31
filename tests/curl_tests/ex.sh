# Example for how to use the functions in curl_util.sh

# So we can call the functions in curl_util.sh
source ./curl_util.sh

url="http://cs47832.fulgentcorp.com:12186/properties"

# Calling with empty header and body
curl_http "GET" "$url" "" ""

# Get curl_http return value
if [ $? -ne 0 ]; then
	echo "curl_http failed"
	rm resp.json
	exit 0
fi

check_resp "./res.json"
echo "check_resp return: $?"

rm resp.json
exit 0
