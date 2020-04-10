source ./curl_util.sh

# Test valid key
url="http://$host_name:$port_number/properties/1"
print_test_info_line "DELETE" "$url"

curl_http "DELETE" "$url" "Api-Key: cs4783FTW" ""
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi
check_resp "./test_resps/property_deleted.json"

if [ $? -ne 0 ]; then
	echo "File doesn't match expected output"
	exit 1
fi

# Test missing key
print_test_info_line "DELETE" "$url"
curl_http "DELETE" "$url" "" ""

if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi

check_resp "./test_resps/missing_key.json"
exit $?
