"""
⚠️ Disclaimer ⚠️

This project is an educational toy and is intended for
basic concepts and experiments. It is not intended
for use in a production environment and does not require
the necessary level of security, performance,
or fault tolerance.

Use this code at your own risk. For your
projects, it is recommended to rely on proven
Frameworks and libraries.
"""

import os
import importlib.util as libutil
from fastapi import FastAPI, APIRouter


class Pathify():
    def __init__(self, routers_dir: str = "routers") -> None:
        """
        Initializing the Pathify class.

        :param routers_dir: Directory where routers are stored
        """
        self.app = FastAPI()
        self.router = APIRouter()
        self.routers_dir = routers_dir
        self.load_routes()
        self.app.include_router(self.router)

    def process_dynamic_path(self, path: str) -> str:
        """
        Converts a path with parameters in [param] format to FastAPI format.
        :param path: Path from the file structure.
        :return: Converted path compatible with FastAPI.
        """
        return path.replace("[", "{").replace("]", "}")

    def load_routes(self) -> None:
        """
        Dynamically loads routes from the specified directory and adds them to the FastAPI application.
        """
        for root, dirs, files in os.walk(self.routers_dir):
            relative_path = os.path.relpath(root, self.routers_dir).replace("\\", "/")

            if relative_path == ".":
                url_path = "/"
            else:
                dynamic_url_path = self.process_dynamic_path(relative_path)
                url_path = "" if dynamic_url_path == "." else f"/{dynamic_url_path}"

            for file in files:
                if file.endswith(".py"):
                    module_name = file[:-3]
                    file_path = os.path.join(root, file)
                    spec = libutil.spec_from_file_location(module_name, file_path)
                    if spec is not None:
                        module = libutil.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        if url_path:
                            if hasattr(module, "get"):
                                self.router.get(url_path)(module.get)
                            if hasattr(module, "post"):
                                self.router.post(url_path)(module.post)
                        else:
                            raise ImportError(f"Failed to load module: {module_name}")
                    else:
                        raise ImportError(f"Failed to load module: {module_name}")
    def get_app(self):
        """
        Returns an instance of FastAPI application.
        """
        return self.app
