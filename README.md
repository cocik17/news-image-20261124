# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/cocik17/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/cocik17/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image summing up the world's news of Tuesday 24 November 2026: six stories that defined the day, from Gaza to Zaporizhzhia, a $41B biopharma deal, a record US anti-scam sweep, Russian jets near South Korea, and a 5.6 earthquake in Nepal.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=ydyxtegc&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>

## Isi gambar

- Israel membunuh kepala keamanan dalam Hamas di Gaza
- Serangan Rusia ke Zaporizhzhia: 2 tewas, 40 luka-luka
- Sanofi membeli Insmed seharga $41 miliar
- AS mendakwa 800+ orang dalam razia penipuan terbesar sepanjang sejarah
- Jet Rusia memicu peringatan berlindung di Korea Selatan
- Gempa 5,6 mengguncang Nepal

Setiap cerita diverifikasi dari minimal dua sumber (Reuters, Just Security,
The Hindu, siaran pers Sanofi, Departemen Kehakiman AS, WSJ).

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
