source ./curl_util.sh

print_test_info_line "PUT" "http://$host_name:$port_number/properties/[ID]"

url="http://$host_name:$port_number/properties/2"

curl_http "PUT" "$url" "Api-Key: cs4783FTW" "{'address':'testing2', 'city':'testing2',\
 												'state':'tt', 'zip': '22222'}"
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi
check_resp "./test_resps/property_updated.json"

if [ $? -ne 0 ]; then
	exit 1
fi

print_test_info_line "PUT" "http://$host_name:$port_number/properties/[ID]"

url="https://$host_name:$port_number/properties/2"

curl_https "PUT" "$url" "Api-Key: cs4783FTW" "{'address':'testing2', 'city':'testing2',\
 												'state':'tt', 'zip': '22222'}"
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi
check_resp "./test_resps/property_updated.json"
exit $?
