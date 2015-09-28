# -*- coding: utf-8-unix; mode: python -*-
"""hmctgmls: How many challenges to get the my lovely ship ?

hmctgmls is a short script to get the number of trials to win a rare drop item.

Copyright (c) 2015 IMAI Toshiyuki

Author: 2015 IMAI Toshiyuki

This software is released under the MIT License.
http://opensource.org/licenses/mit-license.php
"""
__author__ = 'IMAI Toshiyuki'
__version__ = '1.0'

import sys
from decimal import *

if __name__ == '__main__':
    print()
    print('How many challenges to get the my lovely ship ?')
    print()

    try:
        rate = sys.argv[1]
    except:
        print('Need an argument for drop rate.')
        print()
        print('example:')
        print('>python {0[0]} 2.5'.format(sys.argv))
        exit()

    if Decimal(rate) <= 0:
        print('The argument must be higher than 0.')
        exit()

    try:
        rate = Decimal(rate) / Decimal(100)
    except:
        print('The argument must be a numerical number.')
        exit()

    print('When the drop rate is {0}%.'.format(sys.argv[1]))
    print()

    chance = Decimal(100)
    result = {'20p': 0,
              '50p': 0,
              '80p': 0,
              '90p': 0,
              '95p': 0,
              '98p': 0,
              '99p': 0,
              '99_999p': 0}
    count = 0
    while chance > Decimal(0.001):
        count += 1
        chance -= chance * rate
        if chance <= 80 and result['20p'] == 0:
            result['20p'] = count
        if chance <= 50 and result['50p'] == 0:
            result['50p'] = count
        if chance <= 20 and result['80p'] == 0:
            result['80p'] = count
        if chance <= 10 and result['90p'] == 0:
            result['90p'] = count
        if chance <= 5 and result['95p'] == 0:
            result['95p'] = count
        if chance <= 2 and result['98p'] == 0:
            result['98p'] = count
        if chance <= 1 and result['99p'] == 0:
            result['99p'] = count
        if chance <= 0.001 and result['99_999p'] == 0:
            result['99_999p'] = count

    print('''result
20%    : {20p:>4}
50%    : {50p:>4}
80%    : {80p:>4}
90%    : {90p:>4}
95%    : {95p:>4}
98%    : {98p:>4}
99%    : {99p:>4}
99.999%: {99_999p:>4}'''.format(**result))
