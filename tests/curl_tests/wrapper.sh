# Runs as part of the pipeline. Start the service locally runs the curl tests
# and kills the server
echo "Starting curl tests..."
python3 ../../main.py localhost 12188 &
servicePID=$!
#bash test_driver.py
echo "exit 1" > a.sh
bash a.sh
test_result=$?
kill -9 $servicePID
echo "Service shut down, ending stage..."
exit $test_result
