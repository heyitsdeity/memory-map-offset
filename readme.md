# Memory-Map-Offset

Memory Map Offset is a Python 3.7 script which adds an offset to `.map` files, the symbol maps sometimes found in first party NGC/Wii games.

## Usage:

```bash
memory-map-offset.py [-h] -i INPUT -o OFFSET [-x OUTPUT]

Add an offset to a dolphin memory map.

optional arguments:
  -h, --help  show this help message and exit
  -i INPUT    path to input map file
  -o OFFSET   memory offset
  -x OUTPUT   path to output file; defaults to input file

$ python3 memory-map-offset.py -i YOURGAMEID.map -o 8000000
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Released under the [MIT License](https://opensource.org/licenses/MIT).
