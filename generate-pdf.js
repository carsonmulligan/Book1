const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Load local HTML file
  await page.goto('file://' + __dirname + '/book_markdown_to_html.html', {
    waitUntil: 'networkidle0'
  });

  // Configure PDF options for vertical layout
  await page.pdf({
    path: 'vertical-book.pdf',
    format: 'A4',
    printBackground: true,
    margin: {
      top: '20mm',
      right: '15mm',
      bottom: '20mm',
      left: '15mm'
    },
    preferCSSPageSize: true
  });

  await browser.close();
})(); 