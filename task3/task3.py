import json
def check(data: dict, values: list[dict]):
	if "values" in data.keys():
		for nest in data["values"]:
			check(nest, values)
	for v in values["values"]:
		if data["id"] == v["id"]:
			data["value"] = v["value"]
file = open("result.json", 'w')
values = json.loads(open("values.json", 'r').read())
with open("tests.json", 'r') as tests:
	data_tests = json.loads(tests.read())
	for i in data_tests["tests"]:
		check(i, values)
file.write(str(data_tests))