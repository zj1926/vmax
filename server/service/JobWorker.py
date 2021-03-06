import os
from server.misc.CsvWriter import CsvWriter
from server.misc.util import json_reader
from server.misc.FileWalker import FileWalker
import server.service.UtilService as UtilService

json_config = json_reader('./local/movie_config.json')
paths, img_temp, star_path = json_config["paths"], json_config["img_temp"], json_config["star_path"]



def do_category():
    result = []
    for one_cat in star_path:
        one_group = []
        for root, dirs, files in os.walk(one_cat):
            if not one_group:
                one_group = dirs
                break
        result.append(one_group)
    return result


def do_csv():
    walker = FileWalker(paths)
    list = walker.getList()

    map = {
        'company': 'c',
        'id': 'i',
        'movie': 'm',
        'image': 'im',
        'url': 'r'
    }
    print("generating the CSV file ... ")

    wr = CsvWriter()
    wr.start(map, list)

    print('================')
    print('Finished!')
    print('================')


def do_dup():
    list = UtilService.csv_to_list()
    result = []
    end = len(list) - 1

    for oneIndex, oneItem in enumerate(list):
        if oneIndex < end and oneItem['c'] == list[oneIndex + 1]['c'] and oneItem['i'] == list[oneIndex + 1]['i']:
            result.append(oneItem)
            result.append(list[oneIndex + 1])

    print('generate dup result successfully!')
    return result


def parse_name(rawstr):
    if not rawstr[0].isalpha():
        return None
    str = rawstr.replace('-', '')
    alpha_start = False
    id_start = False
    result = ['', '']

    for key, v in enumerate(str):
        if v.isalpha():
            alpha_start = True
        if alpha_start and v.isdigit():
            id_start = True
        if id_start and not v.isdigit():
            break

        if id_start:
            result[1] += v
        else:
            result[0] += v.lower()

    return result


def do_pair():
    fileList = UtilService.csv_to_list()
    img_list = []
    map_list = []
    for root, dirs, files in os.walk(img_temp):
        for onename in files:
            parse_name_result = parse_name(onename)
            if parse_name_result:
                img_list.append({
                    'c': parse_name_result[0],
                    'i': parse_name_result[1],
                    'oa': onename
                })

    for one_parse in img_list:
        matched = False
        dictItem = None
        for oneFile in fileList:
            if oneFile['i'] == one_parse['i'] and oneFile['c'] == one_parse['c']:
                matched = True
                dictItem = oneFile
        if matched:
            map_list.append({'img': one_parse['oa'], 'target': dictItem['r']})

    return map_list


def do_filter_1(keyword0):
    list = UtilService.csv_to_list()
    keyword = keyword0.encode('utf-8')
    sku = parse_name(keyword)
    result = filter(lambda x: sku[0] in x['c'] and sku[1] in x['i'], list)
    return result

def do_filter_2(keyword0):
    keyword = keyword0.encode('utf-8')
    list = UtilService.csv_to_list()
    result = []
    for one_item in list:
        try:
            keyInMovie = False
            for onemovie in one_item['m']:
                if keyword in onemovie:
                    keyInMovie = True
            if keyword in one_item['r'].lower() or keyInMovie:
                result.append(one_item)
        except Exception as e:
            print(one_item['r'])
            print(one_item['m'])

    return result