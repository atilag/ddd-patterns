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
from ddd.event import EventBase


class InternalEvent(EventBase):
    """
    An internal event is an in-memory event that is happening within your current bounded context
    and triggered sometime during a transaction.
    It should be synchronous in order to avoid potential inconsitences.
    """

    def __init__(
        self, data, name, version="1", date: datetime = None, origin: str = None
    ):
        super(EventBase, self).__init__(
            name, data, version=version, date=date, origin=origin
        )