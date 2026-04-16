---
date: '2026-04-16T11:29:51+07:00'
draft: false
title: 'Water Level'
---

WIP.

logging:
15/04/2026
- I decided to use the code from [Azfar Rosdi](https://www.cytron.io/tutorial/esp32-water-tank-monitoring).
- I learnt that `pulseIn(pin, state)` is used to calculate
  how long certain `pin` go from `!state` to `state`.
  It returns the time spent in microseconds.
- Now why did the water level indicator not work on my waffer jar?
- I read from [HandsOn Tech User Guide](https://handsontec.com/dataspecs/sensor/SR-04-Ultrasonic.pdf) that the surface must have a minimum area of 0.5m<sup>2</sup>. Maybe that's why, need to confirm it anyway.
---
04/01/2026
- I learnt about SPIFFS (SPI Flash Filesystem). It's a file system used for SPI NOR flash device; a memory commonly used for embedded devices [GigaDevice](https://www.gigadevice.com/product/flash/spi-nor-flash).
- I learnt that SPIFFS is mounted at /spiffs.
- I learnt that SPIFFS store files in a flat structure. So, for example, if I store a file like /spiffs/dir/file1.txt, this file has a name "/dir/file1.txt" instead a file1.txt in a /dir/ directory [SPIFFS](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/storage/spiffs.html).
