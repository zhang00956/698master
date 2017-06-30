'''msg reply'''
import time
from master.trans import common


def get_link_replay_apdu(trans_object):
    '''get_link_replay_apdu'''
    tm1_text = common.list2text(list(filter(lambda row: row['dtype'] == 'date_time'\
                                                , trans_object.res_list))[0]['m_list'])
    tm_local = time.localtime()
    tm2_text = '%04X %02X %02X %02X %02X %02X %02X 0000'\
                    % (tm_local[0], tm_local[1], tm_local[2],\
                        tm_local[7], tm_local[3], tm_local[4], tm_local[5])
    reply_apdu_text = '81 %s %s'%(trans_object.get_piid(), '80') + tm1_text + tm2_text + tm2_text
    return reply_apdu_text


def get_rpt_replay_apdu(trans_object):
    '''get_rpt_replay_apdu'''
    reply_test = '00'
    return reply_test