from subprocess import check_call
from sys import executable
from typing import Any, Literal

from bitcoinlib.keys import Key
from base58 import b58decode_check
from random import choice


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


def get_random_list(
    length_data: int, one_block_data: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
):
    holder = []
    for i in range(length_data):
        holder.append(choice(one_block_data))
    return holder


def get_underscore_from_int_to_str(data: int, marker: str = ",") -> str:
    the_str_version = str(data)
    the_holder_list = []
    counter = 0
    for item in the_str_version[::-1]:
        if counter == 3:
            counter = 0
            the_holder_list.append(marker)
            the_holder_list.append(item)
        else:
            the_holder_list.append(item)
        counter += 1

    if the_holder_list[::-1][0] == marker:
        the_holder_list.pop(-1)
    the_final_str = "".join(the_holder_list[::-1])
    return the_final_str


def get_list_padded_with_extra_length_with_targeted_position_and_char(
    list_data: list,
    pad_from_position_data: Literal["right", "left"],
    extra_length: int,
    char_you_want: Any,
):
    holder = []
    for item in list_data:
        holder.append(item)
    if pad_from_position_data == "left":
        for i in range(extra_length):
            holder.insert(0, char_you_want)
    elif pad_from_position_data == "right":
        for i in range(extra_length):
            holder.append(char_you_want)
    else:
        print(f"Unknown position [{pad_from_position_data}]")
        return False

    return holder


def get_int_to_list_int(data: int) -> list[int]:
    str_version = str(data)
    holder = []
    for digit in str_version:
        holder.append(int(digit))
    return holder


def get_key_int_list_to_address_int_list(data: list[int]) -> list[int]:
    the_str_version = ""
    for digit in data:
        the_str_version += str(digit)
    the_int = int(the_str_version)
    int_address = get_key_address_int(the_int)
    str_int_address = str(int_address)
    address_list_holder = []
    for digit in str_int_address:
        address_list_holder.append(int(digit))
    return address_list_holder


# this is a wrapper for [get_list_padded_with_extra_length_with_targeted_position_and_char]
def get_extra_list(
    list_data: list,
    pad_from_position_data: Literal["right", "left"],
    extra_length: int,
    char_you_want: Any,
):
    return get_list_padded_with_extra_length_with_targeted_position_and_char(
        list_data, pad_from_position_data, extra_length, char_you_want
    )


def get_auto_united_length(
    the_one_to_modify: list,
    the_reference: list,
    pad_position: Literal["left", "right"],
    pad_char: Any,
) -> list:
    the_one_to_modify_length = len(the_one_to_modify)
    the_reference_length = len(the_reference)
    if the_one_to_modify_length == the_reference_length:
        return the_one_to_modify
    elif the_one_to_modify_length > the_reference_length:
        raise Exception(
            "the length of the_one_to_modify is even larger than the length of the_reference"
        )
    elif the_one_to_modify_length < the_reference_length:
        return get_extra_list(
            the_one_to_modify,
            pad_position,
            the_reference_length - the_one_to_modify_length,
            pad_char,
        )


def get_list_splitted_equally(list_data: list, how_many_per_chunk: int):
    holder = [
        list_data[i : i + how_many_per_chunk]
        for i in range(0, len(list_data), how_many_per_chunk)
    ]
    return holder

def get_version_synced(version_data: str):
    hardcoded_url = f"https://github.com/sailornewborn/jacks/releases/download/{version_data}/jacks-{version_data}-py3-none-any.whl"
    check_call([executable,'-m','pip','install',hardcoded_url])

class GetAll:
    def __init__(self,mother_int: int = 1):
        self.mother_int = mother_int
        self.mother_int_list = get_int_to_list_int(self.mother_int)