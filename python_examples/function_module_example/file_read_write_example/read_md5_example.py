# -*- coding:utf-8 -*-
import hashlib

__author__ = 'Evan'


def get_file_md5(path):
    """
    获取文件内容的MD5值
    :param path: 文件所在路径
    :return:
    """
    with open(path, 'rb') as file:
        data = file.read()

    diff_check = hashlib.md5()
    diff_check.update(data)
    md5_code = diff_check.hexdigest()
    return md5_code


if __name__ == '__main__':
    md5_str = get_file_md5(path=r'C:\Users\evaliu\Desktop\sample.txt')
    print(md5_str)
