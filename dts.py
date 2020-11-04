import datetime
import calendar

#         1         2         3         4         5         6         7
#1234567890123456789012345678901234567890123456789012345678901234567890123456789

# [START control date and time]
class DateTime2String:

    switch_hour = 6
    
    # initialization
    def __init__(self, dt_val):
        self.dt_val = dt_val

    def get_dummy(self, text):
        print(text)

    # get first date of target month.
    def get_first(self):
        dt_first = datetime.date(self.dt_val.year, self.dt_val.month, 1)
        return dt_first

    # get last date of target month.
    def get_last(self):
        dt_first = datetime.date(self.dt_val.year, self.dt_val.month, 1)
        _, days = calendar.monthrange(self.dt_val.year, self.dt_val.month)
        dt_last = dt_first + datetime.timedelta(days=days - 1)
        return dt_last

    # get collection name like 202006.
    def get_colname(self):
        col_name = self.dt_val.strftime('%Y%m')
        return col_name


    # get document name like 20200630.
    def get_docname(self):
        doc_name = self.dt_val.strftime('%Y%m%d')
        return doc_name


    # get document name like 20200630.
    def get_ymd(self):
        ymd_format = self.dt_val.strftime('%Y-%m-%d')
        return ymd_format


# [END control date and time]


#         1         2         3         4         5         6         7
#1234567890123456789012345678901234567890123456789012345678901234567890123456789

class Ms2DataTime:

    def __init__(self, dtn_val):
        self.dtn_val = dtn_val

    def get_dt():
        tz_jst = datetime.timezone(datetime.timedelta(hours=9))

        dt = datetime.datetime(self.dtn_val.year, self.dtn_val.month, 
                               self.dtn_val.day, self.dtn_val.hour + 9, 
                               self.dtn_val.minute, self.dtn_val.second,
                               tzinfo=tz_jst)

        return dt


