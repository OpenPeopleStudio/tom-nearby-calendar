import json,hashlib
from datetime import datetime,timedelta,timezone
from zoneinfo import ZoneInfo
TZ=ZoneInfo('America/St_Johns')
L=[ # (start,end,title,location,url,source,virtual,note)
("2026-10-28T16:00:00-02:30","2026-10-28T18:00:00-02:30","Know Your Audience: Build Meaningful Connections","230 Elizabeth Ave, St. John's, NL A1B 3X9 (Room A1046, Art & Administration, Memorial University)","https://www.eventbrite.ca/e/know-your-audience-build-meaningful-connections-tickets-2003346691884","Eventbrite",0,""),
("2026-10-29T09:00:00-02:30","2026-10-29T10:15:00-02:30","Export Café YYT (Featuring UK Government's Department for BIST)","Co. Innovation Centre, 710 Torbay Road, #Suite A, St. John's, NL A1A 5G9","https://www.eventbrite.com/e/export-cafe-yyt-featuring-uk-governments-department-for-bist-tickets-2002233259578","Eventbrite",0,""),
("2026-10-30T08:30:00-02:30","2026-10-30T10:00:00-02:30","Tequity+ What Progress Requires: Gloria Steinem's Legacy and the Work Ahead","7 Ricketts Road, St. John's, NL A1C 6G8","https://www.eventbrite.ca/e/tequity-what-progress-requires-gloria-steinems-legacy-and-the-work-ahead-tickets-2003161843999","Eventbrite",0,""),
("2026-10-30T10:30:00-02:30","2026-10-30T13:30:00-02:30","Banking, Finance & Insurance: Careers and Connections","The Landing (UC 3015) Third Floor, University Centre, Memorial University, 1 Arctic Avenue, St. John's, NL A1B 3V6","https://www.eventbrite.ca/e/banking-finance-insurance-careers-and-connections-tickets-2003406067478","Eventbrite",0,""),
("2026-11-03T10:00:00-03:30","2026-11-03T17:00:00-03:30","2026 Atlantic Canada Mineral Processors (CMP) Conference","Alt Hotel St. John's, 125 Water Street, St. John's, NL A1C 5X4","https://www.eventbrite.ca/e/2026-atlantic-canada-mineral-processors-cmp-conference-tickets-1995449661654","Eventbrite",0,""),
("2026-11-03T17:30:00Z","2026-11-03T20:30:00Z","St. John's: Founder Bootcamp","St. John's Convention Centre, 101 New Gower St, St. John's, NL A1C 4K2","https://lu.ma/st-johns-founder-bootcamp","Luma",0,""),
("2026-11-07T18:00:00-03:30","2026-11-07T20:30:00-03:30","Connect. Empower. Elevate. | Newfoundland & Labrador Networking Event","7 Ricketts Road, St. John's, NL A1C 6G8","https://www.eventbrite.ca/e/connect-empower-elevate-newfoundland-labrador-networking-event-tickets-2000528913834","Eventbrite",0,""),
("2026-11-20T08:30:00-03:30","2026-11-20T12:30:00-03:30","CES-NL 2026 Professional Development Conference","Admiralty House Communications Museum, 365 Old Placentia Road, Mount Pearl, NL A1N 0G7","https://www.eventbrite.ca/e/ces-nl-2026-professional-development-conference-tickets-2003147004614","Eventbrite",0,""),
("2026-11-21T21:30:00Z","2026-11-22T01:30:00Z","Demo Night 6","90 Duckworth St, St. John's, NL A1C 1E7","https://lu.ma/px2a1hjt","Luma",0,""),
# personal_radar rows (no published end time -> 2h placeholder)
("R2026-11-08T19:00",None,"Raine Maida & Chantal Kreviazuk at JAG","JAG","https://jaghotel.ca","personal_radar (source: jaghotel.ca)",0,"R"),
("R2026-11-10T20:00",None,"The Last Waltz 50th Anniversary at JAG","JAG Soundhouse","https://jagsoundhouse.ca/shows/","personal_radar",0,"R"),
("R2026-11-19T20:00",None,"HYPROV at JAG","JAG Soundhouse","https://jagsoundhouse.ca/shows/","personal_radar",0,"R"),
("R2026-11-21T20:00",None,"The Trews with Wintersleep at JAG","JAG Soundhouse","https://jaghotel.ca/event/the-trews-with-wintersleep/","personal_radar",0,"R"),
("R2026-11-22T19:30",None,"Jimmy Carr at Mary Brown's","Mary Brown's Centre","https://mbcentre.ca/","personal_radar",0,"R"),
("R2026-11-26T19:30",None,"Bored Teachers comedy tour at JAG","JAG Soundhouse","https://jagsoundhouse.ca/shows/","personal_radar",0,"R"),
# virtual
("2026-10-28T15:00:00+01:00","2026-10-28T18:00:00+01:00","AI & the Agentic Era: What It Means for Founders","Online (Founder Institute)","https://www.eventbrite.com/e/ai-the-agentic-era-what-it-means-for-founders-tickets-2003209562727","Eventbrite",1,""),
("2026-10-28T12:00:00-07:00","2026-10-28T13:30:00-07:00","MENTORSHOP: Using Claude AI to Build a SaaS Site in about a Week","Online","https://www.eventbrite.com/e/mentorshop-using-claude-ai-to-build-a-saas-site-in-about-a-week-tickets-2003024863286","Eventbrite",1,""),
("2026-10-29T11:00:00-04:00","2026-10-29T12:00:00-04:00","AI-Enabled Innovation and the Future of Competitive Advantage","Online (MIT Industrial Liaison Program | Startup Exchange)","https://www.eventbrite.com/e/ai-enabled-innovation-and-the-future-of-competitive-advantage-registration-2001078065361","Eventbrite",1,""),
("2026-10-29T12:00:00-06:00","2026-10-29T13:30:00-06:00","Battery Energy Storage in Alberta","Online (Solar Alberta)","https://www.eventbrite.ca/e/battery-energy-storage-in-alberta-tickets-1997636007072","Eventbrite",1,""),
("2026-10-30T12:00:00-04:00","2026-10-30T13:00:00-04:00","Intro to Angel Investing","Online (VentureSouth)","https://www.eventbrite.com/e/intro-to-angel-investing-tickets-1963612506867","Eventbrite",1,""),
("2026-11-02T15:00:00+01:00","2026-11-02T17:30:00+01:00","Investor Readiness Session (Online Workshop for Startup Founders)","Online (Leapfunder)","https://www.eventbrite.nl/e/investor-readiness-session-online-workshop-for-startup-founders-tickets-1990414887509","Eventbrite",1,""),
("2026-11-05T13:00:00-05:00","2026-11-05T14:00:00-05:00","From Bootstrapping to Venture Capital: The Funding Landscape for Startups","Online (Futurpreneur Canada)","https://www.eventbrite.ca/e/from-bootstrapping-to-venture-capital-the-funding-landscape-for-startups-tickets-2003201107437","Eventbrite",1,""),
("2026-11-05T12:00:00-05:00","2026-11-05T13:00:00-05:00","From Research to Mission: Defense Innovation at MIT","Online (MIT ILP | Startup Exchange)","https://www.eventbrite.com/e/from-research-to-mission-defense-innovation-at-mit-registration-2002293650208","Eventbrite",1,""),
("2026-11-05T12:00:00Z","2026-11-05T13:00:00Z","How to fund your climate tech startup","Online (Barclays Eagle Labs)","https://www.eventbrite.co.uk/e/how-to-fund-your-climate-tech-startup-tickets-1994796232229","Eventbrite",1,""),
("2026-11-06T10:00:00-05:00","2026-11-06T12:00:00-05:00","European Venture Capital Summit","Online (EurDC)","https://www.eventbrite.com/e/european-venture-capital-summit-tickets-1998094648882","Eventbrite",1,""),
("2026-11-10T10:00:00-05:00","2026-11-10T11:00:00-05:00","Venture Capital: From Lab to Launch","Online (CincyTech)","https://www.eventbrite.com/e/venture-capital-from-lab-to-launch-tickets-2000271145843","Eventbrite",1,""),
("2026-11-12T08:00:00-08:00","2026-11-12T09:00:00-08:00","Venture Trailblazers Featuring Mac Conwell","Online (Founder Institute)","https://www.eventbrite.com/e/venture-trailblazers-featuring-mac-conwell-tickets-2003780779251","Eventbrite",1,""),
("2026-11-17T14:30:00Z","2026-11-17T16:30:00Z","Power From the Past: Heritage's Role in Renewable Energy","Online (Heritage Network)","https://www.eventbrite.co.uk/e/power-from-the-past-heritages-role-in-renewable-energy-tickets-2001164427673","Eventbrite",1,""),
("2026-11-19T13:00:00-05:00","2026-11-19T15:00:00-05:00","November 2026 Online VC Fast Pitch.","Online (Black Dog Venture Partners)","https://www.eventbrite.com/e/november-2026-online-vc-fast-pitch-tickets-2003376111880","Eventbrite",1,""),
("2026-11-19T19:00:00-05:00","2026-11-19T20:00:00-05:00","Co-Founder Matching Online Event | Find a Startup Business Partner","Online (FoundersBeta)","https://www.eventbrite.ca/e/co-founder-matching-online-event-find-a-startup-business-partner-tickets-2003243556403","Eventbrite",1,""),
]
# --- Expansion 2026-10-26 (pass 2) ---
L+=[tuple(x) for x in json.load(open('s2/picks.json'))]
L+=[
("2026-10-28T19:00:00-02:30","2026-10-28T21:00:00-02:30","Kyla Cobbler: Gone Rogue Live","Arts and Culture Centre, 95 Allandale Road, St. John's, NL","https://destinationstjohns.com/event/kyla-cobbler-gone-rogue-live/","Destination St. John's",0,""),
("2026-11-05T08:30:00-03:30","2026-11-05T12:30:00-03:30","Business and Arts NL (Un)Common Threads: Creativity & Innovation Summit 2026","Sheraton Hotel Newfoundland, 115 Cavendish Square, St. John's, NL","https://businessandartsnl.com/uncommon-threads/summit-2026","Destination St. John's",0,""),
("2026-11-05T10:00:00-03:30","2026-11-05T11:30:00-03:30","Board of Trade Coffee & Connect","The Board of Trade, Cabot Building 8th Floor, 100 New Gower St, St. John's, NL","https://members.theboardoftrade.ca/events/details/coffee-connect-4618","The Board of Trade",0,""),
("2026-11-05T12:00:00-03:30","2026-11-05T19:00:00-03:30","Craft Council of NL Christmas Craft Fair (runs Nov 5-8)","Jack Byrne Arena, 7 Kennedys Brook Drive, Torbay, NL","https://www.craftcouncilnl.ca/craft-fair/craft-fair","Craft Council NL",0,""),
("2026-11-26T17:00:00-03:30","2026-11-26T23:00:00-03:30","2026 Board of Trade Business Awards Gala","Delta Hotel, 120 New Gower Street, St. John's, NL","https://members.theboardoftrade.ca/events/details/2026-board-of-trade-business-awards-4575","The Board of Trade",0,""),
("2026-11-29T12:00:00-03:30","2026-11-29T14:00:00-03:30","Downtown St. John's Christmas Parade","Downtown St. John's, NL","https://downtownstjohns.com/signature-events/christmas-parade/","Downtown St. John's",0,""),
("2026-11-05T12:00:00-07:00","2026-11-05T13:00:00-07:00","Data Centres: Are We Regulating Intelligently? (Alberta)","Online (Environmental Law Centre)","https://elc.ab.ca/post-library/webinar-data-centres-are-we-regulating-intelligently/","Organiser page",1,""),
("2026-11-19T13:00:00-05:00","2026-11-19T14:00:00-05:00","Energy Strategy: How Hyperscalers and AI Labs Are Securing Power","Online (Wood Mackenzie)","https://www.woodmac.com/events/2026-large-loads-and-data-centre-webinar-series/","Organiser page",1,""),
]
NOW=datetime.now(timezone.utc)
def p(s):
  if s.startswith('R'): return datetime.fromisoformat(s[1:]).replace(tzinfo=TZ)
  return datetime.fromisoformat(s.replace('Z','+00:00'))
esc=lambda t:t.replace('\\','\\\\').replace(';','\\;').replace(',','\\,').replace('\n','\\n')
def fold(l):
  b=l.encode();out=[]
  while len(b)>73:
    i=73
    while (b[i]&0xC0)==0x80:i-=1
    out.append(b[:i].decode());b=b[i:]
  out.append(b.decode());return '\r\n '.join(out)
now=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
seen=set();lines=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//Grok Bot//Nearby + Virtual//EN","CALSCALE:GREGORIAN","METHOD:PUBLISH","X-WR-CALNAME:Nearby + Virtual","X-WR-TIMEZONE:America/St_Johns","REFRESH-INTERVAL;VALUE=DURATION:PT12H","X-PUBLISHED-TTL:PT12H"]
rows=[]
for s,e,t,loc,url,src,v,n in L:
  st=p(s);en=p(e) if e and 'T' in e else st+timedelta(hours=2)
  if en<NOW: continue
  title=("[virtual] " if v else "")+t
  k=(st.astimezone(timezone.utc).isoformat(),t.lower())
  if k in seen: continue
  seen.add(k)
  d=f"Source: {url}\nVia: {src}\nLocal time: {st.astimezone(TZ):%a %b %d %Y %I:%M %p} NT"
  if n=="R": d+="\nEnd time not published; 2h placeholder."
  uid=hashlib.sha1((k[0]+k[1]).encode()).hexdigest()+"@nearby-virtual"
  lines+= ["BEGIN:VEVENT",f"UID:{uid}",f"DTSTAMP:{now}",f"DTSTART:{st.astimezone(timezone.utc):%Y%m%dT%H%M%SZ}",f"DTEND:{en.astimezone(timezone.utc):%Y%m%dT%H%M%SZ}",fold("SUMMARY:"+esc(title)),fold("LOCATION:"+esc(loc)),fold("DESCRIPTION:"+esc(d)),f"URL:{url}","TRANSP:TRANSPARENT","END:VEVENT"]
  rows.append((st.astimezone(TZ).strftime('%Y-%m-%d %H:%M NT'),title,src,url))
rows.sort()
lines.append("END:VCALENDAR")
open('nearby-virtual.ics','w',newline='').write('\r\n'.join(lines)+'\r\n')
json.dump(rows,open('events.json','w'),indent=1)
for r in sorted(rows): print(r[0],'|',r[1],'|',r[2])
print(len(rows))
