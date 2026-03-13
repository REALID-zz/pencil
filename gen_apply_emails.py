import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

BASE = os.path.dirname(os.path.abspath(__file__))

BIO = """Mengzhen Yang (DCT) is a Chinese visual artist born in 1993 in Ma'anshan, China. She studied fine art at Gwangju University in South Korea before relocating to the United States, where she spent nearly a decade building her professional practice in Los Angeles and New York.

Her work has been exhibited internationally at the Boston Asia Contemporary Art Exhibition (BACAF 2016), the World Trade Center's THE OCULUS ART SHOW in New York, and the Council of Asian Designers of America (CADA) exhibition at 415 Broadway, New York. She has shown with CHAMELEON GALLERY (New York) and collaborated with LA-based street fashion brand 212'FUN.

In 2020, Yang was recognized as one of the AACYF Top 30 Under 30 Outstanding Chinese in the United States and received a Certificate of Congressional Recognition from U.S. Representative Gilbert R. Cisneros Jr. (California, 39th District). She has served as Artist Coordinator of the California Music and Art Alliance (CAMAC) and participated in SOCAL ELITE CONNECT 2019.

Yang holds a recommendation from Prof. Xiang Jian, Lecturer at the University of Southern California (USC), who is also a collector of her oil paintings.

For over a decade, Yang has worked exclusively by hand — oil on canvas, charcoal, watercolor — creating large-scale, physically intensive paintings built through palette knife and impasto techniques. Her painting "I Am a Growth" took over three years to complete. Most of her works originate from dreams — unconscious imagery translated through physical labor into sculptural paint surfaces. Recently, she has begun exploring the intersection of traditional hand-painting and digital media — merging charcoal portraiture with digital disruption, and translating painterly gesture into generative code."""

PORTFOLIO = "https://realid-zz.github.io/pencil/"

def make_eml(to, subject, body_html, attachments, filename):
    msg = MIMEMultipart()
    msg['From'] = 'hihelloaikenni@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body_html, 'html', 'utf-8'))
    for img_path, img_name in attachments:
        full = os.path.join(BASE, img_path)
        if os.path.exists(full):
            with open(full, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-Disposition', 'attachment', filename=img_name)
                msg.attach(img)
            print(f'  + {img_name}')
    out = os.path.join(BASE, filename)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(msg.as_string())
    sz = os.path.getsize(out) / 1024 / 1024
    print(f'  => {filename} ({sz:.1f}MB)')

imgs = [
    ('submit-ready/Mengzhen Yang_Jungle Descent_Oil on Canvas_2026.jpg', 'Jungle_Descent_Oil_2026.jpg'),
    ('submit-ready/Mengzhen Yang_Crimson Sovereign_Oil on Canvas_120x180cm_2026.jpg', 'Crimson_Sovereign_Oil_2026.jpg'),
    ('submit-ready/Mengzhen Yang_I Am a Growth_Oil on Canvas_26x24in_2019.jpg', 'I_Am_a_Growth_Oil_2019.jpg'),
]

bio_html = BIO.replace('\n\n', '</p><p>').replace('\n', ' ')
bio_html = f'<p>{bio_html}</p>'

# === 1. NONAME STUDIO SHANGHAI ===
print('\n=== 1. Noname Studio Shanghai ===')
make_eml(
    'noname.studio@yahoo.com',
    'Artist Residency Application \u2014 Mengzhen Yang (DCT)',
    f"""<html><body style="font-family:Georgia,serif;color:#222;line-height:1.9;font-size:15px">
<p>Dear Noname Studio Selection Committee,</p>

<p>I am writing to formally apply for the artist residency program at Noname Studio in Zhujiajiao, Shanghai.</p>

{bio_html}

<h3 style="color:#333;font-size:14px;letter-spacing:1px">RESIDENCY PROPOSAL</h3>
<p>I wish to apply for a <b>2\u20133 month residency</b> to develop a new series of large-scale oil paintings exploring the convergence of Eastern landscape tradition and contemporary abstraction. The generous 300sqm studio space at Noname would be ideal for the physically demanding scale of my practice. I am pleased to donate one completed work to the foundation collection as part of the residency terms.</p>

<h3 style="color:#333;font-size:14px;letter-spacing:1px">PORTFOLIO</h3>
<p><a href="{PORTFOLIO}">{PORTFOLIO}</a></p>

<h3 style="color:#333;font-size:14px;letter-spacing:1px">REFERENCE</h3>
<p>Prof. Xiang Jian, University of Southern California \u2014 <a href="mailto:xjian@usc.edu">xjian@usc.edu</a></p>

<p>Selected works are attached for your review. I would be grateful for the opportunity to discuss my application further.</p>

<p>Respectfully,<br>
<b>Mengzhen Yang (DCT)</b><br>
<a href="mailto:hihelloaikenni@gmail.com">hihelloaikenni@gmail.com</a><br>
<a href="{PORTFOLIO}">{PORTFOLIO}</a></p>
</body></html>""",
    imgs,
    'email-noname-studio.eml'
)

# === 2. SERLACHIUS FINLAND ===
print('\n=== 2. Serlachius Residency Finland ===')
make_eml(
    'residency@serlachius.fi',
    'Residency Application 2027 \u2014 Mengzhen Yang (DCT), Visual Artist',
    f"""<html><body style="font-family:Georgia,serif;color:#222;line-height:1.9;font-size:15px">
<p>Dear Anita Hannunen and the Serlachius Residency Selection Committee,</p>

<p>I am writing to apply for the Serlachius Residency for 2027. I have also submitted the formal application through the Webropol online form.</p>

{bio_html}

<h3 style="color:#333;font-size:14px;letter-spacing:1px">RESIDENCY PROPOSAL</h3>
<p><b>Project: Between Dream and Material \u2014 Large-Scale Oil Painting Series</b></p>
<p>I propose to develop a new body of large-scale oil paintings during a 2\u20134 month residency, inspired by the Finnish landscape, its distinctive light conditions, and the unique dialogue between nature and industrial heritage that defines M\u00e4ntt\u00e4. My deeply physical working process \u2014 palette knife impasto built over sustained periods \u2014 aligns naturally with the focused, extended residency format that Serlachius offers.</p>
<p>I am drawn to the intersection of the Serlachius Museums' world-class collections and the contemplative solitude of M\u00e4ntt\u00e4. I would welcome the opportunity to organize an exhibition or open studio event in the residency gallery space during my stay.</p>

<h3 style="color:#333;font-size:14px;letter-spacing:1px">PORTFOLIO</h3>
<p><a href="{PORTFOLIO}">{PORTFOLIO}</a></p>

<h3 style="color:#333;font-size:14px;letter-spacing:1px">REFERENCE</h3>
<p>Prof. Xiang Jian, University of Southern California \u2014 <a href="mailto:xjian@usc.edu">xjian@usc.edu</a></p>

<p>Selected works are attached. Thank you for your time and consideration.</p>

<p>Warm regards,<br>
<b>Mengzhen Yang (DCT)</b><br>
<a href="mailto:hihelloaikenni@gmail.com">hihelloaikenni@gmail.com</a><br>
<a href="{PORTFOLIO}">{PORTFOLIO}</a></p>
</body></html>""",
    imgs,
    'email-serlachius.eml'
)

# === 3. CORRIDOR FOUNDATION SHENZHEN ===
print('\n=== 3. Corridor Foundation Shenzhen ===')
make_eml(
    'info@corridorfoundation.com',
    'Artist Residency Inquiry \u2014 Mengzhen Yang (DCT)',
    f"""<html><body style="font-family:Georgia,serif;color:#222;line-height:1.9;font-size:15px">
<p>Dear Corridor Foundation Team,</p>

<p>I am writing to inquire about the current availability of your artist residency program in Shenzhen.</p>

{bio_html}

<h3 style="color:#333;font-size:14px;letter-spacing:1px">PORTFOLIO</h3>
<p><a href="{PORTFOLIO}">{PORTFOLIO}</a></p>

<p>Could you kindly advise whether the residency is currently accepting applications, or when the next open call is expected? I would be grateful for any information regarding the application process.</p>

<p>Selected works are attached for your reference.</p>

<p>Best regards,<br>
<b>Mengzhen Yang (DCT)</b><br>
<a href="mailto:hihelloaikenni@gmail.com">hihelloaikenni@gmail.com</a><br>
<a href="{PORTFOLIO}">{PORTFOLIO}</a></p>
</body></html>""",
    imgs,
    'email-corridor.eml'
)

# === 4. SWATCH ART PEACE HOTEL ===
print('\n=== 4. Swatch Art Peace Hotel Shanghai ===')
make_eml(
    'artpeacehotel@swatch.com',
    'Artist-in-Residence Application \u2014 Mengzhen Yang (DCT)',
    f"""<html><body style="font-family:Georgia,serif;color:#222;line-height:1.9;font-size:15px">
<p>Dear Swatch Art Peace Hotel Selection Committee,</p>

<p>I am writing to apply for the artist-in-residence program at the Swatch Art Peace Hotel on the Bund, Shanghai.</p>

{bio_html}

<h3 style="color:#333;font-size:14px;letter-spacing:1px">RESIDENCY PROPOSAL</h3>
<p>I wish to apply for a <b>3\u20136 month residency</b> to create a new body of large-scale oil paintings examining the intersection of Eastern and Western painterly traditions. Having spent nearly a decade between South Korea and the United States, and now returned to China, I seek to synthesize these cross-cultural experiences through painting. Shanghai's position as a cultural crossroads \u2014 and the Swatch Art Peace Hotel's extraordinary location on the Bund \u2014 provide the ideal context for this body of work.</p>

<h3 style="color:#333;font-size:14px;letter-spacing:1px">PORTFOLIO</h3>
<p><a href="{PORTFOLIO}">{PORTFOLIO}</a></p>

<h3 style="color:#333;font-size:14px;letter-spacing:1px">REFERENCE</h3>
<p>Prof. Xiang Jian, University of Southern California \u2014 <a href="mailto:xjian@usc.edu">xjian@usc.edu</a></p>

<p>Selected works are attached. I am also completing the online application through your portal. Thank you for your consideration.</p>

<p>Respectfully,<br>
<b>Mengzhen Yang (DCT)</b><br>
<a href="mailto:hihelloaikenni@gmail.com">hihelloaikenni@gmail.com</a><br>
<a href="{PORTFOLIO}">{PORTFOLIO}</a></p>
</body></html>""",
    imgs,
    'email-swatch.eml'
)

print('\n=== ALL 4 EMAILS REGENERATED ===')
