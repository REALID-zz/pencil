const puppeteer = require('puppeteer-core');
const fs = require('fs');

const CHROME_PATHS = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
];
function findChrome() {
  for (const p of CHROME_PATHS) { if (fs.existsSync(p)) return p; }
  throw new Error('Chrome not found');
}

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    executablePath: findChrome(),
    defaultViewport: { width: 1400, height: 900 },
  });
  const pages = [
    ['https://realid-zz.github.io/pencil/', 'preview-home.png'],
    ['https://realid-zz.github.io/pencil/project-oil.html', 'preview-oil.png'],
    ['https://realid-zz.github.io/pencil/project-glitch.html', 'preview-glitch.png'],
    ['https://realid-zz.github.io/pencil/project-astral.html', 'preview-astral.png'],
  ];
  for (const [url, file] of pages) {
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
    await page.screenshot({ path: file });
    console.log('Done: ' + file);
    await page.close();
  }
  await browser.close();
})();
