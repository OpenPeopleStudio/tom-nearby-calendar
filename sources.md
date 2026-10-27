# Sources (checked 2026-10-26)
| Source | Real feed for refresh? | URL |
|---|---|---|
| personal_radar | Yes - SQL (read-only), rows lack end time and often a URL | public.personal_radar where category='event' |
| Luma local (geo 47.56,-52.71) | Yes - JSON API (unofficial) | https://api.lu.ma/discover/get-paginated-events?latitude=47.56&longitude=-52.71&pagination_limit=50 |
| Luma category (ai/tech/climate) | API works but geolocates to server IP (Seattle, in-person) - NOT usable for virtual; no online filter found | https://api.lu.ma/discover/get-paginated-events?slug=ai |
| Eventbrite St. John's | No feed; listing page JSON-LD (dates only) + per-event page startDate/endDate with offsets | https://www.eventbrite.ca/d/canada--st-johns/business--events/ |
| Eventbrite online | Same scrape method; topics artificial-intelligence, startups, venture-capital, energy, founders | https://www.eventbrite.ca/d/online/<topic>/ |
| Genesis Centre | Schema.org JSON-LD on events page (scrapable, small) | https://www.genesiscentre.ca/events |
| techNL | The Events Calendar (WordPress) but ?ical=1 and /wp-json/tribe/events/v1 returned HTML/nothing - no usable feed found | https://technl.ca/events/ |
| Memorial University | /main/events/ 404 - not yet located | https://www.mun.ca/ |
| City of St. John's, Destination St. John's, Meetup | Not checked in slice 1 | stjohns.ca / destinationstjohns.com / meetup.com |
