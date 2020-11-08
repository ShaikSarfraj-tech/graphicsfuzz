# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from gfauto.common_pb2 import (
    Binary as gfauto___common_pb2___Binary,
)

from gfauto.device_pb2 import (
    DeviceList as gfauto___device_pb2___DeviceList,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Settings(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    maximum_duplicate_crashes: builtin___int = ...
    maximum_fuzz_failures: builtin___int = ...
    reduce_tool_crashes: builtin___bool = ...
    reduce_crashes: builtin___bool = ...
    reduce_bad_images: builtin___bool = ...
    extra_graphics_fuzz_generate_args: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    extra_graphics_fuzz_reduce_args: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    only_reduce_signature_regex: typing___Text = ...
    _comment: typing___Text = ...
    extra_spirv_fuzz_generate_args: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    extra_spirv_fuzz_shrink_args: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    extra_spirv_reduce_args: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    common_spirv_args: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    legacy_graphics_fuzz_vulkan_arg: builtin___bool = ...
    skip_semantics_changing_reduction: builtin___bool = ...
    spirv_opt_just_o: builtin___bool = ...
    keep_reduction_work: builtin___bool = ...

    @property
    def device_list(self) -> gfauto___device_pb2___DeviceList: ...

    @property
    def custom_binaries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[gfauto___common_pb2___Binary]: ...

    @property
    def latest_binary_versions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[gfauto___common_pb2___Binary]: ...

    def __init__(self,
        *,
        device_list : typing___Optional[gfauto___device_pb2___DeviceList] = None,
        custom_binaries : typing___Optional[typing___Iterable[gfauto___common_pb2___Binary]] = None,
        maximum_duplicate_crashes : typing___Optional[builtin___int] = None,
        maximum_fuzz_failures : typing___Optional[builtin___int] = None,
        reduce_tool_crashes : typing___Optional[builtin___bool] = None,
        reduce_crashes : typing___Optional[builtin___bool] = None,
        reduce_bad_images : typing___Optional[builtin___bool] = None,
        latest_binary_versions : typing___Optional[typing___Iterable[gfauto___common_pb2___Binary]] = None,
        extra_graphics_fuzz_generate_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        extra_graphics_fuzz_reduce_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        only_reduce_signature_regex : typing___Optional[typing___Text] = None,
        _comment : typing___Optional[typing___Text] = None,
        extra_spirv_fuzz_generate_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        extra_spirv_fuzz_shrink_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        extra_spirv_reduce_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        common_spirv_args : typing___Optional[typing___Iterable[typing___Text]] = None,
        legacy_graphics_fuzz_vulkan_arg : typing___Optional[builtin___bool] = None,
        skip_semantics_changing_reduction : typing___Optional[builtin___bool] = None,
        spirv_opt_just_o : typing___Optional[builtin___bool] = None,
        keep_reduction_work : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Settings: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Settings: ...
    def HasField(self, field_name: typing_extensions___Literal[u"device_list",b"device_list"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"_comment",b"_comment",u"common_spirv_args",b"common_spirv_args",u"custom_binaries",b"custom_binaries",u"device_list",b"device_list",u"extra_graphics_fuzz_generate_args",b"extra_graphics_fuzz_generate_args",u"extra_graphics_fuzz_reduce_args",b"extra_graphics_fuzz_reduce_args",u"extra_spirv_fuzz_generate_args",b"extra_spirv_fuzz_generate_args",u"extra_spirv_fuzz_shrink_args",b"extra_spirv_fuzz_shrink_args",u"extra_spirv_reduce_args",b"extra_spirv_reduce_args",u"keep_reduction_work",b"keep_reduction_work",u"latest_binary_versions",b"latest_binary_versions",u"legacy_graphics_fuzz_vulkan_arg",b"legacy_graphics_fuzz_vulkan_arg",u"maximum_duplicate_crashes",b"maximum_duplicate_crashes",u"maximum_fuzz_failures",b"maximum_fuzz_failures",u"only_reduce_signature_regex",b"only_reduce_signature_regex",u"reduce_bad_images",b"reduce_bad_images",u"reduce_crashes",b"reduce_crashes",u"reduce_tool_crashes",b"reduce_tool_crashes",u"skip_semantics_changing_reduction",b"skip_semantics_changing_reduction",u"spirv_opt_just_o",b"spirv_opt_just_o"]) -> None: ...
type___Settings = Settings
