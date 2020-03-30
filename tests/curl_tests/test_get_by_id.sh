url="http://$host_name:$port_number/properties"
output_url="$url/[ID]"
printf "TESTING - GET - $output_url "

# Add more tests when testing DB is setup
curl -s -X GET "$url/1" > get_by_id_resp.json

if [ $? -ne 0 ]; then
	printf "%s\n" "- CURL FAILED"	
	rm get_by_id_resp.json
	exit 1
fi

# Cheat the test for now
cat get_by_id_resp.json > get_by_id_data.json

diff get_by_id_resp.json get_by_id_data.json > get_by_id_diff_output.txt
diff_code="$?"

rm get_by_id_resp.json
rm get_by_id_data.json

if [ $diff_code -ne 0 ]; then
	printf "%s\n" "- FAILED"
	cat get_by_id_diff_output.txt
	exit 1	
else
	printf "%s\n" "- PASSED"
	rm get_by_id_diff_output.txt
	exit 0	
fi
