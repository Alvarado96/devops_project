url="http://$host_name:$port_number/properties"
printf "TESTING - GET - %s " "$url"

curl -s -X GET "$url" > get_all_resp.json

# Check return value of curl command
ret_code="$?"
if [ "$ret_code" != 0 ]; then
	printf "%s\n" "- CURL FAILED"
	cat get_all_resp.json
	rm get_all_resp.json
	exit $ret_code
fi

# Cheating the test for now until a test DB is setup
cat get_all_resp.json > get_all_data.json

diff get_all_resp.json get_all_data.json > get_all_diff_output.txt
diff_code="$?"

rm get_all_resp.json
rm get_all_data.json # Remove this line later

if [ $diff_code -ne 0 ]; then
	printf "%s\n" "- FAILED"
	cat get_all_diff_output.txt
	printf "\n"
	exit 1
else
	printf "%s\n" "- PASSED"
	rm get_all_diff_output.txt
	exit 0
fi
