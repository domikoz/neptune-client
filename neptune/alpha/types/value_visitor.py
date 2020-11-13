#
# Copyright (c) 2020, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import abc
from typing import TypeVar, Generic

from neptune.alpha.types.atoms import GitRef
from neptune.alpha.types.atoms.datetime import Datetime
from neptune.alpha.types.atoms.float import Float
from neptune.alpha.types.atoms.string import String
from neptune.alpha.types.atoms.file import File
from neptune.alpha.types.series.float_series import FloatSeries
from neptune.alpha.types.series.image_series import ImageSeries
from neptune.alpha.types.series.string_series import StringSeries
from neptune.alpha.types.sets.string_set import StringSet
from neptune.alpha.types.value import Value

Ret = TypeVar('Ret')


class ValueVisitor(Generic[Ret]):

    def visit(self, value: Value) -> Ret:
        return value.accept(self)

    @abc.abstractmethod
    def visit_float(self, value: Float) -> Ret:
        pass

    @abc.abstractmethod
    def visit_string(self, value: String) -> Ret:
        pass

    @abc.abstractmethod
    def visit_datetime(self, value: Datetime) -> Ret:
        pass

    @abc.abstractmethod
    def visit_file(self, value: File) -> Ret:
        pass

    @abc.abstractmethod
    def visit_float_series(self, value: FloatSeries) -> Ret:
        pass

    @abc.abstractmethod
    def visit_string_series(self, value: StringSeries) -> Ret:
        pass

    @abc.abstractmethod
    def visit_image_series(self, value: ImageSeries) -> Ret:
        pass

    @abc.abstractmethod
    def visit_string_set(self, value: StringSet) -> Ret:
        pass

    @abc.abstractmethod
    def visit_git_ref(self, value: GitRef) -> Ret:
        pass
