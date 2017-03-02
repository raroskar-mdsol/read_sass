from sas7bdat import SAS7BDAT
import json
import os
import uuid
import itertools

def get_file_info(filename, study_uuid):
    f = SAS7BDAT(filename)

    column_names = f.column_names
    column_types = f.column_types

    file_metadata = {}
    file_metadata["fields"] = []

    file_metadata["study_uuid"] = study_uuid
    file_metadata["uuid"] = "dataset_uuid_"+os.path.splitext(f.properties.filename)[0] #uuid.uuid4().urn.split(':')[2]
    file_metadata["name"] = f.properties.filename
    file_metadata["number_of_fields"] = f.properties.column_count
    file_metadata["number_of_rows"] = f.properties.row_count
    file_metadata["last_updated_at"] = str(f.properties.date_modified)

    for inx, val in enumerate(column_names):
        column_info = {}
        column_info["type"] = column_types[inx]
        column_info["name"] = val
        file_metadata["fields"].append(column_info)

    file_data = []
    for row in itertools.islice(f, 1, None):
        obj = {}
        obj["dataset_uuid"] = file_metadata["uuid"]
        for inx, val in enumerate(column_names):
            obj[val] = str(row[inx])
        file_data.append(obj)

    return [file_metadata, file_data]

#with open('data.json', 'w') as outfile:
#    json.dump(file_data, outfile)

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
metadata = {}
metadata["datasets"] = []
data = {}
data["datasets"] = []
# rootdir = '/Users/raroskar/Downloads/sample_docs/'
rootdir = raw_input("Please enter absolute path for folder containing .sas7bdat files: ")
# for filename in os.listdir(rootdir):
#     if filename.endswith(".sas7bdat"):
#         print os.path.join(rootdir, filename)
#         file_metadata, file_data = get_file_info(os.path.join(rootdir, filename), 'my_sample_study_1')
#         metadata["datasets"].append(file_metadata)
#         data["datasets"].append(file_data)

print os.path.join(rootdir, "aede.sas7bdat")
file_metadata, file_data = get_file_info(os.path.join(rootdir, "aede.sas7bdat"), 'my_sample_study_1')
metadata["datasets"].append(file_metadata)
data["datasets"].append(file_data)

with open('metadata.json', 'w') as outfile:
    json.dump(metadata, outfile, indent=4)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)


