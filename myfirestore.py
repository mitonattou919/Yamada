from google.cloud import firestore

import time
import datetime

import dts

#         1         2         3         4         5         6         7
#1234567890123456789012345678901234567890123456789012345678901234567890123456789

def return_datetime(val):
    tz_jst = datetime.timezone(datetime.timedelta(hours=9))

    dt_tmp = datetime.datetime(val.year, val.month, val.day,
        val.hour, val.minute, val.second,tzinfo=tz_jst)

    dt = dt_tmp + datetime.timedelta(hours = 9)

    return dt

#         1         2         3         4         5         6         7
#1234567890123456789012345678901234567890123456789012345678901234567890123456789


class MyFireStore:

    switch_time = 6

    def __init__(self, col_root):
        self.col_root = col_root

    def set_time(self, set_type, user_id, dt):

        start_time = time.time()

        if set_type == 'start':
            data = {
                u'start_time': dt
            }

            dt_target = dt
        
        elif set_type == 'end':
            data = {
                u'end_time': dt
            }

            dt_from = datetime.datetime(
                dt.year, dt.month, dt.day, 0,
                tzinfo=datetime.timezone(datetime.timedelta(hours=9))
            )

            dt_switch = datetime.datetime(
                dt.year, dt.month, dt.day, self.switch_time,
                tzinfo=datetime.timezone(datetime.timedelta(hours=9))
            )

            if dt_from <= dt <= dt_switch:
                dt_target = dt - datetime.timedelta(days=1)
            else:
                dt_target = dt

        else:
            raise ValueError('Invalid type')

        my_dt = dts.DateTime2String(dt_target)
        col_name = my_dt.get_colname()
        doc_name = my_dt.get_docname()

        db = firestore.Client()
        user_ref = db.collection(self.col_root).document(user_id)

        user_ref.collection(col_name).document(doc_name).set(data, merge=True)

        elapsed_time = time.time() - start_time
        print ("fs.set_time elapsed:{0}".format(elapsed_time) + "[sec]")


    def set_teamid(self, user_id, team_id):

        start_time = time.time()

        data = {
            u'team_id': team_id
        }

        db = firestore.Client()
        db.collection(self.col_root).document(user_id).set(data, merge=True)

        elapsed_time = time.time() - start_time
        print ("fs.set_teamid elapsed:{0}".format(elapsed_time) + "[sec]")


    def set_common(self, user_id, set_key, set_val):

        start_time = time.time()

        data = {
            set_key: set_val
        }

        db = firestore.Client()
        db.collection(self.col_root).document(user_id).set(data, merge=True)

        elapsed_time = time.time() - start_time
        print ("fs.set_common elapsed:{0}".format(elapsed_time) + "[sec]")


    def get_various(self, user_id):

        start_time = time.time()

        db = firestore.Client()
        doc_ref = db.collection(self.col_root).document(user_id)
        doc = doc_ref.get()
        if doc.exists:
            print(f'Document data: {doc.to_dict()}')
            d = doc.to_dict()

            return d

        else:
            print(f'No such document.')

        elapsed_time = time.time() - start_time
        print ("fs.get_various elapsed:{0}".format(elapsed_time) + "[sec]")


    def init_various(self, user_id):

        start_time = time.time()

        db = firestore.Client()
        doc_ref = db.collection(self.col_root).document(user_id)

        doc_ref.update({
            u'modify_type': firestore.DELETE_FIELD,
            u'modify_date': firestore.DELETE_FIELD,
            u'modify_hour': firestore.DELETE_FIELD,
            u'modify_min': firestore.DELETE_FIELD,
            u'modify_user': firestore.DELETE_FIELD,
            u'report_month': firestore.DELETE_FIELD,
            u'report_user': firestore.DELETE_FIELD
        })

        elapsed_time = time.time() - start_time
        print ("fs.init elapsed:{0}".format(elapsed_time) + "[sec]")


    def get_user(self, team_id):

        start_time = time.time()

        user_dic = {}
        db = firestore.Client()
        docs = db.collection(self.col_root).where(u'team_id', u'==', team_id).stream()

        for doc in docs:
            user_id = doc.id
            d = doc.to_dict()
            user_name = d['user_name']
            user_dic[user_id] = user_name

        elapsed_time = time.time() - start_time
        print ("fs.get_user elapsed:{0}".format(elapsed_time) + "[sec]")

        return user_dic


    def get_time(self, user_id, dt):

        start_time = time.time()

        my_dt = dts.DateTime2String(dt)
        col_name = my_dt.get_colname()
        doc_name = my_dt.get_docname()

        target_month = dt.strftime('%Y/%m')
        report_text = ''

        db = firestore.Client()
        user_ref = db.collection(self.col_root).document(user_id)

        docs = user_ref.collection(col_name).order_by(u'start_time').stream()

        break_minutes_60 = 60
        break_minutes_45 = 45
        total_secs = 0
        working_days = 0

        for doc in docs:
            d = doc.to_dict()

            if 'start_time' in d and 'end_time' in d:
                dt_start = return_datetime(d['start_time'])
                dt_end = return_datetime(d['end_time'])
                td_tmp = dt_end - dt_start

                if td_tmp.seconds > (8*60*60):
                    td = td_tmp - datetime.timedelta(minutes = break_minutes_60)
                elif td_tmp.seconds > (6*60*60):
                    td = td_tmp - datetime.timedelta(minutes = break_minutes_45)
                else:
                    td = td_tmp

                total_secs = total_secs + td.seconds
                report_text = ( report_text + '\n'
                               + dt_start.strftime('%m/%d %H:%M') 
                               + ' ~ ' + dt_end.strftime('%H:%M') + ' ' 
                               + format((td.seconds / 60 / 60), '3.2f') + '時間')
                
                working_days += 1

        #average_secs = total_secs / i

        elapsed_time = time.time() - start_time
        print ("fs.get_time elapsed:{0}".format(elapsed_time) + "[sec]")

        #return report_text
        return target_month, report_text, total_secs, working_days


#         1         2         3         4         5         6         7
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
