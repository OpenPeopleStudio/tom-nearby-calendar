# Hosting: Nearby + Virtual ICS feed
- Live: https://tom-nearby-calendar-6z8fv.ondigitalocean.app/nearby-virtual.ics (Content-Type text/calendar, verified 30 VEVENTs 2026-10-26 21:37 NDT; LIVE 115 VEVENTs (56 local, 59 virtual) verified 2026-10-26 22:22 NDT, see below)
- Subscribe: webcal://tom-nearby-calendar-6z8fv.ondigitalocean.app/nearby-virtual.ics
- DO App Platform app id: 245e7be9-b526-481d-bd4f-5ffc07f94960 (name tom-nearby-calendar, region tor/tor1, single static site component "feed", tier starter = free)
- Repo (public): https://github.com/OpenPeopleStudio/tom-nearby-calendar (branch main)
- Cost: $0. Free tier, static site only (1 of 3 free static sites; there were no other apps). No droplet, Spaces, DB or domain.

## Update
1. Rebuild nearby-virtual.ics (build.py) and push it to main of the repo.
2. Autodeploy is OFF: the app uses a public git URL because DigitalOcean's GitHub app is not authorized ("GitHub user not authenticated"). After a push, trigger a redeploy (DO console > app > Deploy, or apps-create-deployment via MCP).
   To get deploy-on-push: authorize the DigitalOcean GitHub app for this repo at https://cloud.digitalocean.com/apps/new, then update the spec to use `github: {repo: OpenPeopleStudio/tom-nearby-calendar, branch: main, deploy_on_push: true}`.
Note: GitHub API upload turned the file's CRLF line endings into LF; calendar clients accept this, but strict validators may warn.

## Build
`python3 build.py` (reads s2/picks.json for scraped Eventbrite picks; drops events whose end is past). Scraper scripts: s2/eb.py (listing URLs) then s2/det.py (per-event JSON-LD) then s2/picks.py (curated name list).

## Redeploy workaround (until DO GitHub auth is connected)
The app uses a public `git` source (no GitHub app auth), so DO reuses its cached build/commit on spec re-apply. What works ($0): push changes to a NEW branch (e.g. `live-YYYYMMDD[b]`), then `apps/apps-update` the spec with `static_sites[0].git.branch` set to that branch. DO then clones the new commit. Currently live from branch `live-20261026` @ 48ea528. Connecting GitHub in DO (github source + deploy_on_push) would remove this step.
