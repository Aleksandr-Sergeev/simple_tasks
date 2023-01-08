from enum import Enum


class FileManagementExceptionCodes(Enum):
    PATH_NOT_EXIST = "path_not_exist"
    PATH_NOT_DIR = "path_not_dir"
    PATH_IS_EMPTY = "path_is_empty"
    FILE_WRONG_TYPE = "file_wrong_type"
    TARGET_PATH_BROKEN = "target_path_broken"
