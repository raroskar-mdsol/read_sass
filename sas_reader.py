from sas7bdat import SAS7BDAT
import uuid
import itertools

def get_dataset_metadata(filename, study_uuid):
    f = SAS7BDAT(filename)

    column_names = f.column_names
    column_types = f.column_types

    file_metadata = {}
    file_metadata["fields"] = []

    file_metadata["study_uuid"] = study_uuid
    file_metadata["dataset_uuid"] = uuid.uuid4().urn.split(':')[2]#"dataset_uuid_"+os.path.splitext(f.properties.filename)[0]
    file_metadata["dataset_name"] = f.properties.filename
    file_metadata["dataset_no_of_fields"] = f.properties.column_count
    file_metadata["dataset_no_of_rows"] = f.properties.row_count
    file_metadata["dataset_updated_at"] = str(f.properties.date_modified)

    for inx, val in enumerate(column_names):
        column_info = {}
        column_info["type"] = column_types[inx]
        column_info["name"] = val
        file_metadata["fields"].append(column_info)

    file_data = []
    for row in itertools.islice(f, 1, None):
        obj = {}
        obj["study_uuid"] = file_metadata["study_uuid"]
        obj["dataset_uuid"] = file_metadata["dataset_uuid"]
        for inx, val in enumerate(column_names):
            obj[val] = str(row[inx])
        file_data.append(obj)

    return [file_metadata, file_data]