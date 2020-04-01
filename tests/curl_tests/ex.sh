# Example for how to use the functions in curl_util.sh

# So we can call the functions in curl_util.sh
source ./curl_util.sh

method="GET"
url="http://cs47832.fulgentcorp.com:12186/properties"

# Print the test info
print_test_info_line "GET" "$url"

# Calling with empty header and body
curl_http "$method" "$url" "" ""

# Get curl_http return value
if [ $? -ne 0 ]; then
	printf "$s\n" "curl_http FAILED"
	rm resp.json
	exit 0
fi

# Ignoring the return value, would normally check this to determine
# if the future tests should be run or not
check_resp "./res.json"

rm resp.json
exit 0
