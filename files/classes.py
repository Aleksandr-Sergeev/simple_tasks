import aiofiles as aiofiles
from PIL import Image
from pathlib import Path
from .exceptions import FileManagementException
from .exception_codes import FileManagementExceptionCodes
import asyncio
from io import BytesIO
from .utils import timeit
from .enums import SupportedImageTypes


class PathFinder(object):
    def __init__(self, **kwargs):
        self.source = kwargs.pop('source')
        self.path_to_files = self.get_path_to_files()

    def get_path_to_files(self) -> Path:
        path_to_files = Path(self.source)
        self._check_path_to_files(path_to_files)
        return path_to_files

    def _check_path_to_files(self, path_to_files: Path) -> None:
        if not path_to_files.exists():
            raise FileManagementException(self.source, message=FileManagementExceptionCodes.PATH_NOT_EXIST.value)
        # elif not path_to_files.is_dir():
        #     raise FileManagementException(source, message=FileManagementExceptionCodes.PATH_NOT_DIR.value)


class ImageChecker(PathFinder):
    def __init__(self, **kwargs):
        super(ImageChecker, self).__init__(**kwargs)
        self.supported_image_types = tuple(i.value for i in SupportedImageTypes.__members__.values())
        self.files_to_process_list = []

    def get_images_to_process(self) -> None:
        if self.path_to_files.is_file() and self._check_if_supported_image_type(self.path_to_files.name):
            self.files_to_process_list.append(self.path_to_files)
        else:
            self.files_to_process_list = [image_path for image_path in self.path_to_files.iterdir() if image_path.is_file()
                                     and self._check_if_supported_image_type(image_path.name)]
        if len(self.files_to_process_list) == 0:
            raise FileManagementException(self.path_to_files.name,
                                          message=FileManagementExceptionCodes.FILE_WRONG_TYPE.value)

    def _check_if_supported_image_type(self, file_name: str):
        return True if file_name.lower().endswith(self.supported_image_types) else False


class ImagesResizer(ImageChecker):
    def __init__(self, **kwargs):
        super(ImagesResizer, self).__init__(**kwargs)
        self.resize_percent = int(kwargs.pop('resize_percent'))
        self.do_async = kwargs.pop('do_async')

    @timeit
    def resize_images(self) -> None:
        self.get_path_to_files()
        self.get_images_to_process()
        # process_images(images_to_process, int(resize_percent))
        if self.do_async:
            asyncio.get_event_loop().run_until_complete(self.process_images_async())

    async def process_images_async(self):
        tasks = []
        for file_path in self.files_to_process_list:
            with Image.open(file_path) as image:

                # buffer = self._write_image_to_bytecode(image)
                w, h = image.size
                w, h = int(w * self.resize_percent / 100), int(h * self.resize_percent / 100)
                resized_image = image.resize((w, h), Image.ANTIALIAS)
                buffer = BytesIO()
                resized_image.save(buffer, format="JPEG")

                target_filepath = self.get_target_filepath(file_path)
                task = asyncio.ensure_future(self.save_image(buffer.getbuffer(), target_filepath))
                tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

    def _write_image_to_bytecode(self, image: Image):
        w, h = image.size
        w, h = int(w * self.resize_percent / 100), int(h * self.resize_percent / 100)
        resized_image = image.resize((w, h), Image.ANTIALIAS)
        buffer = BytesIO()
        resized_image.save(buffer, format="JPEG")
        return buffer

    @staticmethod
    def get_target_filepath(file_path: Path) -> Path:
        target_folder = Path(file_path.parent, "resized")
        if not target_folder.exists():
            target_folder.mkdir(parents=True, exist_ok=True)
        elif not target_folder.is_dir():
            raise FileManagementException(target_folder.name,
                                          message=FileManagementExceptionCodes.TARGET_PATH_BROKEN.value)
        return Path(target_folder.__str__(), file_path.name)

    async def save_image(self, image: memoryview, target: Path):
        async with aiofiles.open(target, "wb") as open_file:
            await open_file.write(image)
            await open_file.flush()
