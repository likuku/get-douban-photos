#!/usr/bin/env python
# encoding: utf-8
"""
get-douban-photos.py

Created by likuku on 2017-08-21.
Copyright (c) 2017 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import requests
import random
import time

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46 Safari/536.5',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',)
# headers={'User-Agent': random.choice(USER_AGENTS)}

list_url_str_photo = []


def make_dirs_for_work():
    _dir = 'images'
    if os.path.isdir(_dir):
        print('# Info: dir %s is existed' % _dir)
    elif os.path.isfile(_dir):
        print('# Error: %s is a File !' % _dir)
        sys.exit()
    else:
        os.makedirs(_dir, mode=0o755)


def get_photo_from_list_url_str_photo_file(input_list_url_str_photo):
    pass
    # < 2017-08-29
    _list = input_list_url_str_photo
    for _index in range(len(_list)):
        pass
        _url_str = _list[_index]
        if _url_str is not None:
            pass
            try:
                pass
                _img_name_str = _url_str.rsplit('/', 1)[1]
                if os.path.isfile(_img_name_str) is False:
                    print('Download: %s' % _url_str, end=' ')
                    _response = requests.get(_url_str, headers={'User-Agent': random.choice(USER_AGENTS)})
                    # print(_response.headers)
                    if _response.status_code == requests.codes.ok:
                        open(_img_name_str, 'wb').write(_response.content)
                        print('%9d/%d OK' % (_index+1, len(_list)))
                else:
                    print('Download: %s' % _url_str, end=' ')
                    print('%9d/%d Warn: file existed' % (_index+1, len(_list)))
            except Exception as e:
                raise
    # 2017-08-29>


def get_list_url_str_photo_file(input_list_url_str_photo):
    pass
    # < 2017-08-29
    print('# make list for all photo file urls')
    _list_url_photo_page = input_list_url_str_photo
    _list = []
    for _index in range(len(_list_url_photo_page)):
        pass
        time.sleep(random.random())
        _tmp_url = get_url_str_photo_file(_list_url_photo_page[_index])
        print('# get photo url from: %s' % _list_url_photo_page[_index], end=' ')
        _list.append(_tmp_url)
        print('%9d/%d OK' % (_index+1, len(_list_url_photo_page)))
    return(_list)
    # 2017-08-29>


def get_url_str_photo_file(input_photo_url):
    pass
    # <2017-08-27
    from pyquery import PyQuery as pyq
    _url_str = input_photo_url
    # <2017-08-29
    # time.sleep(0.03)
    # 2017-08-29>
    try:
        pass
        # <2017-08-29
        _response = requests.get(_url_str, headers={'User-Agent': random.choice(USER_AGENTS)})
        _html = _response.content
        _doc_photo_page = pyq(_html)
        # 2017-08-29>
        _url_str_photo_large = _doc_photo_page('.photo-edit')('a').attr('href')
        if _url_str_photo_large is not None:
            pass
            # <2017-08-29
            _response = requests.get(_url_str_photo_large, headers={'User-Agent': random.choice(USER_AGENTS)})
            _html = _response.content
            _doc_photo_large = pyq(_html)
            # 2017-08-29>
            _url_str_photo_large_file = _doc_photo_large('.pic-wrap')('img').attr('src')
            _url_str_photo_file = _url_str_photo_large_file
        else:
            _url_str_photo_main = _doc_photo_page('.mainphoto')('img').attr('src')
            _url_str_photo_file = _url_str_photo_main
    except Exception as e:
        raise
        pass
        _url_str_photo_file is None
    return(_url_str_photo_file)
    # 2017-08-27 >


def get_list_url_str_photo(input_album_url):
    pass
    # < 2017-08-27
    print('# make list for all photo page urls')
    from pyquery import PyQuery as pyq
    _url_str = input_album_url
    _list_url_str_photo = []
    _url_str_next_page = None
    try:
        pass
        # <2017-08-29
        _response = requests.get(_url_str, headers={'User-Agent': random.choice(USER_AGENTS)})
        _html = _response.content
        _doc_photo_page = pyq(_html)
        # 2017-08-29>
        _url_str_next_page = _doc_photo_page('.next')('a').attr('href')
        # print('type(_url_str_next_page)',type(_url_str_next_page))
        # <2017-08-29
        # print('_url_str_next_page:',_url_str_next_page)
        # 2017-08-29 >
        _a_list = _doc_photo_page('.photo_wrap')('.photolst_photo')
        for href in _a_list.items():
            pass
            # print(href('a').attr('href'))
            _url_str_photo_page = href('a').attr('href')
            # _list_url_str_photo.append(_url_str_photo_page)
            list_url_str_photo.append(_url_str_photo_page)
        # print((_url_str_next_page is not None) and (_url_str_next_page.find('type=rec') == -1))
        # while ((_url_str_next_page is not None) and (_url_str_next_page.find('type=rec') == -1)):
        if ((_url_str_next_page is not None) and (_url_str_next_page.find('type=rec') is -1)):
            pass
            # <2017-08-29
            # print('_url_str_next_page in while:',_url_str_next_page)
            # print('_count_key:',_url_str_next_page.find('type=rec'))
            time.sleep(random.random())
            # 2017-08-29 >
            get_list_url_str_photo(_url_str_next_page)
        # return(_list_url_str_photo)
        # print(list_url_str_photo)
        return(list_url_str_photo)
    except Exception as e:
        raise
    # 2017-08-27>


def test(arg):
    pass
    from pyquery import PyQuery as pyq
    # _url_str = 'https://www.douban.com/photos/album/xxxx/'
    _url_str = sys.argv[1]
    print(_url_str)
    photo_url_list = get_list_url_str_photo(_url_str)
    photo_file_url_list = get_list_url_str_photo_file(photo_url_list)
    print(photo_url_list, len(photo_url_list), len(list(set(photo_url_list))))
    print(photo_file_url_list,)
    get_photo_from_list_url_str_photo_file(photo_file_url_list)
    sys.exit()
    try:
        pass
        doc = pyq(url=_url_str)
        print('test')
        print(doc('head').find('title').text())
        print(doc('.next')('a').attr('href'))
        # print(doc('.photo_wrap')('.photolst_photo'))
        # < 2017-08-23
        _a_list = doc('.photo_wrap')('.photolst_photo')
        for href in _a_list.items():
            pass
            print(href('a').attr('href'))
            # break
        # 2017-08-23 >
        # < 2017-08-24
            _url_str_photo_page = href('a').attr('href')
            break
            #
        _doc_photo_page = pyq(url=_url_str_photo_page)
        _url_str_photo_main = _doc_photo_page('.mainphoto')('img').attr('src')
        _url_str_photo_large = _doc_photo_page('.photo-edit')('a').attr('href')
        #
        print('main_photo:', _url_str_photo_main)
        print('large_photo_url:', _url_str_photo_large)
        # 2017-08-24 >
        # < 2017-08-27
        _doc_photo_large = pyq(url=_url_str_photo_large)
        _url_str_photo_large_file = _doc_photo_large('.pic-wrap')('img').attr('src')
        print('_url_str_photo_large_file:', _url_str_photo_large_file)
        # get_photo_from_list_url_str_photo_file([_url_str_photo_large_file])
        # print(get_url_str_photo_file(_url_str_photo_page))
        # 2017-08-27 >
    except Exception as e:
        print(e)
        pass


def main():
    pass
    make_dirs_for_work()
    #test('')

if __name__ == '__main__':
    main()
