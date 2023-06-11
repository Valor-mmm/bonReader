from scan_bon import scan_bon
from bon_kind.dm_bon import dm_bon_indication
from bon_kind.dm_bon import DMParser

parsers = [DMParser]

if __name__ == '__main__':
    print('Hi Valor')
    scanned_text = scan_bon('./sample_images/bon02.jpg', False)

    largest_ratio = 0
    for line in bon_lines:
        for p, index in parsers:
            print(p, index)





