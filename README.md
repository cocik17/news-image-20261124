# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/cocik17/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/cocik17/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image summing up the world's news of Tuesday 24 November 2026: 32 stories across 7 regions, from Gaza to Zaporizhzhia, a $41B biopharma deal, a record US anti-scam sweep, Russian jets near South Korea, and a 5.6 earthquake in Nepal.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ydyxtegc&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>

## Stories in the image (32, all 24 November 2026)

**Middle East**
- Israel kills Hamas security chief in Gaza — airstrike kills Naeem Abu Nahel and six others
- Riyadh tower hit in second strike — PIF tower targeted again within a week
- Tankers hit mines in Strait of Hormuz — fourth tanker ablaze; IRGC claims three hit
- Eisenkot clinches coalition deal — first pact in bid to form Israeli government
- UK sanctions Houthis and 4 officials — asset freezes over torture and detainee abuse
- US eyes Iran in ship cyberattacks — dozens of attacks on vessels, WSJ reports
- Iraq PM seizes Kurdish oilfields — Baghdad takes over fields and crossings

**Ukraine & Europe**
- Russian strike hits Zaporizhzhia — 2 killed, 40 wounded, including four children
- Lukashenko offers to fly Zelenskiy — Zelenskiy: bring Putin to Kyiv instead
- Teen opens fire at Serbian school — two staff hurt in Kragujevac; suspect held
- 2 arrested in break-in at royal home — Anmer Hall intruders held; royals away
- Germany gets Ukraine's Delta system — first ally to share battlefield software

**East Asia**
- Russian jets set off alert in Korea — Seoul scrambles fighters near Ulleung Island
- China probes top Shanghai official — 4th Politburo member probed since 2025
- Japan pays ICC dues early — 2027 contribution rushed ahead of US sanctions
- China extends minerals pause to US — gallium, germanium curbs on hold to Jan 27

**Asia & the Pacific**
- 5.6 earthquake strikes Nepal — tremor hits Koshi province near China border
- Hasina plans return to Bangladesh — ex-PM to come home Dec 16 despite death sentence
- Malaysia to send back 6,803 Myanmar — repatriations in December despite genocide ruling
- Pakistan's first astronaut set for space — Zeeshan Ali to join China's Shenzhou-24 crew
- Gas blast kills 6 at Hanoi eatery — hot-pot restaurant blast injures 10-plus
- Solomons scrap China security pact — turns to Australia treaty instead

**Americas**
- US charges 800+ in record scam sweep — $8 billion recovered in largest-ever crackdown
- Abrego Garcia to leave US voluntarily — ends deportation fight; flies to Spain
- Venezuela reveals $237.5B debt pile — 242% of GDP; restructuring looms
- Trump taps O'Neill for federal judge — ousted NC prosecutor nominated to bench

**Africa**
- 175 migrants missing off Senegal — contact lost with Europe-bound pirogue
- Senegal regain AFCON title — CAS restores 1-0 win over Morocco
- RSF spy chief defects to Sudan army — Al-Tayeb Jabara quits in video statement

**Business, Space & Sport**
- Sanofi buys Insmed for $41 billion — biggest biopharma deal of the year
- Ariane 6 lofts 36 Amazon satellites — 10th flight of Europe's heavy rocket
- Chess title fight opens with draw — Gukesh holds Sindarov in Game 1, Geneva

Every story was verified from at least two sources (Reuters, AP, BBC, WSJ, Al Jazeera, Xinhua, Straits Times, CNN, The Hindu, NYT, Nature, Arianespace, Sanofi, US Dept. of Justice). Events from 23 November or earlier were excluded (e.g. the Nvidia CEO reinstatement, the Megaspeed blacklist, the Ukraine strike on a Russian warship off Libya, Russia's 'open war' warning to Estonia, the Iowa explosives court ruling, and the Senate probe of Vance — all 22–23 November).

## Cara jalan

Program ini mendekode gambar `entry.png.b64` (base64 dari `entry.png`)
ke `/output/entry.png`:

```sh
python3 main.py
```

Di luar container grader, direktori output bisa diatur lewat
`MAKEFUN_OUTPUT_DIR`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Lisensi

MIT — lihat `LICENSE`.
