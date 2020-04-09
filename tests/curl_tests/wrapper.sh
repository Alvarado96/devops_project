# Runs as part of the pipeline. Start the service locally runs the curl tests
# and kills the server
echo "Starting curl tests..."
python3 ../../main.py -p 12188 &
servicePID=$!
bash tests/curl_tests/test_driver.sh localhost 12188
test_result=$?
kill -9 $servicePID
echo "Service shut down, ending stage..."
exit $test_result
