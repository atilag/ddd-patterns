# (C) Copyright Juan Gomez Mosquera 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import threading
from contextlib import ContextDecorator
from typing import Callable
from collections import defaultdict
from ddd.internal_event import InternalEvent


class InternalDomainEvents(ContextDecorator):
    """
    An in-memory Internal domain events interface to use within Contexts.

    We are using a context manager so we don't have to worry about cleaning the state
    after the transaction has finished, because internal domain events should only be
    valid withing the lifetime of a transaction.
    """

    # By using an instance per thread we make sure this will work in possible concurrent
    # scenarios
    local_storage = threading.local()

    def __enter__(self):
        if not hasattr(self.local_storage, "event_and_callback"):
            self.local_storage.event_and_callback = defaultdict(list)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # We want this to be removed every time we exit from the Context so we
        # can enforce the fact an event lives only within a transaction lifetime
        del self.local_storage.event_and_callback

    def register(self, domain_event: InternalEvent, callback: Callable):
        if not hasattr(self.local_storage, "event_and_callback"):
            raise Exception("register() method can only be called within a Context")
        self.local_storage.event_and_callback[domain_event].append(callback)

    @classmethod
    def publish(cls, domain_event: InternalEvent, *args, **kwargs):
        if not hasattr(cls, "local_storage") or not hasattr(
            cls.local_storage, "local_storage"
        ):
            raise Exception("raise_event() method needs to be called within a Context")

        for callback in cls.local_storage.event_and_callback[domain_event]:
            callback(*args, **kwargs)
