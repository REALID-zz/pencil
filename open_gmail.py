import urllib.parse, subprocess

emails = [
    {
        'to': 'noname.studio@yahoo.com',
        'su': 'Artist Residency Application - Mengzhen Yang (DCT)',
        'body': """Dear Noname Studio Team,

My name is Mengzhen Yang (artist name: DCT), a Chinese visual artist born in 1993 in Ma'anshan, Anhui Province. I am writing to apply for the artist residency program at Noname Studio in Zhujiajiao, Shanghai.

ABOUT MY PRACTICE
For over a decade, I have worked exclusively by hand - oil on canvas, charcoal, watercolor - creating large-scale, physically intensive paintings built through palette knife and impasto techniques over months and years. My painting "I Am a Growth" took over three years to complete. Most of my paintings originate from dreams.

Recently, I have begun exploring the intersection of traditional hand-painting and digital media.

PORTFOLIO
https://realid-zz.github.io/pencil/

RESIDENCY PLAN
I would like to apply for a 2-3 month residency to develop a new series of large-scale oil paintings. The 300sqm studio would be ideal for my large-format work. I am happy to donate one work to the foundation collection.

CONTACT
Name: Mengzhen Yang
Artist Name: DCT
Email: hihelloaikenni@gmail.com
Nationality: Chinese
Born: 1993, Ma'anshan, China
Medium: Oil painting, charcoal, mixed media, generative art

Selected works attached. Thank you for your consideration.

Best regards,
Mengzhen Yang (DCT)"""
    },
    {
        'to': 'residency@serlachius.fi',
        'su': 'Residency Application - Mengzhen Yang (DCT), Chinese Visual Artist',
        'body': """Dear Serlachius Residency Team,

My name is Mengzhen Yang (artist name: DCT), a Chinese visual artist. I am writing to apply for the Serlachius Residency 2027.

ABOUT MY WORK
I have been painting by hand for over a decade - oil on canvas using palette knife and impasto techniques, creating large-scale works over months and years. My painting "I Am a Growth" required three years. Most of my paintings originate from dreams.

Recently I began exploring traditional painting and digital media - merging charcoal with digital disruption, and translating painterly gesture into generative code.

RESIDENCY PROPOSAL
Project: Between Dream and Material - Large-Scale Oil Painting Series
I plan to develop new large-scale oil paintings inspired by Finnish landscape and the dialogue between nature and industrial heritage in Mantta. I would welcome the chance to organize an exhibition during the residency.

PORTFOLIO
https://realid-zz.github.io/pencil/

ARTIST INFO
Name: Mengzhen Yang (DCT)
Nationality: Chinese
Born: 1993
Email: hihelloaikenni@gmail.com
Travel: Alone
Language: Chinese (native), English (fluent)
Profession: Visual Artist / Painter

Selected works attached. I will also submit via the online form.

Warm regards,
Mengzhen Yang (DCT)"""
    },
    {
        'to': 'info@corridorfoundation.com',
        'su': 'Artist Residency Inquiry - Mengzhen Yang (DCT)',
        'body': """Dear Corridor Foundation Team,

My name is Mengzhen Yang (artist name: DCT), a Chinese visual artist based in Ma'anshan. I am writing to inquire about your artist residency program in Shenzhen.

For over a decade, I have worked exclusively by hand - oil on canvas, charcoal, watercolor - creating large-scale paintings. My painting "I Am a Growth" took over three years. Most of my paintings originate from dreams. Recently I began exploring traditional painting and digital media intersections.

PORTFOLIO
https://realid-zz.github.io/pencil/

Is the residency currently accepting applications? I would be grateful for any information about the next open call.

Selected works attached. Thank you.

Best regards,
Mengzhen Yang (DCT)
hihelloaikenni@gmail.com"""
    },
    {
        'to': 'artpeacehotel@swatch.com',
        'su': 'Artist Residency Application - Mengzhen Yang (DCT), Oil Painter',
        'body': """Dear Swatch Art Peace Hotel Team,

My name is Mengzhen Yang (artist name: DCT), a Chinese visual artist born in 1993. I would like to apply for the artist-in-residence program at the Swatch Art Peace Hotel, Shanghai.

ABOUT MY PRACTICE
I have been painting by hand for over a decade - oil on canvas, charcoal, watercolor - creating large-scale paintings through palette knife and impasto techniques. "I Am a Growth" took three years. Most of my paintings come from dreams.

Recently I began exploring traditional hand-painting and digital media.

RESIDENCY PLAN
I would like to apply for a 3-6 month residency to create a new body of large-scale oil paintings exploring the intersection of Eastern and Western painterly traditions.

PORTFOLIO
https://realid-zz.github.io/pencil/

ARTIST INFO
Full Name: Mengzhen Yang
Artist Name: DCT
Nationality: Chinese
Born: 1993, Ma'anshan, Anhui, China
Medium: Oil painting, charcoal, mixed media, generative art
Email: hihelloaikenni@gmail.com

Selected works attached. Thank you for your consideration.

Best regards,
Mengzhen Yang (DCT)"""
    }
]

for i, e in enumerate(emails):
    params = urllib.parse.urlencode({'view': 'cm', 'fs': '1', 'to': e['to'], 'su': e['su'], 'body': e['body']})
    url = f"https://mail.google.com/mail/?{params}"
    subprocess.Popen(['cmd', '/c', 'start', '', url], shell=False)
    print(f"[{i+1}] Opened: -> {e['to']}")
