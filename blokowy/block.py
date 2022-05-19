# Przemysław Sankowski
# 12.04.2021

import string
import sys
from PIL import Image
from io import BytesIO
import random
import hashlib

def readimage(path):
    with open(path, "rb") as f:
            return bytearray(f.read())

def generate_output_image(input_image, output_image_name):
    output_image = Image.open(BytesIO(input_image))
    output_image.save(output_image_name)

def md5sum(block):
    back_to_bytes = bytes(block)
    result = hashlib.md5(back_to_bytes)
    result_list = []

    for i in result.digest():
        result_list.append(i)

    return result_list

def ecb_encrypt(ecb_img):
    single_block = []
    counter = 0
    pos = 0
    block_size = 16

    for i in ecb_img[54:]:
        counter += 1
        single_block.append(i)
        if counter % block_size == 0:
            md5ed_block = md5sum(single_block)
            for j in range(0, block_size):
                ecb_img[54 + j + pos] = md5ed_block[j]
            pos += block_size
            single_block.clear()

def xor(var, key):
    key = key[:len(var)]
    int_var = int.from_bytes(var, sys.byteorder)
    int_key = int.from_bytes(key, sys.byteorder)
    int_enc = int_var ^ int_key
    return int_enc.to_bytes(len(var), sys.byteorder)

def cbc_encrypt(cbc_img):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    IV = bytes(random_string, 'utf-8')
    single_block = []
    counter = 0
    pos = 0
    block_size = 8

    first_block = xor(bytes(cbc_img[54:54 + block_size]), IV)
    md5ed_block = md5sum(first_block)
    prev_block = md5ed_block

    for i in range(0, block_size):
        cbc_img[54 + i] = md5ed_block[i]

    for i in cbc_img[54 + block_size:]:
        counter += 1
        single_block.append(i)
        if counter % block_size == 0:
            current_block = xor(prev_block, single_block)
            md5ed_block = md5sum(current_block)
            prev_block = md5ed_block
            for j in range(0, block_size):
                cbc_img[54 + j + pos] = md5ed_block[j]
            pos += block_size
            single_block.clear()

if __name__ =="__main__":
    ecb_img = readimage("plain.bmp")
    cbc_img = readimage("plain.bmp")
    ecb_encrypt(ecb_img)
    cbc_encrypt(cbc_img)
    generate_output_image(ecb_img, "ecb_crypto.bmp")
    generate_output_image(cbc_img, 'cbc_crypto.bmp')

