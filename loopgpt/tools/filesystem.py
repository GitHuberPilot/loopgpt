from loopgpt.tools.base_tool import BaseTool
import os


class ReadFromFile(BaseTool):
    @property
    def args(self):
        return {"file": "Path to the file to read."}

    @property
    def resp(self):
        return {
            "content": "Contents of the file. If the file doesn't exist, this field will be empty."
        }

    def run(self, file):
        try:
            with open(file, "r") as f:
                return {"content": f.read()}
        except Exception:
            return {"content": ""}


class WriteToFile(BaseTool):
    @property
    def args(self):
        return {
            "file": "Path of the file to write to.",
            "content": "Content to be written to the file.",
        }

    @property
    def resp(self):
        return {"success": "true or false"}

    def run(self, file, content):
        with open(file, "w") as f:
            f.write(content)
        return {"success": True}


class AppendToFile(BaseTool):
    @property
    def args(self):
        return {
            "file": "Path of the file to append to.",
            "content": "Content to be appended to the file.",
        }

    @property
    def resp(self):
        return {"success": "true or false"}

    def run(self, file, content):
        with open(file, "a") as f:
            f.write(content)
        return {"success": True}


class DeleteFile(BaseTool):
    @property
    def args(self):
        return {"file": "Path to the file to be deleted"}

    @property
    def resp(self):
        return {"success": "true if the file was successfully deleted. Else false."}

    def run(self, file):
        try:
            os.remove(file)
            return {"success": True}
        except Exception:
            return {"success": False}


class CheckIfFileExists(BaseTool):
    @property
    def args(self):
        return {"file": "Path to the check if file exists."}

    @property
    def resp(self):
        return {"exists": "true if the file exists, else false."}

    def run(self, file):
        return {"exists": os.path.isfile(file)}


FileSystemTools = [
    ReadFromFile,
    WriteToFile,
    AppendToFile,
    DeleteFile,
    CheckIfFileExists,
]
