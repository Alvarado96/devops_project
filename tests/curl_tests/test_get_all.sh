url="http://$host_name:$port_number/properties"
echo "TESTING - GET - $url"

curl -s -X GET "$url" > get_all_output.json

# Check return value of curl command
ret_code="$?"
if [ "$ret_code" != 0 ]; then
	echo "CURL FAILED..."
	cat get_all_output.json
	rm get_all_output.json
	exit $ret_code
fi

cat get_all_output.json
rm get_all_output.json

echo ""
exit 0
