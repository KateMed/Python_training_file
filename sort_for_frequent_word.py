
zen = """ Haruki Murakami was shocked and depressed to find his normal sixfigure
readership exploding into the millions when he published
Norwegian Wood in 1987. Fame was one thing, superstardom another,
and the craziness of it sent him back to the anonymity of Europe (he
had written the book in Greece and Italy). In 1991 he moved to the
United States. Not until 1995 was he prepared to resume living in
Japan, but strictly on his own terms, without the television
appearances and professional pontificating expected of a bestselling
Japanese author.
Norwegian Wood is still the one Murakami book that "everyone" in
Japan has read, but Murakami's young audience has grown up with
him as he has begun wrestling with Japan's dark past (in The Wind-up
Bird Chronicle) and the 1995 double punch of the Kobe earthquake
and, in Underground, the sarin gas attack on the Tokyo subway.
Accustomed to his cool, fragmented, American-flavoured narratives
on mysterious sheep and disappearing elephants, some of Murakami's
early readers were dismayed to find that Norwegian Wood seemed to
be "just" a love story - and one that bore a suspicious resemblance to
the kind of Japanese mainstream autobiographical fiction that
Murakami had rejected since his exciting debut in 1979. As Murakami
himself tells it, "Many of my readers thought that Norwegian Wood
was a retreat for me, a betrayal of what my works had stood for until
then. For me personally, however, it was just the opposite: it was an
adventure, a challenge. I had never written that kind of straight, simple
story, and I wanted to test myself. I set Norwegian Wood in the late
1960s. I borrowed the details of the protagonist's university
environment and daily life from those of my own student days. """

from collections import Counter
#split разбивает строку по пробельным символам
#strip очищает слово от того, что указано в скобках
#lover привоит все буквы к нижнему регистру
cleaned_list = []
for word in zen.split():
    cleaned_list.append(word.strip('.,-!').lower())
print(Counter(cleaned_list).most_common(3))