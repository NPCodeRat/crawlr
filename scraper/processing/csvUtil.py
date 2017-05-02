import glob
import os.path
import unicodecsv
import datetime
import definitions


class CSVUtil(object):
    """Push formatted data to CSV"""

    @classmethod
    def build(cls, aggregate):
        data_path = os.path.join(definitions.ROOT_DIR, 'data')
        filename = datetime.datetime.now().strftime('%G%m%dT%H%M%S.csv')
        files = os.path.join(data_path, '*')
        files = glob.glob(files)
        print 'Emptying previous search results...'
        for file in files:
            os.remove(file)
        print 'Writing search results to CSV...'
        output = open(os.path.join(data_path, filename), 'wb')
        writer = unicodecsv.writer(output, delimiter=',', encoding='utf-8')
        for row in aggregate:
            writer.writerow(row)
        print 'CSV complete.  Check crawlr/data for output.'
