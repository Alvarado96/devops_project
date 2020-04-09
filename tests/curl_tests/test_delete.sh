source ./curl_util.sh

print_test_info_line "DELETE" "http://$host_name:$port_number/properties/[ID]"

curl_http "DELETE" "$url" "cs4783FTW" ""
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi
check_resp "./tests/curl_tests/test_resps/property_deleted.json"

if [ $? -ne 0 ]; then
	exit 1
fi

print_test_info_line "DELETE" "http://$host_name:$port_number/properties/[ID]"

curl_https "DELETE" "$url" "cs4783FTW" ""
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi

check_resp "./test_resps/property_deleted.json"

exit $?
