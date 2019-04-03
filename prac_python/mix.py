#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 16:01:10 2018

@author: tdhiraj
"""

def populate_dict(s):
    import string
    d_s = {}
    for x in string.ascii_lowercase:
        cnt = s.count(x)
        if cnt > 1:
            d_s[x] = cnt
    return d_s

def mix(s1, s2):
    output= []
    m_s1 = populate_dict(s1)
    m_s2 = populate_dict(s2)
    for k in m_s1:
        if m_s2.get(k,0) != 0:
            if m_s1[k] > m_s2[k]:
                output.append('1:'+ (k*m_s1[k]))
            elif m_s1[k] < m_s2[k]:
                output.append('2:' + k*m_s2[k])
            else:
                output.append('=:' + k*m_s1[k])
            del m_s2[k]
        else:
            output.append('1:'+ (k*m_s1[k]))

    for k in m_s2:
        output.append('2:'+(k*m_s2[k]))
    output.sort(key=lambda x: (-len(x), x))
    return '/'.join(output)

print(mix('looping is fun but dangerous','less dangerous than coding'))