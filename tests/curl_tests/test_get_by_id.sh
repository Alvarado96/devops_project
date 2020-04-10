# Tests the GET by id properties endpoint: /properties/<string:id>
source ./curl_util.sh

url="http://$host_name:$port_number/properties/1"
print_test_info_line "GET" "$url"

curl_http "GET" "$url" "" ""
if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi
check_resp "./test_resps/1.json"

if [ $? -ne 0 ]; then
	echo "File doesn't match expected output in 1.json"
	exit 1
fi

# Test for expected output with an invalid id

url="http://$host_name:$port_number/properties/50"
print_test_info_line "GET" "$url"

curl_http "GET" "$url" "" ""

if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi

check_resp "./test_resps/id_not_found.json"

if [ $? -ne 0 ]; then
	echo "File doesn't match expected output in id_not_found.json"
	exit 1
fi

# Test for expected output with id not an integer

url="http://$host_name:$port_number/properties/July"
print_test_info_line "GET" "$url"

curl_http "GET" "$url" "" ""

if [ $? -ne 0 ]; then
	handle_curl_error
	exit 1
fi

check_resp "./test_resps/id_not_int.json"
exit $?
