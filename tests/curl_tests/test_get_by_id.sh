# Tests the GET by id properties endpoint: /properties/<string:id>
source ./curl_util.sh

url="http://$host_name:$port_number/properties/1"
print_test_info_line "GET" "$url"

curl_http "GET" "$url" "" ""
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi

check_resp "get_by_id_data.json" # TODO
if [ $? -ne 0 ]; then
	exit 1
fi

# https test
url="https://$host_name:$port_number/properties/1"
print_test_info_line "GET" "$url"

curl_https "GET" "$url" "" ""
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi

check_resp "get_by_id_data.json" # TODO
exit $?