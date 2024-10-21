---
title: LEDs
---

## HDR LEDs

* SK9822

## WS2812b

### Timing

* Approx 30 us per LED.
* Max LEDs at framerate f (in hz): `n = 33333/f`
  * 60 Hz: 555 LEDs
  * 100 Hz: 333 LEDs
