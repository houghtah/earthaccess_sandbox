# collection of functions for reading satellite data
#

import earthaccess
import xarray as xr

def test_print():

    print(" Holy crap ... it worked!  Didn't it?!? ")


# general routine to open a data file
#
def open_data(ifile,level='L2',loc='cloud'):
    
    if 'cloud' in loc:
        path = earthaccess.open(ifile)
        ifile = path[0]
        dataset = xr.open_dataset(ifile)
    else:
        dataset = xr.open_dataset(ifile)

    if 'L2' in level:
        datatree = xr.open_datatree(ifile)
        dataset = xr.merge(datatree.to_dict().values())

    return dataset


# functions to remind myself what data is available via earthaccess
#
def list_avail_oci():
    results = earthaccess.search_datasets(instrument="oci")
    for item in results:
        summary = item.summary()
        print(summary["short-name"])

def list_avail_harp2():
    results = earthaccess.search_datasets(instrument="harp2")
    for item in results:
        summary = item.summary()
        print(summary["short-name"])

def list_avail_spexone():
    results = earthaccess.search_datasets(instrument="spexone")
    for item in results:
        summary = item.summary()
        print(summary["short-name"])