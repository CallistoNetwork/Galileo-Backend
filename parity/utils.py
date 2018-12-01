from hexbytes import HexBytes
from web3.datastructures import AttributeDict


def web3_to_dict(object):
    new_object = {}

    for key in object.keys():
        value = object[key]

        if isinstance(value, HexBytes):
            value = value.hex()

        if isinstance(value, list):
            new_value = []
            for v in value:
                if isinstance(v, AttributeDict):
                    new_value.append(web3_to_dict(v))
                elif isinstance(v, HexBytes):
                    new_value.append(v.hex())
                else:
                    new_value.append(v)
            value = new_value

        new_object[key] = value

    return new_object


def convert_id_to_number_or_hash(block_id):
    try:
        return int(block_id)
    except ValueError:
        return HexBytes(block_id)
