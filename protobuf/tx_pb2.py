# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tx.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tx.proto',
  package='protobuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x08tx.proto\x12\x08protobuf\"\xc0\x01\n\x0bTransaction\x12\x0e\n\x06\x65xecer\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12&\n\tsignature\x18\x03 \x01(\x0b\x32\x13.protobuf.Signature\x12\x0b\n\x03\x66\x65\x65\x18\x04 \x01(\x03\x12\x0e\n\x06\x65xpire\x18\x05 \x01(\x03\x12\r\n\x05nonce\x18\x06 \x01(\x03\x12\n\n\x02to\x18\x07 \x01(\t\x12\x12\n\ngroupCount\x18\x08 \x01(\x05\x12\x0e\n\x06header\x18\t \x01(\x0c\x12\x0c\n\x04next\x18\n \x01(\x0c\":\n\tSignature\x12\n\n\x02ty\x18\x01 \x01(\x05\x12\x0e\n\x06pubkey\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"\xe4\x01\n\x0b\x43oinsAction\x12,\n\x08transfer\x18\x01 \x01(\x0b\x32\x18.protobuf.AssetsTransferH\x00\x12,\n\x08withdraw\x18\x04 \x01(\x0b\x32\x18.protobuf.AssetsWithdrawH\x00\x12*\n\x07genesis\x18\x02 \x01(\x0b\x32\x17.protobuf.AssetsGenesisH\x00\x12\x38\n\x0etransferToExec\x18\x05 \x01(\x0b\x32\x1e.protobuf.AssetsTransferToExecH\x00\x12\n\n\x02ty\x18\x03 \x01(\x05\x42\x07\n\x05value\"6\n\rAssetsGenesis\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x15\n\rreturnAddress\x18\x03 \x01(\t\"e\n\x14\x41ssetsTransferToExec\x12\x11\n\tcointoken\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x0c\n\x04note\x18\x03 \x01(\x0c\x12\x10\n\x08\x65xecName\x18\x04 \x01(\t\x12\n\n\x02to\x18\x05 \x01(\t\"_\n\x0e\x41ssetsWithdraw\x12\x11\n\tcointoken\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x0c\n\x04note\x18\x03 \x01(\x0c\x12\x10\n\x08\x65xecName\x18\x04 \x01(\t\x12\n\n\x02to\x18\x05 \x01(\t\"M\n\x0e\x41ssetsTransfer\x12\x11\n\tcointoken\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x0c\n\x04note\x18\x03 \x01(\x0c\x12\n\n\x02to\x18\x04 \x01(\t\"5\n\x05\x41sset\x12\x0c\n\x04\x65xec\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"2\n\x0cTransactions\x12\"\n\x03txs\x18\x01 \x03(\x0b\x32\x15.protobuf.Transactionb\x06proto3'
)




_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='protobuf.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execer', full_name='protobuf.Transaction.execer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protobuf.Transaction.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='protobuf.Transaction.signature', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='protobuf.Transaction.fee', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expire', full_name='protobuf.Transaction.expire', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='protobuf.Transaction.nonce', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='protobuf.Transaction.to', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groupCount', full_name='protobuf.Transaction.groupCount', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='protobuf.Transaction.header', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next', full_name='protobuf.Transaction.next', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=215,
)


_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='protobuf.Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ty', full_name='protobuf.Signature.ty', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pubkey', full_name='protobuf.Signature.pubkey', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='protobuf.Signature.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=275,
)


_COINSACTION = _descriptor.Descriptor(
  name='CoinsAction',
  full_name='protobuf.CoinsAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transfer', full_name='protobuf.CoinsAction.transfer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='withdraw', full_name='protobuf.CoinsAction.withdraw', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='genesis', full_name='protobuf.CoinsAction.genesis', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transferToExec', full_name='protobuf.CoinsAction.transferToExec', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ty', full_name='protobuf.CoinsAction.ty', index=4,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='protobuf.CoinsAction.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=278,
  serialized_end=506,
)


_ASSETSGENESIS = _descriptor.Descriptor(
  name='AssetsGenesis',
  full_name='protobuf.AssetsGenesis',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='protobuf.AssetsGenesis.amount', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='returnAddress', full_name='protobuf.AssetsGenesis.returnAddress', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=562,
)


_ASSETSTRANSFERTOEXEC = _descriptor.Descriptor(
  name='AssetsTransferToExec',
  full_name='protobuf.AssetsTransferToExec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cointoken', full_name='protobuf.AssetsTransferToExec.cointoken', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protobuf.AssetsTransferToExec.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='protobuf.AssetsTransferToExec.note', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execName', full_name='protobuf.AssetsTransferToExec.execName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='protobuf.AssetsTransferToExec.to', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=665,
)


_ASSETSWITHDRAW = _descriptor.Descriptor(
  name='AssetsWithdraw',
  full_name='protobuf.AssetsWithdraw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cointoken', full_name='protobuf.AssetsWithdraw.cointoken', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protobuf.AssetsWithdraw.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='protobuf.AssetsWithdraw.note', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execName', full_name='protobuf.AssetsWithdraw.execName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='protobuf.AssetsWithdraw.to', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=667,
  serialized_end=762,
)


_ASSETSTRANSFER = _descriptor.Descriptor(
  name='AssetsTransfer',
  full_name='protobuf.AssetsTransfer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cointoken', full_name='protobuf.AssetsTransfer.cointoken', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protobuf.AssetsTransfer.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='protobuf.AssetsTransfer.note', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='protobuf.AssetsTransfer.to', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=841,
)


_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='protobuf.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exec', full_name='protobuf.Asset.exec', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='protobuf.Asset.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='protobuf.Asset.amount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=843,
  serialized_end=896,
)


_TRANSACTIONS = _descriptor.Descriptor(
  name='Transactions',
  full_name='protobuf.Transactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txs', full_name='protobuf.Transactions.txs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=898,
  serialized_end=948,
)

_TRANSACTION.fields_by_name['signature'].message_type = _SIGNATURE
_COINSACTION.fields_by_name['transfer'].message_type = _ASSETSTRANSFER
_COINSACTION.fields_by_name['withdraw'].message_type = _ASSETSWITHDRAW
_COINSACTION.fields_by_name['genesis'].message_type = _ASSETSGENESIS
_COINSACTION.fields_by_name['transferToExec'].message_type = _ASSETSTRANSFERTOEXEC
_COINSACTION.oneofs_by_name['value'].fields.append(
  _COINSACTION.fields_by_name['transfer'])
_COINSACTION.fields_by_name['transfer'].containing_oneof = _COINSACTION.oneofs_by_name['value']
_COINSACTION.oneofs_by_name['value'].fields.append(
  _COINSACTION.fields_by_name['withdraw'])
_COINSACTION.fields_by_name['withdraw'].containing_oneof = _COINSACTION.oneofs_by_name['value']
_COINSACTION.oneofs_by_name['value'].fields.append(
  _COINSACTION.fields_by_name['genesis'])
_COINSACTION.fields_by_name['genesis'].containing_oneof = _COINSACTION.oneofs_by_name['value']
_COINSACTION.oneofs_by_name['value'].fields.append(
  _COINSACTION.fields_by_name['transferToExec'])
_COINSACTION.fields_by_name['transferToExec'].containing_oneof = _COINSACTION.oneofs_by_name['value']
_TRANSACTIONS.fields_by_name['txs'].message_type = _TRANSACTION
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE
DESCRIPTOR.message_types_by_name['CoinsAction'] = _COINSACTION
DESCRIPTOR.message_types_by_name['AssetsGenesis'] = _ASSETSGENESIS
DESCRIPTOR.message_types_by_name['AssetsTransferToExec'] = _ASSETSTRANSFERTOEXEC
DESCRIPTOR.message_types_by_name['AssetsWithdraw'] = _ASSETSWITHDRAW
DESCRIPTOR.message_types_by_name['AssetsTransfer'] = _ASSETSTRANSFER
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
DESCRIPTOR.message_types_by_name['Transactions'] = _TRANSACTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), {
  'DESCRIPTOR' : _SIGNATURE,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Signature)
  })
_sym_db.RegisterMessage(Signature)

CoinsAction = _reflection.GeneratedProtocolMessageType('CoinsAction', (_message.Message,), {
  'DESCRIPTOR' : _COINSACTION,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.CoinsAction)
  })
_sym_db.RegisterMessage(CoinsAction)

AssetsGenesis = _reflection.GeneratedProtocolMessageType('AssetsGenesis', (_message.Message,), {
  'DESCRIPTOR' : _ASSETSGENESIS,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.AssetsGenesis)
  })
_sym_db.RegisterMessage(AssetsGenesis)

AssetsTransferToExec = _reflection.GeneratedProtocolMessageType('AssetsTransferToExec', (_message.Message,), {
  'DESCRIPTOR' : _ASSETSTRANSFERTOEXEC,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.AssetsTransferToExec)
  })
_sym_db.RegisterMessage(AssetsTransferToExec)

AssetsWithdraw = _reflection.GeneratedProtocolMessageType('AssetsWithdraw', (_message.Message,), {
  'DESCRIPTOR' : _ASSETSWITHDRAW,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.AssetsWithdraw)
  })
_sym_db.RegisterMessage(AssetsWithdraw)

AssetsTransfer = _reflection.GeneratedProtocolMessageType('AssetsTransfer', (_message.Message,), {
  'DESCRIPTOR' : _ASSETSTRANSFER,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.AssetsTransfer)
  })
_sym_db.RegisterMessage(AssetsTransfer)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Asset)
  })
_sym_db.RegisterMessage(Asset)

Transactions = _reflection.GeneratedProtocolMessageType('Transactions', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONS,
  '__module__' : 'tx_pb2'
  # @@protoc_insertion_point(class_scope:protobuf.Transactions)
  })
_sym_db.RegisterMessage(Transactions)


# @@protoc_insertion_point(module_scope)