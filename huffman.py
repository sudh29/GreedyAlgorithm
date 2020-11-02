# huffman coding using greedy algorithm
import heapq as hp
from collections import defaultdict


def huffmanEncode(cfreq):
    heap = [[freq, [sym, ""]] for sym, freq in cfreq.items()]
    hp.heapify(heap)
    # print(heap)
    while len(heap) > 1:
        low = hp.heappop(heap)
        high = hp.heappop(heap)
        # print("low", low[1:])
        # print("high", high[1:])
        for pair in low[1:]:
            pair[1] = "0" + pair[1]
        for pairh in high[1:]:
            pairh[1] = "1" + pairh[1]
        hp.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])
    return sorted(hp.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


inputText = "This is an example of huffamn coding using greedy approach"
cfreq = defaultdict(int)
for c in inputText:
    cfreq[c] += 1
huffcodes = huffmanEncode(cfreq)
print("Symbol\t Frequency\t Huffamn Code")
for p in huffcodes:
    print("%s\t %s\t\t %s" % (p[0], cfreq[p[0]], p[1]))
