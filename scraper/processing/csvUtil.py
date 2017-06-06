import glob
import os.path
import unicodecsv
import datetime
import definitions


class CSVUtil(object):
    """Push formatted data to CSV"""

    @classmethod
    def build(cls, cb_aggregate, monster_aggregate):
        """Write CSVs to crawlr/data/"""
        data_path = os.path.join(definitions.ROOT_DIR, 'data')
        cb_filename = datetime.datetime.now().strftime('CB_%G%m%dT%H%M%S.csv')
        monster_filename = datetime.datetime.now().strftime('MONSTER_%G%m%dT%H%M%S.csv')
        files = os.path.join(data_path, '*')
        files = glob.glob(files)
        print 'Emptying previous search results...'
        for file in files:
            # Empty data dir on new CSV creation to prevent accumulation of large responses
            os.remove(file)
        print 'Writing search results to CSV...'
        output = open(os.path.join(data_path, cb_filename), 'wb')
        writer = unicodecsv.writer(output, delimiter=',', encoding='utf-8')
        for row in cb_aggregate:
            writer.writerow(row)
        output = open(os.path.join(data_path, monster_filename), 'wb')
        writer = unicodecsv.writer(output, delimiter=',', encoding='utf-8')
        for row in monster_aggregate:
            writer.writerow(row)
        print 'CSV(s) complete.  Check crawlr/data for output.'
