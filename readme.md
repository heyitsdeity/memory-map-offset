# Memory-Map-Offset

Memory Map Offset (MMO) is a command-line script to quickly add an offset to a .MAP file, a C-Type memory map format commonly found in first-party Nintendo games. It is primarily intended for usage with [Dolphin Emulator](https://github.com/dolphin-emu/dolphin)'s debug mode.

- [Memory-Map-Offset](#memory-map-offset)
  - [Installation / Usage](#installation--usage)
  - [Contributing](#contributing)
  - [License / Credit](#license--credit)

## Installation / Usage

MMO runs on Python 3.7 and requires no dependencies.

```
usage: memory-map-offset.py [-h] -i INPUT -o OFFSET [-x OUTPUT]

Add an offset to a dolphin memory map.

optional arguments:
  -h, --help  show this help message and exit
  -i INPUT    path to input map file
  -o OFFSET   memory offset
  -x OUTPUT   path to output file; defaults to input file
```

Modifying a MAP file is as simple as running a single command:

```bash
python3 memory-map-offset.py -i YOURGAMEID.map -o 8000000
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License / Credit

MMO is licensed under the [MIT License](https://opensource.org/licenses/MIT). Created by @heyitsdeity with bugfixes by @makusu2.