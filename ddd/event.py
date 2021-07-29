# (C) Copyright Juan Gomez Mosquera 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from datetime import datetime
from abc import ABC


class EventBase(ABC):
    """
    Event basle class
    """

    def __init__(
        self,
        name: str,
        data: bytes,
        version: str = "1",
        date: datetime = None,
        origin: str = None,
    ):
        self.name = name
        self.version = version
        self.date = datetime.now() if date is None else date
        self.origin = origin
        self.data = data