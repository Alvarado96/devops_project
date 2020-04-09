# Tests the GET all properties endpoint: /properties
source ./curl_util.sh

url="http://$host_name:$port_number/properties"
print_test_info_line "GET" "$url"

curl_http "GET" "$url" "" ""
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi
check_resp "get_all_data.json" # TODO
exit $?
