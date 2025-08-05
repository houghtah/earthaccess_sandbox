# collection of functions for reading satellite data
#

import earthaccess
import os
import xarray as xr

def test_print():

    print(" Holy crap ... it worked!  Didn't it?!? ")


# general routine to open a data file
#
def open_data_file(ifile,level='L2',loc='cloud'):
    
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


def open_data(ifile):

    loc = 'local'
    typ = 'L2'
    
    if isinstance(ifile, list):
        if isinstance(ifile[0], earthaccess.results.DataGranule):
            loc = 'cloud'
            if 'L3' in ifile[0].data_links()[0]: level = 'L3'
    else:
        if 'L3' in ifile: level = 'L3'
            
    dataset = open_data_file(ifile,level=typ,loc=loc)

    return dataset



# Carina and Anna's routine to write an OCSSW parameter file
#
def write_par(path, par):
    """Prepare a parameter file to be read by one of the OCSSW tools.

    Using a parameter file (a.k.a. "par file") is equivalent to specifying
    parameters on the command line.

    Parameters
    ----------
    path
        where to write the parameter file
    par
        the parameter names and values included in the file

    Example
    -------
par = {
    "ifile": l1b_path,
    "ofile": data / l1b_name.replace("L1B", "L2"),
    "north": 39,
    "south": 35,
    "west": -76,
    "east": -74.5,
    "l2prod": "Rrs",
    "proc_uncertainty": 0,
}
write_par("l2gen.par", par)
        
    """
    with open(path, "w") as file:
        writer = csv.writer(file, delimiter="=")
        writer.writerows(par.items())


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