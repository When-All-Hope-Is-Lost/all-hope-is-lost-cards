"""Insert an 'Outside the US' block (before ## Source & license) and the international sources into weather cards.
Usage: python3 tools/intl_block.py <card.md> "<terminology line>"   (idempotent)"""
import sys,re
FAC='"Foreign government page; reuse terms not relied on. Facts only, restated in own words, link-out."'
SRC=[
("GOV.UK: 999 and 112, the UK's national emergency numbers","https://www.gov.uk/guidance/999-and-112-the-uks-national-emergency-numbers"),
("Met Office: Weather warnings guide (National Severe Weather Warning Service)","https://weather.metoffice.gov.uk/guides/warnings"),
("gov.ie: Emergency contacts (112 or 999)","https://www.gov.ie/en/department-of-the-taoiseach/publications/emergency-contacts/"),
("Met Éireann: Warnings & Advisories","https://www.met.ie/warnings"),
("CRTC: 9-1-1 services in Canada","https://crtc.gc.ca/eng/phone/911/can.htm"),
("Environment and Climate Change Canada: Weather alerts (colour-coded Warnings, Advisories, Watches)","https://www.canada.ca/en/services/environment/weather/severeweather/weather-alerts.html"),
("Australian Government (Infrastructure): How to call Triple Zero (000); Using other emergency numbers","https://www.infrastructure.gov.au/media-communications/phone/triple-zero/how-call-triple-zero-000"),
("Bureau of Meteorology: National Warnings Summary","https://www.bom.gov.au/australia/warnings/"),
("New Zealand Government: 111 emergency service","https://www.govt.nz/browse/law-crime-and-justice/crimes-and-emergencies/111-emergency-service/"),
("MetService: About Severe Weather Warnings","https://about.metservice.com/about-severe-weather-warnings"),
]
BLOCK="""**Outside the US** (official sites, checked 2026-10-16):
- **Emergency number:** UK **999 or 112** · Ireland **112 or 999** · Canada **911** (Nunavut and a few other places use local numbers) · Australia **000** (112 also works from a mobile; you can't text 000) · New Zealand **111**.
- **Official warnings:** UK **Met Office** (yellow, amber, red) · Ireland **Met Éireann** (met.ie) · Canada **Environment and Climate Change Canada** (weather.gc.ca or the WeatherCAN app; yellow, orange, or red Warnings, Advisories, and Watches) · Australia **Bureau of Meteorology** (bom.gov.au), plus state emergency services (Advice, Watch and Act, Emergency Warning) · New Zealand **MetService** (metservice.com; Watches, then Orange and Red Warnings), plus local Civil Defence.
"""
p,term=sys.argv[1],sys.argv[2]
s=open(p).read()
if '**Outside the US**' in s: print('skip',p); sys.exit()
blk=BLOCK+("- **Terms:** "+term+"\n" if term else "")
s=s.replace("\n## Source & license","\n"+blk+"\n## Source & license",1)
add="".join(f'  - title: "{t}"\n    url: {u}\n    checked_date: 2026-10-16\n    license: {FAC}\n' for t,u in SRC)
s=s.replace("\ncard_license:","\n"+add.rstrip("\n")+"\ncard_license:",1)
s=re.sub(r"(Card text licensed CC BY-SA 4\.0\.)",r"International emergency numbers and warning-service facts come from the official national sites listed in the sources (facts only, linked). \1",s,count=1)
open(p,'w').write(s); print('ok',p)
