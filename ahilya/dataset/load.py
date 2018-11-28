import subprocess
for i in range(1,100):
	fname = "@"+str(i)+".json"
	subprocess.call(["curl", "-H", '"Content-Type: application/x-ndjson"', "-XPOST", 'https://search-simple-es-2ji7mlt4mv42eh5jk6bcrdmux4.us-east-1.es.amazonaws.com/sample/index/_bulk?pretty', "--data-binary", fname], shell=False)