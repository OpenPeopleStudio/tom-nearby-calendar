# Sources (checked 2026-10-26)
| Source | Real feed for refresh? | URL |
|---|---|---|
| personal_radar (Supabase udiegusxhxtnraopnywe) | Yes - SQL (read-only), rows lack end time and often a URL | public.personal_radar where category='event' |
| Luma local (geo 47.56,-52.71) | Yes - JSON API (unofficial) | https://api.lu.ma/discover/get-paginated-events?latitude=47.56&longitude=-52.71&pagination_limit=50 |
| Luma category (ai/tech/climate) | API works but geolocates to server IP (Seattle, in-person) - NOT usable for virtual; no online filter found | https://api.lu.ma/discover/get-paginated-events?slug=ai |
| Eventbrite St. John's | No feed; listing page JSON-LD (dates only) + per-event page startDate/endDate with offsets | https://www.eventbrite.ca/d/canada--st-johns/business--events/ |
| Eventbrite online | Same scrape method; topics artificial-intelligence, startups, venture-capital, energy, founders | https://www.eventbrite.ca/d/online/<topic>/ |
| Genesis Centre | Schema.org JSON-LD on events page (scrapable, small) | https://www.genesiscentre.ca/events |
| techNL | The Events Calendar (WordPress) but ?ical=1 and /wp-json/tribe/events/v1 returned HTML/nothing - no usable feed found | https://technl.ca/events/ |
| Memorial University | /main/events/ 404 - not yet located | https://www.mun.ca/ |
| City of St. John's, Destination St. John's, Meetup | Not checked in slice 1 | stjohns.ca / destinationstjohns.com / meetup.com |

## Pass 2 (2026-10-26 ~22:30 NT) - expansion to early Jan 2027
| Source | Result |
|---|---|
| Eventbrite St. John's (business, science-and-tech, community, government, arts, music, charity, events; pages 1-3) + Eventbrite online (AI, startups, VC, energy, data-center, founders, grants, cleantech, fundraising, investors, renewable-energy, machine-learning; pages 1-2) | 714 event URLs scraped; per-event JSON-LD (startDate/endDate with offset). Hand-curated: 6 new local + 42 new virtual. Spam/real-estate/healing/course listings excluded. |
| Luma local API | Only the 2 events already in feed |
| Genesis Centre JSON-LD | Only T-Minus30 (started Oct 19, all-month sprint) and Build48 (Mar 2027) - nothing new in window |
| techNL /events/ | No machine-readable event data (archive page only; REST 404) - empty |
| The Board of Trade (members.theboardoftrade.ca) | 2 events (Coffee & Connect Nov 5, Business Awards Nov 26) |
| Destination St. John's (WP REST via WebFetch; curl from box hits SiteGround captcha) | 3 picks (BANL Summit, Kyla Cobbler, Craft Fair); rest are recurring bar/open-mic listings |
| Downtown St. John's | Christmas Parade Nov 29 |
| Organiser pages (web search) | Environmental Law Centre data-centre webinar (Nov 5), Wood Mackenzie hyperscaler power webinar (Nov 19) |
| Memorial (gazette.mun.ca) | 504 timeout; search hits had weekday/date mismatches (likely old years) - skipped |
| Meetup, Propel, City of St. John's calendar | Not scraped this pass (Propel /events 404) |

## Pass 3 (entertainment, 2026-10-26 ~22:45 NT)
| Source | Result |
|---|---|
| Eventbrite St. John's (arts/music/community already scraped) | 15 shows (concerts, The Ship, Celtic Fiddlers, comedy/magic, Halloween, Tibbs Eve) + 3 business (Export Café YYT, NLBA Awards, Atlantic CMP Conference) |
| Holy Heart Theatre (holyhearttheatre.com) | 10 timed shows (Shallaway, Miracle on 34th St, Lady Cove, Christmas to Remember, The Once, Ennis Sisters). Untimed items (Nathan Carter Nov 4, Dardanelles Dec 28, Sheila Williams) skipped |
| Mary Brown's Centre (mbcentre.ca) | Stars on Ice Dec 2, Johnny Reid Dec 12 (Jimmy Carr already in feed) |
| LSPU Hall / RCA (lspuhall.ca) | A Time in the Old Hall Dec 15; Short Play Festival and Feast of Cohen listed without times - skipped |
| Arts and Culture Centre | Irish Descendants Christmas Dec 23 (band tour page) |
| JAG/Soundhouse, Spirit of Newfoundland, Ticketmaster | Not checked this pass (time) |
