from proxy.cbReq import CBReq
from proxy.monsterReq import MonsterReq
from scraper.processing.csvUtil import CSVUtil

cb = CBReq.start()
monster = MonsterReq.start()
CSVUtil.build(cb, monster)
