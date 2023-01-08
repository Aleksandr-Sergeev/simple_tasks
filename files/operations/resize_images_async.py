from ..classes import ImagesResizer


def resize_images(source: str, resize_percent: str, do_async: bool) -> None:
    images_resizer = ImagesResizer(source=source,
                                   resize_percent=resize_percent,
                                   do_async=do_async)
    images_resizer.resize_images()




############################
############################
"""Рабочая версия"""

# import aiofiles as aiofiles
# from PIL import Image
# from pathlib import Path
# import os
# from ..exceptions import FileManagementException
# from ..exception_codes import FileManagementExceptionCodes
# import asyncio
# from io import BytesIO
# from ..utils import timeit
# from ..enums import SupportedImageTypes
#
#
# @timeit
# def resize_images_async(source: str, resize_percent) -> None:
#     path_to_files = get_path_to_files(source)
#     images_to_process = get_images_to_process(path_to_files)
#     # process_images(images_to_process, int(resize_percent))
#     asyncio.get_event_loop().run_until_complete(process_images(images_to_process, resize_percent))
#
#
# def get_path_to_files(source: str) -> Path:
#     path_to_files = Path(source)
#     if not path_to_files.exists():
#         raise FileManagementException(source, message=FileManagementExceptionCodes.PATH_NOT_EXIST.value)
#     # elif not path_to_files.is_dir():
#     #     raise FileManagementException(source, message=FileManagementExceptionCodes.PATH_NOT_DIR.value)
#     return path_to_files
#
#
# def get_images_to_process(directory: Path) -> list[Path]:
#     files_to_process_list = []
#     supported_image_types = tuple(i.value for i in SupportedImageTypes.__members__.values())
#     if directory.is_file() and check_if_supported_image_type(directory.name, supported_image_types):
#         files_to_process_list.append(directory)
#     else:
#         files_to_process_list = [image_path for image_path in directory.iterdir() if image_path.is_file()
#                                  and check_if_supported_image_type(image_path.name, supported_image_types)]
#     if len(files_to_process_list) == 0:
#         raise FileManagementException(directory.name, message=FileManagementExceptionCodes.FILE_WRONG_TYPE.value)
#     return files_to_process_list
#
#
# def check_if_supported_image_type(file_name: str, supported_image_types: tuple):
#     return True if file_name.lower().endswith(supported_image_types) else False
#
#
# async def process_images(paths_list, resize_percent):
#     tasks = []
#     resize_percent = int(resize_percent)
#     for file_path in paths_list:
#         with Image.open(file_path) as image:
#             w, h = image.size
#             w, h = int(w * resize_percent / 100), int(h * resize_percent / 100)
#             resized_image = image.resize((w, h), Image.ANTIALIAS)
#             target_folder = Path(file_path.parent, "resized")
#             if not target_folder.exists():
#                 target_folder.mkdir(parents=True, exist_ok=True)
#             elif not target_folder.is_dir():
#                 raise FileManagementException(target_folder.name,
#                                               message=FileManagementExceptionCodes.TARGET_PATH_BROKEN.value)
#             buffer = BytesIO()
#             resized_image.save(buffer, format="JPEG")
#             target = os.path.join(target_folder.__str__(), file_path.name)
#             task = asyncio.ensure_future(save_image(buffer.getbuffer(), target))
#             tasks.append(task)
#     await asyncio.gather(*tasks, return_exceptions=True)
#
#
# async def save_image(image: memoryview, target: str):
#     async with aiofiles.open(target, "wb") as open_file:
#         await open_file.write(image)
#         await open_file.flush()
