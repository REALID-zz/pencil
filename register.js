const puppeteer = require('puppeteer-core');
const path = require('path');

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';

(async () => {
  const browser = await puppeteer.launch({
    headless: false,
    executablePath: CHROME,
    args: ['--proxy-server=http://127.0.0.1:7897'],
    defaultViewport: { width: 1400, height: 900 }
  });

  const page = await browser.newPage();

  try {
    console.log('1. Going to Painting entry form...');
    await page.goto('https://beautifulbizarreartprize.art/enter-beautiful-bizarre-art-prize/entry-painting/', {
      waitUntil: 'networkidle2',
      timeout: 30000
    });
    await new Promise(r => setTimeout(r, 3000));
    await page.screenshot({ path: 'output/paint-form-1.jpg', type: 'jpeg', quality: 85 });

    // Get all form fields
    const formFields = await page.evaluate(() => {
      const inputs = document.querySelectorAll('input, select, textarea');
      return Array.from(inputs).map(el => ({
        tag: el.tagName,
        type: el.type || '',
        name: el.name || '',
        id: el.id || '',
        placeholder: el.placeholder || '',
        label: el.labels?.[0]?.textContent?.trim() || '',
        required: el.required,
        className: el.className.substring(0, 60)
      }));
    });
    console.log('Form fields:', JSON.stringify(formFields, null, 2));

    // Get page text
    const bodyText = await page.evaluate(() => document.body.innerText.substring(0, 5000));
    console.log('\nPage text:', bodyText.substring(0, 3000));

    // Scroll down to see the form
    await page.evaluate(() => window.scrollBy(0, 500));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({ path: 'output/paint-form-2.jpg', type: 'jpeg', quality: 85 });

    await page.evaluate(() => window.scrollBy(0, 500));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({ path: 'output/paint-form-3.jpg', type: 'jpeg', quality: 85 });

    await page.evaluate(() => window.scrollBy(0, 500));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({ path: 'output/paint-form-4.jpg', type: 'jpeg', quality: 85 });

    await page.evaluate(() => window.scrollBy(0, 500));
    await new Promise(r => setTimeout(r, 1000));
    await page.screenshot({ path: 'output/paint-form-5.jpg', type: 'jpeg', quality: 85 });

  } catch (err) {
    console.error('Error:', err.message);
  }

  await browser.close();
  console.log('Done');
})();
