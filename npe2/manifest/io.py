from typing import List, Optional

from pydantic import BaseModel, Field

from .._types import ReaderFunction
from .utils import Executable


class ReaderContribution(BaseModel, Executable):
    command: str = Field(
        ..., description="Identifier of the command providing `napari_get_reader`."
    )
    filename_patterns: List[str] = Field(
        default_factory=list,
        description="List of filename patterns (for fnmatch) that this reader can "
        "accept. Reader will be tried only if `fnmatch(filename, pattern) == True`",
    )
    accepts_directories: bool = Field(
        False, description="Whether this reader accepts directories"
    )

    def exec(self, args: tuple = (), kwargs: dict = {}) -> Optional[ReaderFunction]:
        from .._command_registry import execute_command

        return execute_command(self.command, args, kwargs)
