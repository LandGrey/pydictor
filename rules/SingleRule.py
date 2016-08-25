#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-23
#
# Single item rule
#
# This is a part of pydictor


def SingleRule(cname, ename, sname, birth, usedpwd, phone, uphone, hphone, email, postcode, nickname, idcard, jobnum, otherdate, usedchar):
    res = []
    for cn in cname:
        res.append(cn)
    for en in ename:
        res.append(en)
        res.append(str(en).upper())
    for sn in sname:
        res.append(sn)
        # {sname _ SNAME}
        res.append(str(sn).lower() + '_' + str(sn).upper())
        # {sname @ SNAME}
        res.append(str(sn).lower() + '@' + str(sn).upper())
        # {sname SNAME .}
        res.append(str(sn).lower() + str(sn).upper() + '.')
    for bd in birth:
        res.append(bd)
        res.append(str(bd)[2:])
        res.append(str(bd)[:4] + str(bd)[4:].replace('0', ''))
    for upass in usedpwd:
        res.append(upass)
        # {upass .}
        res.append(upass + '.')
        # {upass _}
        res.append(upass + '_')
        # {_ upass}
        res.append('_' + upass)
    for ph in phone:
        res.append(ph)
    for uph in uphone:
        res.append(uph)
    for hp in hphone:
        res.append(hp)
    for em in email:
        res.append(em)
        # {@xxx.xxx}
        res.append('@' + str(em).split('@')[1])
    for pc in postcode:
        res.append(pc)
    for nn in nickname:
        res.append(nn)
    for ic in idcard:
        res.append(ic[:6])
        res.append(ic[-4:])
        res.append(ic[-6:])
        res.append(ic[-8:])
    for jn in jobnum:
        res.append(jn)
    for od in otherdate:
        res.append(od)
        res.append(str(od)[2:])
        res.append(str(od)[:4] + str(od)[4:].replace('0', ''))
    for uc in usedchar:
        res.append(uc)

    return res