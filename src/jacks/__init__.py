from subprocess import check_call
from sys import executable
from typing import Any, Literal
from pathlib import Path
from bitcoinlib.keys import Key
from base58 import b58decode_check
from random import choice
import requests
import tomllib
from jacks.revolver import *
import psutil
from socket import AF_INET
from site import getsitepackages
from jacks.walker import *


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
        list_data[i: i + how_many_per_chunk]
        for i in range(0, len(list_data), how_many_per_chunk)
    ]
    return holder


def get_version_synced(version_data: str = None):
    if version_data == None:
        # automatically download the latest
        version_file_url = "https://github.com/sailornewborn/jacks/raw/refs/heads/master/pyproject.toml"
        requested_data = requests.get(version_file_url)
        if requested_data.status_code == 200:
            # success
            version_we_got = tomllib.loads(requested_data.text)["project"]["version"]
            version_data = version_we_got
        else:
            raise Exception("Failed to get the version data from github!")
    hardcoded_url = f"https://github.com/sailornewborn/jacks/releases/download/{version_data}/jacks-{version_data}-py3-none-any.whl"
    check_call([executable, "-m", "pip", "install", hardcoded_url])


class GetAll:
    def __init__(self, mother_int: int = 1):
        self.mother_int = mother_int
        self.mother_int_list = get_int_to_list_int(self.mother_int)
        self.son_address_int = get_key_address_int(self.mother_int)
        self.son_address_int_list = get_int_to_list_int(self.son_address_int)

    def auto_reset(self, new_mother_int: int):
        self.__init__(new_mother_int)


class GetRightBitcoinUniqueIdentifier:
    def __init__(self, identifier: int = 1):
        self.the_unique_identifier = identifier
        self.data_to_calculate = get_int_to_list_int(
            get_key_address_int(self.the_unique_identifier)
        )

    def get_visual(self):
        print(self.the_unique_identifier)
        print(self.data_to_calculate)


def get_LAN_ip_windows() -> str:
    possible_ip = None
    all_interfaces = psutil.net_if_addrs()
    for name, infos in all_interfaces.items():
        for set in infos:
            if set.address.startswith("192.") and set.family == AF_INET:
                possible_ip = set.address
    return possible_ip


class GetUniqueIdentifier:
    # here we set the most significant number the very left one
    def __init__(self, block_size: int = 10):
        self.data_to_calculate: list[int] = None
        self.block_size: int = block_size
        self.unique_identifier: int = None

    def get_data_set(self, data: list[int]):
        self.data_to_calculate = data

    def get_unique_identifier(self):
        identifier_sum = 0
        for number in self.data_to_calculate:
            identifier_sum = (number + identifier_sum) * self.block_size
        self.unique_identifier = int(identifier_sum / self.block_size)
        return self.unique_identifier


# put this function before any real logic!
def get_currentpage_to_preprocessing(
        file_var,
        overwrite_or_append: Literal["overwrite", "append"] = "append",
):
    current_file_path_obj = Path(file_var)
    current_file_texts = current_file_path_obj.read_text()
    current_file_text_lines = current_file_texts.splitlines()
    for line in current_file_text_lines:
        if line.strip().startswith("get_currentpage_to_preprocessing"):
            current_file_text_lines.remove(line)
    current_file_text_lines.insert(0, "\n")
    new_codes = "\n".join(current_file_text_lines)
    sitepackage_path_obj = Path(getsitepackages()[0])
    actual_preprocessing_file_obj = sitepackage_path_obj / "sitecustomize.py"
    if overwrite_or_append == "append":
        if actual_preprocessing_file_obj.exists():
            actual_preprocessing_file_obj.write_text(new_codes, mode="a")
        else:
            actual_preprocessing_file_obj.touch()
            actual_preprocessing_file_obj.write_text(new_codes)
    elif overwrite_or_append == "overwrite":
        if actual_preprocessing_file_obj.exists():
            actual_preprocessing_file_obj.write_text(new_codes)
        else:
            actual_preprocessing_file_obj.touch()
            actual_preprocessing_file_obj.write_text(new_codes)
    else:
        raise Exception(f"Unrecognized option! {overwrite_or_append}")


# here we default the numeric base to 10
def get_form_into_binary_list(accepted_form: list[int] | int) -> list[int]:
    if isinstance(accepted_form, list):
        joint_form = int("".join([str(i) for i in accepted_form]))
        bin_str = bin(joint_form)[2:]
        list_form = list(bin_str)
        list_form = [int(i) for i in list_form]
        return list_form
    elif isinstance(accepted_form, int):
        bin_str = bin(accepted_form)[2:]
        list_form = list(bin_str)
        list_form = [int(i) for i in list_form]
        return list_form


def get_int_from_existing_address(address: str = "") -> int:
    if address == "":
        prize_add = "12c6DSiU4Rq3P4ZxziKxzrL5LmMBrzjrJX"
        address = prize_add
    prize_add_byte = b58decode_check(address)[1:]
    prize_add_int = int.from_bytes(prize_add_byte)
    return prize_add_int


def get_primer_fired(primer: int = 1, times: int = 100) -> list[int]:
    primer_holder = []
    primer_holder.append(primer)
    for i in range(times):
        primer = get_key_address_int(primer)
        primer_holder.append(primer)
    return primer_holder


def get_primer_fired_and_printed(primer: int = 1, times: int = 100) -> list[int]:
    a = get_primer_fired(primer, times)
    for item in a:
        print(item)
    return a


def get_evaluated(file_name):
    indexes = []
    p = Path(file_name)
    lines = p.read_text().splitlines()
    index = 0
    for line in lines:
        if line.strip().endswith('#'):
            indexes.append(index)
        index += 1
    index = 0
    for i in indexes:
        temp_catcher = {}
        left_side = lines[i].split('=')[0].strip()
        exec(p.read_text(), {}, temp_catcher)
        # print(temp_catcher['c'])
        temp_catcher = temp_catcher[left_side]
        if isinstance(temp_catcher, str):
            right_side = f"'{temp_catcher}'"
        elif isinstance(temp_catcher, int):
            right_side = f"{temp_catcher}"
        # currently we only want to support lists with all elements either str or int
        elif isinstance(temp_catcher,list):
            right_side = ""
            supported_type = [int,str]
            for ty in supported_type:
                counter = 0
                for item in temp_catcher:
                    if isinstance(item,ty):
                        counter += 1
                if counter == len(temp_catcher):
                    if ty is int:
                        right_side += '['
                        for index,element in enumerate(temp_catcher):
                            if index == len(temp_catcher) - 1:
                                right_side += f"{element}"
                            else:
                                right_side += f"{element},"
                        right_side += "]"
                    elif ty is str:
                        right_side += "["
                        for index, element in enumerate(temp_catcher):
                            if index == len(temp_catcher)-1:
                                right_side += f"\"{element}\""
                            else:
                                right_side += f"\"{element}\","
                        right_side += "]"
            if right_side == "":
                raise Exception(f"The list has incompatible element(s) that is/are not any of {supported_type} types")

        else:
            raise Exception(f"Cannot translate this type of data {type(temp_catcher)} {temp_catcher}")
        lines[i] = left_side.strip() + " = " + right_side
        index += 1
    full_line_str = "\n".join(lines)
    p.write_text(full_line_str)
    print(f"edit written in file {p}")

def get_multiple_keys_at_once(keys: list[int]) -> list[int]:
    holder = []
    for item in keys:
        holder.append(get_key_address_int(item))
    return holder