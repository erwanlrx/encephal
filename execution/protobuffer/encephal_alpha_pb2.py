# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: encephal_alpha.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
import sys
if sys.version_info >= (3,):
  # some constants that are python2 only
  unicode = str
  long = int
  range = range
  unichr = chr
  def b(s):
    return s.encode("latin-1")
  def u(s):
    return s
else:
  #some constants that are python2 only
  range = xrange
  unicode = unicode
  long = long
  unichr = unichr
  def b(s):
    return s
  # Workaround for standalone backslash
  def u(s):
    return unicode(s.replace(r'\\', r'\\\\'), "unicode_escape")

from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='encephal_alpha.proto',
  package='encephal_alpha',
  serialized_pb=b(
    '\n\x14\x65ncephal_alpha.proto\x12\x0e\x65ncephal_alpha\"\x8c\x01\n\x08\x44\x61taType\x12\x12\n\ndimensions\x18\x01 \x03(\r\x12\x32\n\x04type\x18\x02 \x02(\x0e\x32$.encephal_alpha.DataType.NumericType\"8\n\x0bNumericType\x12\t\n\x05\x46LOAT\x10\x01\x12\t\n\x05INT32\x10\x02\x12\t\n\x05INT64\x10\x03\x12\x08\n\x04\x42OOL\x10\x04\"V\n\x13PerceptronLayerData\x12?\n\x13\x61\x63tivation_function\x18\x01 \x02(\x0e\x32\".encephal_alpha.ActivationFunction\"\xae\x01\n\x16\x43onvolutionalLayerData\x12L\n\x0czero_padding\x18\x01 \x02(\x0e\x32\x36.encephal_alpha.ConvolutionalLayerData.ZeroPaddingType\x12\x14\n\x0ckernel_shape\x18\x02 \x03(\r\"0\n\x0fZeroPaddingType\x12\t\n\x05VALID\x10\x01\x12\x08\n\x04SAME\x10\x02\x12\x08\n\x04\x46ULL\x10\x03\"\x1d\n\x10\x44ropoutLayerData\x12\t\n\x01p\x18\x01 \x02(\x02\"\x18\n\x16\x46ullConnexionLayerData\"\xe0\x04\n\x08PipeNode\x12\r\n\x05index\x18\x01 \x02(\r\x12\x30\n\x0einput_datatype\x18\x02 \x02(\x0b\x32\x18.encephal_alpha.DataType\x12\x30\n\x0eouput_datatype\x18\x03 \x02(\x0b\x32\x18.encephal_alpha.DataType\x12\x38\n\tnode_type\x18\x04 \x02(\x0e\x32%.encephal_alpha.PipeNode.PipeNodeType\x12\x33\n\x04\x64\x61ta\x18\x05 \x02(\x0b\x32%.encephal_alpha.PipeNode.PipeNodeData\x1a\x8b\x02\n\x0cPipeNodeData\x12>\n\x0e\x66ull_connexion\x18\x01 \x01(\x0b\x32&.encephal_alpha.FullConnexionLayerData\x12\x37\n\rdropout_layer\x18\x02 \x01(\x0b\x32 .encephal_alpha.DropoutLayerData\x12=\n\x10perceptron_layer\x18\x03 \x01(\x0b\x32#.encephal_alpha.PerceptronLayerData\x12\x43\n\x13\x63onvolutional_layer\x18\x04 \x01(\x0b\x32&.encephal_alpha.ConvolutionalLayerData\"d\n\x0cPipeNodeType\x12\x12\n\x0e\x46ULL_CONNEXION\x10\x01\x12\x11\n\rDROPOUT_LAYER\x10\x02\x12\x14\n\x10PERCEPTRON_LAYER\x10\x03\x12\x17\n\x13\x43ONVOLUTIONAL_LAYER\x10\x04\"6\n\nConnection\x12\x14\n\x0csocket_index\x18\x01 \x02(\r\x12\x12\n\nnode_index\x18\x02 \x02(\r\"C\n\x06Socket\x12\r\n\x05index\x18\x01 \x02(\r\x12*\n\x08\x64\x61tatype\x18\x02 \x02(\x0b\x32\x18.encephal_alpha.DataType\"=\n\x12SchedulerNodeLayer\x12\'\n\x05nodes\x18\x01 \x03(\x0b\x32\x18.encephal_alpha.PipeNode\"\x94\x01\n\x05Graph\x12\x31\n\x05nodes\x18\x01 \x03(\x0b\x32\".encephal_alpha.SchedulerNodeLayer\x12\'\n\x07sockets\x18\x02 \x03(\x0b\x32\x16.encephal_alpha.Socket\x12/\n\x0b\x63onnections\x18\x03 \x03(\x0b\x32\x1a.encephal_alpha.Connection\"d\n\tDataArray\x12\x14\n\x0c\x66loat_vector\x18\x01 \x03(\x02\x12\x15\n\ruint32_vector\x18\x02 \x03(\r\x12\x15\n\ruint64_vector\x18\x03 \x03(\x04\x12\x13\n\x0b\x62ool_vector\x18\x04 \x03(\x08\"\x9b\x02\n\x0fTrainingDataset\x12\x30\n\x0einput_datatype\x18\x01 \x02(\x0b\x32\x18.encephal_alpha.DataType\x12\x31\n\x0foutput_datatype\x18\x02 \x02(\x0b\x32\x18.encephal_alpha.DataType\x12>\n\x07\x65ntries\x18\x03 \x03(\x0b\x32-.encephal_alpha.TrainingDataset.TrainingEntry\x1a\x63\n\rTrainingEntry\x12(\n\x05input\x18\x01 \x02(\x0b\x32\x19.encephal_alpha.DataArray\x12(\n\x05label\x18\x02 \x02(\x0b\x32\x19.encephal_alpha.DataArray\"n\n\x0eTestingDataset\x12\x30\n\x0einput_datatype\x18\x01 \x02(\x0b\x32\x18.encephal_alpha.DataType\x12*\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x19.encephal_alpha.DataArray*;\n\x12\x41\x63tivationFunction\x12\x0b\n\x07NOTHING\x10\x01\x12\x0b\n\x07SIGMOID\x10\x02\x12\x0b\n\x07SOFTMAX\x10\x03'))

_ACTIVATIONFUNCTION = _descriptor.EnumDescriptor(
  name='ActivationFunction',
  full_name='encephal_alpha.ActivationFunction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOTHING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGMOID', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFTMAX', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1955,
  serialized_end=2014,
)

ActivationFunction = enum_type_wrapper.EnumTypeWrapper(_ACTIVATIONFUNCTION)
NOTHING = 1
SIGMOID = 2
SOFTMAX = 3


_DATATYPE_NUMERICTYPE = _descriptor.EnumDescriptor(
  name='NumericType',
  full_name='encephal_alpha.DataType.NumericType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT32', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT64', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=125,
  serialized_end=181,
)

_CONVOLUTIONALLAYERDATA_ZEROPADDINGTYPE = _descriptor.EnumDescriptor(
  name='ZeroPaddingType',
  full_name='encephal_alpha.ConvolutionalLayerData.ZeroPaddingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VALID', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAME', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=398,
  serialized_end=446,
)

_PIPENODE_PIPENODETYPE = _descriptor.EnumDescriptor(
  name='PipeNodeType',
  full_name='encephal_alpha.PipeNode.PipeNodeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FULL_CONNEXION', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DROPOUT_LAYER', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERCEPTRON_LAYER', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVOLUTIONAL_LAYER', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1014,
  serialized_end=1114,
)


_DATATYPE = _descriptor.Descriptor(
  name='DataType',
  full_name='encephal_alpha.DataType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='encephal_alpha.DataType.dimensions', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='encephal_alpha.DataType.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATATYPE_NUMERICTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=41,
  serialized_end=181,
)


_PERCEPTRONLAYERDATA = _descriptor.Descriptor(
  name='PerceptronLayerData',
  full_name='encephal_alpha.PerceptronLayerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activation_function', full_name='encephal_alpha.PerceptronLayerData.activation_function', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=183,
  serialized_end=269,
)


_CONVOLUTIONALLAYERDATA = _descriptor.Descriptor(
  name='ConvolutionalLayerData',
  full_name='encephal_alpha.ConvolutionalLayerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zero_padding', full_name='encephal_alpha.ConvolutionalLayerData.zero_padding', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kernel_shape', full_name='encephal_alpha.ConvolutionalLayerData.kernel_shape', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONVOLUTIONALLAYERDATA_ZEROPADDINGTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=272,
  serialized_end=446,
)


_DROPOUTLAYERDATA = _descriptor.Descriptor(
  name='DropoutLayerData',
  full_name='encephal_alpha.DropoutLayerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p', full_name='encephal_alpha.DropoutLayerData.p', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=448,
  serialized_end=477,
)


_FULLCONNEXIONLAYERDATA = _descriptor.Descriptor(
  name='FullConnexionLayerData',
  full_name='encephal_alpha.FullConnexionLayerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=479,
  serialized_end=503,
)


_PIPENODE_PIPENODEDATA = _descriptor.Descriptor(
  name='PipeNodeData',
  full_name='encephal_alpha.PipeNode.PipeNodeData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='full_connexion', full_name='encephal_alpha.PipeNode.PipeNodeData.full_connexion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dropout_layer', full_name='encephal_alpha.PipeNode.PipeNodeData.dropout_layer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perceptron_layer', full_name='encephal_alpha.PipeNode.PipeNodeData.perceptron_layer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='convolutional_layer', full_name='encephal_alpha.PipeNode.PipeNodeData.convolutional_layer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=745,
  serialized_end=1012,
)

_PIPENODE = _descriptor.Descriptor(
  name='PipeNode',
  full_name='encephal_alpha.PipeNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='encephal_alpha.PipeNode.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_datatype', full_name='encephal_alpha.PipeNode.input_datatype', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ouput_datatype', full_name='encephal_alpha.PipeNode.ouput_datatype', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_type', full_name='encephal_alpha.PipeNode.node_type', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='encephal_alpha.PipeNode.data', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PIPENODE_PIPENODEDATA, ],
  enum_types=[
    _PIPENODE_PIPENODETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=506,
  serialized_end=1114,
)


_CONNECTION = _descriptor.Descriptor(
  name='Connection',
  full_name='encephal_alpha.Connection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='socket_index', full_name='encephal_alpha.Connection.socket_index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_index', full_name='encephal_alpha.Connection.node_index', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1116,
  serialized_end=1170,
)


_SOCKET = _descriptor.Descriptor(
  name='Socket',
  full_name='encephal_alpha.Socket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='encephal_alpha.Socket.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datatype', full_name='encephal_alpha.Socket.datatype', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1172,
  serialized_end=1239,
)


_SCHEDULERNODELAYER = _descriptor.Descriptor(
  name='SchedulerNodeLayer',
  full_name='encephal_alpha.SchedulerNodeLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='encephal_alpha.SchedulerNodeLayer.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1241,
  serialized_end=1302,
)

_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='encephal_alpha.Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='encephal_alpha.Graph.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sockets', full_name='encephal_alpha.Graph.sockets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connections', full_name='encephal_alpha.Graph.connections', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1305,
  serialized_end=1453,
)

_DATAARRAY = _descriptor.Descriptor(
  name='DataArray',
  full_name='encephal_alpha.DataArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='float_vector', full_name='encephal_alpha.DataArray.float_vector', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint32_vector', full_name='encephal_alpha.DataArray.uint32_vector', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint64_vector', full_name='encephal_alpha.DataArray.uint64_vector', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_vector', full_name='encephal_alpha.DataArray.bool_vector', index=3,
      number=4, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1455,
  serialized_end=1555,
)

_TRAININGDATASET_TRAININGENTRY = _descriptor.Descriptor(
  name='TrainingEntry',
  full_name='encephal_alpha.TrainingDataset.TrainingEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='encephal_alpha.TrainingDataset.TrainingEntry.input', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='encephal_alpha.TrainingDataset.TrainingEntry.label', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1742,
  serialized_end=1841,
)

_TRAININGDATASET = _descriptor.Descriptor(
  name='TrainingDataset',
  full_name='encephal_alpha.TrainingDataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_datatype', full_name='encephal_alpha.TrainingDataset.input_datatype', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_datatype', full_name='encephal_alpha.TrainingDataset.output_datatype', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entries', full_name='encephal_alpha.TrainingDataset.entries', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TRAININGDATASET_TRAININGENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1558,
  serialized_end=1841,
)

_TESTINGDATASET = _descriptor.Descriptor(
  name='TestingDataset',
  full_name='encephal_alpha.TestingDataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_datatype', full_name='encephal_alpha.TestingDataset.input_datatype', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entries', full_name='encephal_alpha.TestingDataset.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1843,
  serialized_end=1953,
)

_DATATYPE.fields_by_name['type'].enum_type = _DATATYPE_NUMERICTYPE
_DATATYPE_NUMERICTYPE.containing_type = _DATATYPE;
_PERCEPTRONLAYERDATA.fields_by_name['activation_function'].enum_type = _ACTIVATIONFUNCTION
_CONVOLUTIONALLAYERDATA.fields_by_name['zero_padding'].enum_type = _CONVOLUTIONALLAYERDATA_ZEROPADDINGTYPE
_CONVOLUTIONALLAYERDATA_ZEROPADDINGTYPE.containing_type = _CONVOLUTIONALLAYERDATA;
_PIPENODE_PIPENODEDATA.fields_by_name['full_connexion'].message_type = _FULLCONNEXIONLAYERDATA
_PIPENODE_PIPENODEDATA.fields_by_name['dropout_layer'].message_type = _DROPOUTLAYERDATA
_PIPENODE_PIPENODEDATA.fields_by_name['perceptron_layer'].message_type = _PERCEPTRONLAYERDATA
_PIPENODE_PIPENODEDATA.fields_by_name['convolutional_layer'].message_type = _CONVOLUTIONALLAYERDATA
_PIPENODE_PIPENODEDATA.containing_type = _PIPENODE;
_PIPENODE.fields_by_name['input_datatype'].message_type = _DATATYPE
_PIPENODE.fields_by_name['ouput_datatype'].message_type = _DATATYPE
_PIPENODE.fields_by_name['node_type'].enum_type = _PIPENODE_PIPENODETYPE
_PIPENODE.fields_by_name['data'].message_type = _PIPENODE_PIPENODEDATA
_PIPENODE_PIPENODETYPE.containing_type = _PIPENODE;
_SOCKET.fields_by_name['datatype'].message_type = _DATATYPE
_SCHEDULERNODELAYER.fields_by_name['nodes'].message_type = _PIPENODE
_GRAPH.fields_by_name['nodes'].message_type = _SCHEDULERNODELAYER
_GRAPH.fields_by_name['sockets'].message_type = _SOCKET
_GRAPH.fields_by_name['connections'].message_type = _CONNECTION
_TRAININGDATASET_TRAININGENTRY.fields_by_name['input'].message_type = _DATAARRAY
_TRAININGDATASET_TRAININGENTRY.fields_by_name['label'].message_type = _DATAARRAY
_TRAININGDATASET_TRAININGENTRY.containing_type = _TRAININGDATASET;
_TRAININGDATASET.fields_by_name['input_datatype'].message_type = _DATATYPE
_TRAININGDATASET.fields_by_name['output_datatype'].message_type = _DATATYPE
_TRAININGDATASET.fields_by_name['entries'].message_type = _TRAININGDATASET_TRAININGENTRY
_TESTINGDATASET.fields_by_name['input_datatype'].message_type = _DATATYPE
_TESTINGDATASET.fields_by_name['entries'].message_type = _DATAARRAY
DESCRIPTOR.message_types_by_name['DataType'] = _DATATYPE
DESCRIPTOR.message_types_by_name['PerceptronLayerData'] = _PERCEPTRONLAYERDATA
DESCRIPTOR.message_types_by_name['ConvolutionalLayerData'] = _CONVOLUTIONALLAYERDATA
DESCRIPTOR.message_types_by_name['DropoutLayerData'] = _DROPOUTLAYERDATA
DESCRIPTOR.message_types_by_name['FullConnexionLayerData'] = _FULLCONNEXIONLAYERDATA
DESCRIPTOR.message_types_by_name['PipeNode'] = _PIPENODE
DESCRIPTOR.message_types_by_name['Connection'] = _CONNECTION
DESCRIPTOR.message_types_by_name['Socket'] = _SOCKET
DESCRIPTOR.message_types_by_name['SchedulerNodeLayer'] = _SCHEDULERNODELAYER
DESCRIPTOR.message_types_by_name['Graph'] = _GRAPH
DESCRIPTOR.message_types_by_name['DataArray'] = _DATAARRAY
DESCRIPTOR.message_types_by_name['TrainingDataset'] = _TRAININGDATASET
DESCRIPTOR.message_types_by_name['TestingDataset'] = _TESTINGDATASET

DataType = _reflection.GeneratedProtocolMessageType('DataType', (_message.Message,),
                                                    {
                                                      'DESCRIPTOR': _DATATYPE,
                                                      # @@protoc_insertion_point(class_scope:encephal_alpha.DataType)
                                                    })

PerceptronLayerData = _reflection.GeneratedProtocolMessageType('PerceptronLayerData', (_message.Message,),
                                                               {
                                                                 'DESCRIPTOR': _PERCEPTRONLAYERDATA,
                                                                 # @@protoc_insertion_point(class_scope:encephal_alpha.PerceptronLayerData)
                                                               })

ConvolutionalLayerData = _reflection.GeneratedProtocolMessageType('ConvolutionalLayerData', (_message.Message,),
                                                                  {
                                                                    'DESCRIPTOR': _CONVOLUTIONALLAYERDATA,
                                                                    # @@protoc_insertion_point(class_scope:encephal_alpha.ConvolutionalLayerData)
                                                                  })

DropoutLayerData = _reflection.GeneratedProtocolMessageType('DropoutLayerData', (_message.Message,),
                                                            {
                                                              'DESCRIPTOR': _DROPOUTLAYERDATA,
                                                              # @@protoc_insertion_point(class_scope:encephal_alpha.DropoutLayerData)
                                                            })

FullConnexionLayerData = _reflection.GeneratedProtocolMessageType('FullConnexionLayerData', (_message.Message,),
                                                                  {
                                                                    'DESCRIPTOR': _FULLCONNEXIONLAYERDATA,
                                                                    # @@protoc_insertion_point(class_scope:encephal_alpha.FullConnexionLayerData)
                                                                  })

PipeNode = _reflection.GeneratedProtocolMessageType('PipeNode', (_message.Message,),
                                                    {
                                                      'DESCRIPTOR': _PIPENODE,
                                                      'PipeNodeData': _reflection.GeneratedProtocolMessageType(
                                                        'PipeNodeData', (_message.Message,),
                                                        {
                                                          'DESCRIPTOR': _PIPENODE_PIPENODEDATA,
                                                          # @@protoc_insertion_point(class_scope:encephal_alpha.PipeNode.PipeNodeData)
                                                        }),
                                                      # @@protoc_insertion_point(class_scope:encephal_alpha.PipeNode)
                                                    })

Connection = _reflection.GeneratedProtocolMessageType('Connection', (_message.Message,),
                                                      {
                                                        'DESCRIPTOR': _CONNECTION,
                                                        # @@protoc_insertion_point(class_scope:encephal_alpha.Connection)
                                                      })

Socket = _reflection.GeneratedProtocolMessageType('Socket', (_message.Message,),
                                                  {
                                                    'DESCRIPTOR': _SOCKET,
                                                    # @@protoc_insertion_point(class_scope:encephal_alpha.Socket)
                                                  })

SchedulerNodeLayer = _reflection.GeneratedProtocolMessageType('SchedulerNodeLayer', (_message.Message,),
                                                              {
                                                                'DESCRIPTOR': _SCHEDULERNODELAYER,
                                                                # @@protoc_insertion_point(class_scope:encephal_alpha.SchedulerNodeLayer)
                                                              })

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,),
                                                 {
                                                   'DESCRIPTOR': _GRAPH,
                                                   # @@protoc_insertion_point(class_scope:encephal_alpha.Graph)
                                                 })

DataArray = _reflection.GeneratedProtocolMessageType('DataArray', (_message.Message,),
                                                     {
                                                       'DESCRIPTOR': _DATAARRAY,
                                                       # @@protoc_insertion_point(class_scope:encephal_alpha.DataArray)
                                                     })

TrainingDataset = _reflection.GeneratedProtocolMessageType('TrainingDataset', (_message.Message,),
                                                           {
                                                             'DESCRIPTOR': _TRAININGDATASET,
                                                             'TrainingEntry': _reflection.GeneratedProtocolMessageType(
                                                               'TrainingEntry', (_message.Message,),
                                                               {
                                                                 'DESCRIPTOR': _TRAININGDATASET_TRAININGENTRY,
                                                                 # @@protoc_insertion_point(class_scope:encephal_alpha.TrainingDataset.TrainingEntry)
                                                               }),
                                                             # @@protoc_insertion_point(class_scope:encephal_alpha.TrainingDataset)
                                                           })

TestingDataset = _reflection.GeneratedProtocolMessageType('TestingDataset', (_message.Message,),
                                                          {
                                                            'DESCRIPTOR': _TESTINGDATASET,
                                                            # @@protoc_insertion_point(class_scope:encephal_alpha.TestingDataset)
                                                          })


# @@protoc_insertion_point(module_scope)
