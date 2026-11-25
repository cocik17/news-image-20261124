# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/cocik17/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/cocik17/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One page of world news from Tuesday 24 November 2026: 38 stories across 9 regions and 20 fields — 13 illustrated front-page stories plus 25 more — from a Huawei guilty verdict and the Dow above 50,000 to Gaza, Zaporizhzhia, a $41B biopharma deal, and a 5.6 earthquake in Nepal.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ydyxtegc&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>

## Stories in the image (38, all 24 November 2026)

**Europe (5)**
- Russian strike hits Zaporizhzhia — 2 killed, 40 wounded, including four children
- Lukashenko offers to fly Zelenskiy — Zelenskiy: bring Putin to Kyiv instead
- Teen opens fire at Serbian school — two staff hurt in Kragujevac; suspect held
- 2 arrested in break-in at royal home — Anmer Hall intruders held; royals away
- Germany gets Ukraine's Delta system — first ally to share battlefield software

**Middle East (7)**
- Israel kills Hamas security chief in Gaza — airstrike kills Naeem Abu Nahel and six others
- Riyadh tower hit in second strike — PIF tower targeted again within a week
- Tankers hit mines in Strait of Hormuz — fourth tanker ablaze; IRGC claims three hit
- Eisenkot clinches coalition deal — first pact in bid to form Israeli government
- UK sanctions Houthis and 4 officials — asset freezes over torture and detainee abuse
- US eyes Iran in ship cyberattacks — dozens of attacks on vessels, WSJ reports
- Iraq PM seizes Kurdish oilfields — Baghdad takes over fields and crossings

**East Asia (4)**
- Russian jets set off alert in Korea — Seoul scrambles fighters near Ulleung Island
- China probes top Shanghai official — 4th Politburo member probed since 2025
- Japan pays ICC dues early — 2027 contribution rushed ahead of US sanctions
- China extends minerals pause to US — gallium, germanium curbs on hold to Jan 27

**Asia & the Pacific (6)**
- 5.6 earthquake strikes Nepal — tremor hits Koshi province near China border
- Hasina plans return to Bangladesh — ex-PM to come home Dec 16 despite death sentence
- Malaysia to send back 6,803 Myanmar — repatriations in December despite genocide ruling
- Pakistan's first astronaut set for space — Zeeshan Ali to join China's Shenzhou-24 crew
- Gas blast kills 6 at Hanoi eatery — hot-pot restaurant blast injures 10-plus
- Solomons scrap China security pact — turns to Australia treaty instead

**Americas (5)**
- US charges 800+ in record scam sweep — $8 billion recovered in largest-ever crackdown
- Abrego Garcia to leave US voluntarily — ends deportation fight; flies to Spain
- Venezuela reveals $237.5B debt pile — 242% of GDP; restructuring looms
- Trump taps O'Neill for federal judge — ousted NC prosecutor nominated to bench
- Gunmen hold 25 hostage in Cartagena — armed men seize supermarket after failed truck raid

**Africa (3)**
- 175 migrants missing off Senegal — contact lost with Europe-bound pirogue
- Senegal regain AFCON title — CAS restores 1-0 win over Morocco
- RSF spy chief defects to Sudan army — Al-Tayeb Jabara quits in video statement

**Markets (2)**
- Sanofi buys Insmed for $41 billion — biggest biopharma deal of the year
- Dow closes back above 50,000 — Dow 50,018.70 (+0.9%); Nasdaq slides 1.5%

**Sport (2)**
- Real Madrid rout PSV 5-1 in comeback — Mbappe scores twice as Real hit five
- Chess title fight opens with draw — Gukesh holds Sindarov in Game 1, Geneva

**World (4)**
- US jury finds Huawei guilty in trade-secrets case — guilty on 10 of 12 counts, cleared of racketeering
- Record 5,258 heat deaths in England — summer 2026 toll highest since 2016
- Bus hits truck in Ras Al Khaimah: 13 dead — bus carried 41; 14 hurt
- Ariane 6 lofts 36 Amazon satellites — 10th flight of Europe's heavy rocket

Every story was verified from at least two sources (Reuters, AP, BBC, WSJ, Al Jazeera, Xinhua, Straits Times, CNN, The Hindu, NYT, UKHSA, The National, Gulf Business, France 24, Sky Sports, AIAA). Events from 23 November or earlier were excluded and are listed in the image's DATE CHECK box (the Nvidia CEO reinstatement, Russia's 'open war' warning to Estonia, the Iowa explosives court ruling, and the Senate probe of Vance — all 23 November; the Russian warship sunk off Libya and COP31 ending without a deal — both 22 November). Two more candidates were checked and rejected for the same reason: the Vanuatu–Australia pact (signed 29 June 2026) and Bolsonaro's ICU stay (since 21 November).

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
