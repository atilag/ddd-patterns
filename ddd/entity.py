# (C) Copyright Juan Gomez Mosquera 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import uuid


class Entity:
    def __init__(self, id=None):
        # uuid4() is random UUID
        self._id = uuid.uuid4() if id is None else id

    @property
    def id(self):
        return str(self._id)

    def __eq__(self, rhs):
        if not isinstance(rhs, self.__class__):
            return False
        return self._id == rhs._id

    def __ne__(self, rhs):
        return not self.__eq__(rhs)
