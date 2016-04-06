from os.path import dirname, realpath, join
ROOT_FOLDER = join(dirname(realpath(dirname('__file__'))), '')
INCLUDES = "include"
DATA_DIR_NAME = "data"


DIR_NOC_LIST = '/noc'
DIR_SCEALEXTRIC_LIST = '/scealextric'


DATA_NOC_VEALE_LISTS = ROOT_FOLDER + DATA_DIR_NAME + DIR_NOC_LIST + '/Veale_NOC_List'
DATA_NOC_TSV_LISTS = ROOT_FOLDER + DATA_DIR_NAME + DIR_NOC_LIST + '/tsv_lists'

DATA_SCEALEXTRIC_LISTS = ROOT_FOLDER + DATA_DIR_NAME + DIR_SCEALEXTRIC_LIST



# EDIT THIS PART APPROPRIATE ACCORDING TO ABOVE STRUCTURE

# NOC_LIST_FILEPATH = "Veale's The NOC List.xlsx"
# SCRIPT_MIDPOINTS_FILEPATH = "Veale's script midpoints.xlsx"
# INITIAL_BOOKENDS_FILEPATH = "Veale's initial bookend actions.xlsx"
# CLOSING_BOOKENDS_FILEPATH = "Veale's closing bookend actions.xlsx"
