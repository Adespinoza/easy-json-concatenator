import glob
import simplejson as json
glob_data = []
# Change 'filename'
for file in glob.glob('./filename-*.json'):
    with open(file) as json_file:
        data = json.load(json_file)

        i = 0
        while i < len(data):
            glob_data.append(data[i])
            i += 1

with open('./combinedFile.json', 'w') as f:
	json.dump(glob_data, f, indent=4)