source ./curl_util.sh

url="http://$host_name:$port_number/properties"
print_test_info_line "POST" "$url"

curl_http "POST" "$url" "Api-Key: cs4783FTW" '{"address":"777 7th st", "city7":"testing7", "state":"TX", "zip":"77777"}'

if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi
check_resp "./test_resps/property_added.json"

if [ $? -ne 0 ]; then
	echo "File doesn't match expected output"
	exit 1
fi

# Test missing key
print_test_info_line "POST" "$url"
curl_http "POST" "$url" "" '{"address":"777 7th st", "city7":"testing7", "state":"TX", "zip":"77777"}'


if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi

check_resp "./test_resps/missing_key.json"
exit $?
