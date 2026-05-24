from bitcoinlib.keys import Key
from base58 import b58decode_check


def get_key(data: int) -> Key:
    k = Key(data.to_bytes(32, "big"))
    return k


def get_raw_address_20_bytes_from_add_str(data: str) -> bytes:
    add_raw = b58decode_check(data)[1:]
    return add_raw


def get_address_str_from_keyobj(data: Key) -> str:
    add = data.address()
    return add


def get_encoded_int_from_raw_bytes(data: bytes) -> int:
    the_int = int.from_bytes(data, "big")
    return the_int


def get_key_address_int(data: int) -> int:
    k = get_key(data)
    add = get_address_str_from_keyobj(k)
    add_raw = get_raw_address_20_bytes_from_add_str(add)
    add_int = get_encoded_int_from_raw_bytes(add_raw)
    return add_int


def get_key_address_str(data: int) -> str:
    k = get_key(data)
    k_add = get_address_str_from_keyobj(k)
    return k_add


def get_int_to_list(data: int) -> list[int]:
    str_version = str(data)
    the_list = []
    for item in str_version:
        the_list.append(int(item))
    return the_list

def get_int_to_wrapped_list(data: int) -> list[list[int]]:
    the_unwrapped_list = get_int_to_list(data)
    holder = []
    for item in the_unwrapped_list:
        holder.append([item])
    return holder