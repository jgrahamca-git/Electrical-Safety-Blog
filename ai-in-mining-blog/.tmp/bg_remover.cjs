const Jimp = require('jimp');
const fs = require('fs');
const path = require('path');

const images = ['symbol-arc-flash.png', 'symbol-electrocution.png', 'symbol-hand-shock.png'];
const asset_dir = '/home/jgrah/Blog_EI_Safety/ai-in-mining-blog/src/assets/';

async function processImages() {
    for (let imgName of images) {
        let imgPath = path.join(asset_dir, imgName);
        console.log(`Processing ${imgName}...`);
        try {
            const image = await Jimp.read(imgPath);
            image.scan(0, 0, image.bitmap.width, image.bitmap.height, function (x, y, idx) {
                var red   = this.bitmap.data[idx + 0];
                var green = this.bitmap.data[idx + 1];
                var blue  = this.bitmap.data[idx + 2];

                if (red > 240 && green > 240 && blue > 240) {
                    this.bitmap.data[idx + 3] = 0; // Transparent
                }
            });
            await image.writeAsync(imgPath);
            console.log(`Done processing ${imgName}`);
        } catch (e) {
            console.log(`Error on ${imgName}:`, e);
        }
    }
}
processImages();
