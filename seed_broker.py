__author__ = 'edill'

from metadataStore.userapi.commands import log, create
import datetime
from os import listdir

run_header_id = 1987
owner="edill"

sample_dict = {
    'header': {
        'run_id': run_header_id,
        'run_owner': owner,
        'beamline_id': 'csx',
        'custom': {},
        'start_time': datetime.datetime.utcnow()
    },
    'beamline_config': {
        'beamline_config_id': 122,
        'header_id': run_header_id,
        'wavelength': .64639,
        'custom': {
            'new_field': 'value'
        }
    },
}

calib =  {
    'synchrotron' : "nsls1",
    'date' : 'Feb 2007',
    "calibrant" : "LaB6",
    "notes" : "x6b",
    "x0" : 927.485,
    "y0" : 1002.781,
    "distance" : 215.454,
    "wavelength" : 0.64613,
    "pixel_size" : 80,
}

log_calib = {
    "text" : "Log the calibration",
    "owner" : owner,
    "event_id" : 1,
    "run_id" : 0,
    "event_type_id" : 100,
    "header_id" : run_header_id,
    "seqno" : 0,
    "data" : {
        "calib" : calib,
        },
}


def create_new_entry():
    create(sample_dict)


def log_frames(frames_list):
    log_frames = {
        "text" : "Log the frames",
        "owner" : owner,
        "event_id" : 0,
        "run_id" : 0,
        "event_type_id" : 101,
        "header_id" : run_header_id,
        "seqno" : 0,
        "data" : {
            "image_files" : frames_list,
            },
    }

    return log_frames

if __name__ == "__main__":
    folder_path = "/home/edill/Data/bnl_feb_07/250-80-1"
    files = []
    for file in listdir(folder_path):
        files.append(folder_path + "/" + file)
    # create a new entry into the data broker
    create(sample_dict)

    # log the frames
    log(**log_frames(files))

    # log the calibration
    log(**log_calib)

