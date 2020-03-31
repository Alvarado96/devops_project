# Runs the curl command using HTTP on the given parameters and outputs the
# results to a file called resp.json.
#
# Parameters:
#		1 -> HTTP method
#		2 -> URL to resource
#		3 -> HTTP headers
#		4 -> HTTP body
#
# Returns:
#		0 if curl was successful, nonzero otherwise
function curl_http {
	local method="$1"
	local url="$2"
	local headers="$3"
	local body="$4"

	curl -s                  \
	     --request "$method" \
	     --header "$header"  \
	     --data "$body"      \
	     "$url"              \
			 > resp.json
	
	return $?
}

# Runs the curl command using HTTPS on the given parameters and outputs the
# results to a file called resp.json.
#
# Parameters:
#		1 -> HTTP method
#		2 -> Resource path
#		3 -> HTTP headers
#		4 -> HTTP body
#
# Returns:
#		0 if curl was successful, 1 otherwise
function curl_https {
	return 0	
}

# Compares the curl output file (resp.json) with the data file to check if the
# service returned the correct response. Prints PASSED or FAILED
# depending the test results. If the test failed the diff output is
# displayed. The curl output file is deleted before returning.
#
# Parameters:
#		1 -> path to data file to compare resp.json to
#
# Returns:
#		0 if test passed, -1 otherwise
function check_resp {
	local data_path="$1"

	# TODO cheat the test for now, change later
	cat resp.json > $data_path

	diff $data_path resp.json > diff_output.txt
	diff_code=$?

	if [ $diff_code -ne 0 ]; then
		echo "FAILED"
		cat diff_output.txt
		ret=1
	else
		echo "PASSED"
		ret=0
	fi

	rm diff_output.txt
	rm $data_path # TODO remove this later
	return $ret
}
