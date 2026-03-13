const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME_PATHS = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
];

function findChrome() {
  for (const p of CHROME_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error('Chrome not found');
}

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    executablePath: findChrome(),
    defaultViewport: { width: 1400, height: 900 },
    args: ['--start-maximized'],
  });

  const page = await browser.newPage();

  console.log('Opening Beautiful Bizarre Art Prize - Painting entry...');
  await page.goto('https://beautifulbizarreartprize.art/enter-beautiful-bizarre-art-prize/entry-painting/', {
    waitUntil: 'networkidle2',
    timeout: 60000,
  });

  await page.screenshot({ path: 'bb-step1-loaded.png', fullPage: true });
  console.log('Screenshot saved: bb-step1-loaded.png');
  console.log('Page loaded. Browser will stay open for you to continue manually.');
  console.log('');
  console.log('=== FILL IN THE FOLLOWING ===');
  console.log('Email: hihelloaikenni@gmail.com');
  console.log('First Name: Mengzhen');
  console.log('Last Name: Yang');
  console.log('Country: China');
  console.log('Artist Name: Mengzhen Yang');
  console.log('Website: https://realid-zz.github.io/pencil/');
  console.log('');
  console.log('=== ARTWORK 1 (Painting) ===');
  console.log('Artwork Name: Jungle Descent');
  console.log('Materials: Oil on canvas, palette knife impasto');
  console.log('Upload: Use your ORIGINAL high-res photo from phone/camera');
  console.log('');
  console.log('Browser is open. Fill the form, then close browser when done.');

  await new Promise(() => {});
})();
