from proxy.cbReq import CBReq
from proxy.monsterReq import MonsterReq
from scraper.processing.csvUtil import CSVUtil

# Run one CB and one Monster scrape
cb = CBReq.start()
monster = MonsterReq.start()
CSVUtil.build(cb, monster)
