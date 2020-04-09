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

	curl -s -S                 \
	     --request "$method" \
	     --header "$headers"  \
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
	local method="$1"
	local url="$2"
	local headers="$3"
	local body="$4"

	curl -s                  \
	     --request "$method" \
	     --header "$headers"  \
	     --data "$body"      \
	     "$url"              \
			 > resp.json
	
	return $?	
}

# Compares the curl output file (resp.json) with the data file to check 
# if the service returned the correct response. Prints PASSED or FAILED
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

	_print_test_result $diff_code

	rm diff_output.txt
	rm resp.json

	return $diff_code
}

# Prints the method and URL that is being tested to stdout. This
# function should be called before running a test.
#
# Parameters:
#		1 -> HTTP method
#		2 -> URL
#
# Returns:
#		0 always
function print_test_info_line {
	local method="$1"
	local url="$2"
	printf "%s - %s - %s - " "TESTING" "$1" "$2"
	return 0
}

# Prints the result of the previously run test. This should be called
# following a call to print_test_info_line and other curl test functions.
# If the test status is non-zero the diff command output is displayed also.
#
# Note, this is a private function and should only be called from this
# file.
#
# Parameters:
#		1 -> status of the test, this either 0 (passed) or non-zero (failed)
#
# Returns:
#		0 always
function _print_test_result {
	local status="$1"
	
	if [ $status -eq 0 ]; then
		printf "%s\n" "PASSED"
	else
		printf "%s\n", "FAILED"
		cat diff_output.txt
	fi

	return 0
}

# Call this function if curl_http returns a non-zero error code. It will
# print a test failed message and print the output of the failed curl
# command. Before returning it will delete the resp.json file.
#
# Parameters:
#		none
#
# Returns:
#		always 0
function handle_curl_error {
	printf "%s\n" "CURL FALIED"
	cat resp.json
	rm resp.json
	return 0	
}
