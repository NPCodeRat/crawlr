import glob
import os.path
import unicodecsv
import datetime


class CSVUtil(object):
    """Push formatted data to CSV"""

    @classmethod
    def build(cls, aggregate):
        data_path = '../data/'
        filename = datetime.datetime.now().strftime('%G%m%dT%H%M%S.csv')
        files = glob.glob('../data/*')
        print 'Emptying previous search results...'
        for file in files:
            os.remove(file)
        print 'Writing search results to CSV...'
        output = open('{}{}'.format(data_path, filename), 'wb')
        writer = unicodecsv.writer(output, delimiter=',', encoding='utf-8')
        for row in aggregate:
            writer.writerow(row)
        print 'CSV complete.  Check crawlr/data for output.'
