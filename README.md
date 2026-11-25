# Ringkasan Berita Dunia — 24 November 2026

Entry untuk bounty make.fun `news-image-20261124`: satu gambar yang
merangkum berita dunia Selasa, 24 November 2026.

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
